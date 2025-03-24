import requests
import json
import os
from typing import Dict, Any
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
from urllib.parse import quote
import time
from tqdm import tqdm

def search_youtube(query: str, limit: int = 10) -> Dict[str, Any]:
    """Search YouTube videos using the provided API."""
    url = "https://yt-search-and-download-mp3.p.rapidapi.com/search"
    
    querystring = {
        "q": query,
        "limit": str(limit)
    }
    
    headers = {
        "x-rapidapi-key": os.getenv('RAPIDAPI_KEY'),
        "x-rapidapi-host": os.getenv('RAPIDAPI_HOST')
    }
    
    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error occurred while making the request: {e}")
        return {}

def display_results(results: Dict[str, Any]) -> None:
    """Display search results in a readable format."""
    if not results or 'videos' not in results:
        print("No results found or an error occurred.")
        return

    videos = results['videos']
    if not videos:
        print("No videos found for your search query.")
        return

    print("\nSearch Results:")
    print("-" * 50)
    
    for idx, video in enumerate(videos, 0):
        name = video.get('name', 'N/A')
        artist = 'Unknown'
        title = name
        if ' - ' in name:
            artist, title = name.split(' - ', 1)
        
        video_url = video.get('url', 'N/A')
        
        print(f"\n{idx}. Artist: {artist}")
        print(f"   Title: {title}")
        print(f"   URL: {video_url}")

def download_mp3(video_url: str, title: str) -> bool:
    """Download MP3 from YouTube video URL."""
    # Check if file already exists
    filename = f"music/{title}.mp3"
    if os.path.exists(filename):
        while True:
            response = input(f"\nFile '{filename}' already exists. Do you want to download it again? (y/n): ").lower()
            if response in ['y', 'yes']:
                break
            elif response in ['n', 'no']:
                return False
            print("Please enter 'y' or 'n'")
    
    url = "https://yt-search-and-download-mp3.p.rapidapi.com/mp3"
    querystring = {"url": video_url}
    
    headers = {
        "x-rapidapi-key": os.getenv('RAPIDAPI_KEY'),
        "x-rapidapi-host": os.getenv('RAPIDAPI_HOST')
    }
    
    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()
        data = response.json()
        
        if data.get('success') and data.get('download'):
            # Create music directory if it doesn't exist
            os.makedirs('music', exist_ok=True)
            
            # Get the download URL from base64-encoded string
            download_url = data['download']
            
            # Download the file with progress tracking using tqdm
            print("\nDownloading...")
            mp3_response = requests.get(download_url, stream=True)
            mp3_response.raise_for_status()
            
            total_size = int(mp3_response.headers.get('content-length', 0))
            block_size = 1024  # 1 Kilobyte
            
            filename = f"music/{title}.mp3"
            
            with open(filename, 'wb') as f, tqdm(
                desc=title,
                total=total_size,
                unit='iB',
                unit_scale=True,
                unit_divisor=1024,
                bar_format='{desc}: {percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}]'
            ) as pbar:
                for data in mp3_response.iter_content(block_size):
                    size = f.write(data)
                    pbar.update(size)
            
            print(f"\nSuccessfully downloaded: {filename}")
            return True
        else:
            print("\nError: Invalid response format or download URL not found")
            return False
            
    except requests.RequestException as e:
        print(f"\nError downloading MP3: {e}")
        return False

def main():
    while True:
        query = input("\nEnter artist name and/or song title (or 'quit' to exit): ").strip()
        
        if query.lower() in ["quit", "q"]:
            print('Thank you')
            break
        
        if not query:
            print("Please enter a valid search term.")
            continue

        while True:
            try:
                limit = input("Enter number of results to show (1-40, default 10): ").strip()
                if not limit:
                    limit = 10
                    break
                limit = int(limit)
                if 1 <= limit <= 40:
                    break
                print("Please enter a number between 1 and 40.")
            except ValueError:
                print("Please enter a valid number.")
            except KeyboardInterrupt:
                print("Thank you")
        
        print(f"\nSearching for: {query}")
        results = search_youtube(query, limit)
        display_results(results)
        
        if results and 'videos' in results and results['videos']:
            while True:
                choice = input("\nEnter the song ID to download (or press Enter to search again): ").strip()
                
                if not choice:
                    break
                
                try:
                    choice_idx = int(choice)
                    if 0 <= choice_idx < len(results['videos']):
                        video = results['videos'][choice_idx]
                        title = video['name'].replace('/', '_').replace('\\', '_')
                        if download_mp3(video['url'], title):
                            break
                    else:
                        print("Invalid selection. Please enter a valid number.")
                except ValueError:
                    print("Please enter a valid number.")
                except KeyboardInterrupt:
                    print("Thank you")


if __name__ == "__main__":
    print("Beastbroak 's Music CLI")
    print("Enter 'quit' at any time to exit")
    main()