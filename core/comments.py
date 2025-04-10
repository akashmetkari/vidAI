# core/comments.py

import requests
import pandas as pd
from transformers import pipeline

# Load sentiment pipeline once
sentiment_pipeline = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

def fetch_comments(video_id, max_comments=20):
    """
    Dummy placeholder for comments – since YouTube API v3 requires API key.
    Replace this function with real YouTube Data API if needed.
    """
    # Simulate fake comments for now
    dummy_comments = [
        "Amazing video!", "I didn't like this one", "Very helpful explanation",
        "Too fast", "Well done", "Could be better", "Loved the visuals",
        "Sound quality is poor", "Thank you!", "Best tutorial ever"
    ] * 2  # 20 comments
    return dummy_comments[:max_comments]

def classify_comments(comments):
    """
    Applies sentiment classification on list of comments.
    Returns DataFrame with comment and sentiment label.
    """
    results = sentiment_pipeline(comments)
    labels = [res['label'] for res in results]

    return pd.DataFrame({
        "Comment": comments,
        "Sentiment": labels
    })
