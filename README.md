
# YouTube Comments Summarizer Extension

## Overview

The **YouTube Comments Summarizer** is a Chrome extension that helps users quickly understand the sentiment and content of the top comments on a YouTube video. With just a single click, the extension summarizes the top 100 comments, reducing the time spent reading through lengthy comment threads by **95%**.

This extension integrates a backend built in **Flask** with a frontend created using **HTML, CSS, and JavaScript**. The extension fetches the comments using YouTube's API, processes them, and returns a concise summary using a language model.

---

## Features

- **Summarize Top Comments**: Automatically fetches and summarizes the top 100 comments in a video.
- **Fast Processing**: Generates a summary in under 5 seconds, providing users with the essential points quickly.
- **User-Friendly Interface**: A "Summarize Comments" button is added to the comments section of YouTube for easy access.
- **Efficiency**: Reduces comment reading time by 95%.
- **Advanced Summarization**: Uses the **ChatGoogle GenerativeAI LLM** to create summaries of each chunk of comments.

---
## Workflow Diagram

The following diagram illustrates the complete workflow:

![image](https://github.com/user-attachments/assets/206c81e3-59b5-428c-a24f-69ac84660b6d)

---

## How It Works

The extension performs the following steps:

1. **Video Detection**: When a YouTube video is opened in a Chrome tab, the extension captures the video URL.
   
2. **API Call**: The video ID is extracted from the URL, and an API call is made to fetch the comment thread using the YouTube API.

3. **Chunking Comments**: The comments are divided into manageable chunks for processing. Each chunk is then passed to the **ChatGoogle GenerativeAI LLM** for summarization.

4. **Summarization**: For each chunk of comments, a summarization chain is called using the language model. These summaries are gathered into a final summary of the entire comment thread.

5. **Display Summary**: The summarized text is presented to the user in a clean, concise format, directly below the YouTube video.

---

## Installation

1. **Download the Extension**:
   Clone this repository to your local machine using:
   ```bash
   git clone https://github.com/your-repo/YouTube-Comments-Analysis-and-Summary.git
   ```

2. **Install Chrome Extension**:
   - Open Chrome and go to `chrome://extensions/`.
   - Enable "Developer Mode" by toggling the switch in the top-right corner.
   - Click on "Load unpacked" and select the Chrome Extension folder.

3. **Backend Setup**:
   - Install the necessary Python dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Run the Flask app:
     ```bash
     python server.py
     ```

4. **API Key Setup**:
setup all these things in secrets.toml file

- API_SERVICE_NAME = "youtube"
- API_VERSION = "v3"
- YOUTUBE_API_KEY=
- GEMINI_API_KEY=

6. **Run the Application**:
   Once the Flask server is running and the extension is loaded, navigate to any YouTube video and click the **Summarize Comments** button in the comments section.

---

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask (Python)
- **APIs**: YouTube Data API v3, ChatGoogle GenerativeAI
- **Language Model**: ChatGoogle GenerativeAI LLM (for summarization)

---
## Screenshots 
![image](https://github.com/user-attachments/assets/88c1032a-4e7e-4241-92f5-6f92637c22d9)


## Future Improvements

- **Increased Comment Limit**: Extend the summarization to include more than the top 100 comments.
- **Language Support**: Support summarization in multiple languages.
- **Sentiment Analysis**: Provide a sentiment score or summary of the general mood in the comment section (positive, neutral, or negative).
