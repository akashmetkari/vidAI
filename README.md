


# VidAI 🎥📄🧠

**VidAI** is an AI-powered web app that allows users to **summarize**, **analyze sentiment of comments**, and **ask questions** about any YouTube video. It leverages **free**, high-performance **open-source models** to offer a powerful yet cost-effective GenAI experience — no OpenAI API required!


## 🌟 Features

- 🔍 **YouTube Video Summarization** using `facebook/bart-base`
- 💬 **YouTube Comment Sentiment Analysis** using multilingual BERT
- 🤖 **Question-Answering (RAG)** on video transcripts using Sentence Transformers + FAISS
- 🧠 **Streamlit-based Web UI** for a clean and interactive experience
- 🔓 **No paid APIs** – Fully open-source and local inference



## 🛠 Tech Stack

| Area            | Technology Used                                      |
|-----------------|------------------------------------------------------|
| **NLP Models**  | BART, BERT, Sentence Transformers (`all-MiniLM`)     |
| **Embeddings**  | FAISS for vector search                              |
| **Frontend**    | Streamlit                                            |
| **Data Source** | `youtube-transcript-api`, `yt-dlp`, `requests`       |
| **TTS (Optional)** | `pyttsx3` or any other TTS lib (optional)         |



## 📦 Installation

```bash
git clone https://github.com/akashmetkari/VidAI.git
cd VidAI
pip install -r requirements.txt
```

> ✅ Make sure to activate your virtual environment if you're using one.

---

## ▶️ Running the App

```bash
streamlit run app.py
```

Then open your browser and go to:  
**http://localhost:8501**

---

## 📁 Project Structure

```
VidAI/
├── app.py                    # Main Streamlit app
├── requirements.txt          # Python dependencies
├── README.md                 # Project description
└── core/
    ├── summarizer.py         # Summarization using BART
    ├── comments.py           # Fetch + analyze YouTube comments
    ├── qa_engine.py          # RAG-based question-answering
    ├── transcript_utils.py   # YouTube transcript extraction
    └── tts.py                # Optional Text-to-Speech
```

---

## 🧪 Example Workflow

1. 🔗 Paste a YouTube video URL
2. 📃 View its transcript summary
3. 💬 Analyze top comments (positive/negative/neutral)
4. ❓ Ask follow-up questions based on video content

---

## 💡 Future Plans

- 🌐 Add multilingual support for summary and Q&A
- 🧑‍💻 Avatar video narration using GenAI
- 📁 PDF or video file upload support
- 🗣️ Voice-based Q&A interface
- 📊 Visualization of sentiment trends

---

## 🙌 Acknowledgements

- 🤗 Hugging Face Transformers & Datasets
- 🎈 Streamlit for rapid UI prototyping
- 🎥 YouTube Transcript API & yt-dlp

---

## 👨‍💻 Author

**Akash Metkari**  
📧 [ametkari13042004@gmail.com](mailto:ametkari13042004@gmail.com)  
🔗 [LinkedIn: akashmetkari](https://www.linkedin.com/in/akash-metkari-24654rt3)  
🌐 [GitHub: akashmetkari](https://github.com/akashmetkari)

---

> ⭐ Star this repo if you like it. Contributions are welcome!

