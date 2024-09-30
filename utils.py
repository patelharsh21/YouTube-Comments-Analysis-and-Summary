import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_text_splitters import TokenTextSplitter
from langchain.chains.summarize import load_summarize_chain
from dotenv import load_dotenv
from googleapiclient.discovery import build
from pytube import extract

api_server_name = st.secrets["API_SERVICE_NAME"]
api_version = st.secrets['API_VERSION']
youtube_api_key = st.secrets['YOUTUBE_API_KEY']
gemini_api_key = st.secrets['GEMINI_API_KEY']

def start_youtube_service():
     return build(api_server_name, api_version, developerKey=youtube_api_key)

def extract_video_id_from_link(url):
    return extract.video_id(url)

def get_comments_thread(youtube, video_id, next_page_token):
    results = youtube.commentThreads().list(
        part="snippet,replies",                     
        videoId=video_id,
        textFormat='plainText',
        maxResults=100,
        # pageToken = next_page_token
    ).execute()
    return results

def load_comments_in_format(comments):
    all_comments = []
    all_comments_string = ""
    for thread in comments["items"]:
        comment = {}
        comment['content'] = thread['snippet']['topLevelComment']['snippet']['textOriginal']
        all_comments_string = all_comments_string + comment['content']+"\n"
        replies = []
        if 'replies' in thread:
            for reply in thread['replies']['comments']:
                reply_text = reply['snippet']['textOriginal']
                all_comments_string = all_comments_string + reply_text+"\n"
                replies.append(reply_text)
            comment['replies'] = replies
        
        all_comments.append(comment)
    return all_comments_string

def fetch_comments(url):
    youtube = start_youtube_service()
    video_id = extract_video_id_from_link(url)
    next_page_token = ''
   
    data = get_comments_thread(youtube, video_id, next_page_token)
    all_comments = load_comments_in_format(data)
    return all_comments

def get_summary(text):

    #Tokenization
    text_splitter = TokenTextSplitter(
        chunk_size=1000, 
        chunk_overlap=10
    )
    chunks = text_splitter.create_documents([text])

    #Summarization
    llm = ChatGoogleGenerativeAI(
        model="gemini-pro",
        google_api_key=gemini_api_key
        
    )
    
    chain = load_summarize_chain(
        llm, 
        chain_type="map_reduce"
    )

    #Invoke Chain
    response=chain.run(chunks)

    return response

def get_summary_from_url(url_input) :
            # Get Comments from Youtube API - INPUT
            text = fetch_comments(url_input)

            # Tokenization and Summarization  - MAIN CODE
            final_summary = get_summary(text)
            return final_summary
