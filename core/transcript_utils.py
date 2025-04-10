# core/transcript_utils.py

from youtube_transcript_api import YouTubeTranscriptApi

def get_video_id(youtube_url):
    """
    Extracts video ID from YouTube URL.
    """
    import re
    video_id_match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", youtube_url)
    return video_id_match.group(1) if video_id_match else None

def get_transcript(youtube_url):
    """
    Returns full transcript text from a YouTube video.
    """
    video_id = get_video_id(youtube_url)
    if not video_id:
        return "Invalid YouTube URL"

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        full_text = " ".join([entry["text"] for entry in transcript])
        return full_text
    except Exception as e:
        return f"Transcript fetch failed: {e}"
