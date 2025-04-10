# core/tts.py

from gtts import gTTS
import os

def generate_audio(text, lang="en", filename="summary_audio.mp3"):
    """
    Converts text to speech and saves as MP3.
    """
    lang_code = "hi" if lang.lower() == "hindi" else "en"
    try:
        tts = gTTS(text, lang=lang_code)
        tts.save(filename)
        return filename
    except Exception as e:
        print(f"TTS Error: {e}")
        return None
