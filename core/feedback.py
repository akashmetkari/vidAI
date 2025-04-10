# core/feedback.py

import csv
import os
from datetime import datetime

FEEDBACK_FILE = "feedback_data.csv"

def store_feedback(video_url, rating, comment):
    """Store feedback (thumbs + comment) in a CSV file"""
    file_exists = os.path.isfile(FEEDBACK_FILE)

    with open(FEEDBACK_FILE, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["timestamp", "video_url", "rating", "comment"])
        writer.writerow([
            datetime.now().isoformat(),
            video_url,
            rating,
            comment.strip() if comment else ""
        ])