import streamlit as st
from comments import fetch_comments
from utils import get_summary


gemini_api_key = st.secrets['GEMINI_API_KEY']


def get_summary_from_url(url_input) :
            # Get Comments from Youtube API - INPUT
            text = fetch_comments(url_input)

            # Tokenization and Summarization  - MAIN CODE
            final_summary = get_summary(text)
            return final_summary
