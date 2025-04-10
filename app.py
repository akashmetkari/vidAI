# app.py

import os
os.environ["TRANSFORMERS_NO_TF"] = "1"

import streamlit as st
from core.transcript_utils import get_transcript
from core.summarizer import generate_summary
from core.comments import fetch_comments, classify_comments
from core.qa_engine import answer_question
from core.translate import translate_text
from core.tts import generate_audio

st.set_page_config(page_title="VidAI", layout="wide")
st.title("🎬 VidAI — LLM-powered YouTube Summarizer + Q&A")

youtube_url = st.text_input("Paste a YouTube video URL:")
language = st.selectbox("Choose summary/comment language:", ["English", "Hindi"])

if youtube_url:
    with st.spinner("Fetching transcript..."):
        transcript = get_transcript(youtube_url)

    if "Transcript fetch failed" in transcript or "Invalid" in transcript:
        st.error(transcript)
    else:
        st.subheader("📝 Summary")
        summary = generate_summary(transcript, language)
        summary_translated = translate_text(summary, target_lang=language)
        st.success(summary_translated)

        if st.button("🔊 Play Summary Audio"):
            audio_file = generate_audio(summary_translated, lang=language.lower())
            if audio_file:
                st.audio(audio_file, format="audio/mp3")

        st.subheader("❓ Ask Questions About the Video")
        question = st.text_input("Ask a question:")
        if question:
            with st.spinner("Thinking..."):
                answer = answer_question(transcript, question)
            st.info(answer)

        st.subheader("💬 YouTube Comments Sentiment")
        comments = fetch_comments(video_id="dummy_id")  # Replace with actual video_id if needed
        sentiment_df = classify_comments(comments)
        st.dataframe(sentiment_df, use_container_width=True)

        st.markdown("---")
        st.caption("🚀 Built with ❤️ using HuggingFace, Streamlit, FAISS, and gTTS.")
