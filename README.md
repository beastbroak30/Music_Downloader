# Music Downloader

**Music Downloader** is a Python application designed to download and manage music files from various sources.

## Features

- Search for music using an API
- Download music in MP3 format
- Organize and store downloaded files

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/beastbroak30/Music_Downloader.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd Music_Downloader
   ```
3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## API Setup

This project uses the **YT Search and Download MP3** API. Follow these steps to configure it:

1. **Sign Up on RapidAPI:**
   - Visit the [YT Search and Download MP3 API page](https://rapidapi.com/zayviusdigital/api/yt-search-and-download-mp3).
   - Click on the "Sign Up" button at the top-right corner and create a RapidAPI account.

2. **Subscribe to the API:**
   - Navigate back to the [API page](https://rapidapi.com/zayviusdigital/api/yt-search-and-download-mp3).
   - Click on the "Subscribe to Test" button.
   - Choose a suitable subscription plan (BASIC: Free to use) and subscribe.

3. **Obtain API Key and Endpoint:**
   - After subscribing, go to the "Endpoints" tab on the API page.
   - Find the base URL (endpoint) and your unique API key.

4. **Configure the `.env` File:**
   - Rename `.env.template` to `.env` if you haven’t already.
   - Open the `.env` file in a text editor.
   - Add the following lines, replacing `YOUR_API_KEY` and `API_ENDPOINT` with your actual values:
     ```env
     RAPIDAPI_KEY=YOUR_API_KEY
     API_ENDPOINT=API_ENDPOINT
     ```
   - Save and close the `.env` file.

## Usage

- **Run the application:**
  ```bash
  python main.py
  ```
- Follow the on-screen instructions to search and download music.

## Directory Structure

- `main.py`: The main script for running the downloader.
- `requirements.txt`: List of dependencies.
- `.env.template`: Template for environment variables.
- `music/`: Directory where downloaded music is stored.

## Contributing

Contributions are welcome! Follow these steps:

1. **Fork the repository.**
2. **Create a new branch:**
   ```bash
   git checkout -b feature-name
   ```
3. **Make changes and commit:**
   ```bash
   git commit -m "Added new feature"
   ```
4. **Push to your branch:**
   ```bash
   git push origin feature-name
   ```
5. **Submit a pull request.**

---
