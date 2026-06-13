# 🤖 RAG Teaching Assistant

> An intelligent AI-powered teaching assistant that answers questions based on video course content using Retrieval-Augmented Generation (RAG) technology.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-3.0-green)
![Groq](https://img.shields.io/badge/Groq-LLama3-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📌 About The Project

This project transforms video course content into an intelligent Q&A system. Upload your course videos, and the AI assistant will answer any questions based on the video content — just like having a personal tutor available 24/7!

### 🎯 Problem It Solves
- Students struggle to find specific information in long course videos
- Rewatching hours of content just to find one answer is time-consuming
- This assistant gives instant, context-aware answers from video content

---

## ✨ Features

- 🎥 **Video to Text** — Automatically transcribes course videos using OpenAI Whisper
- 🧠 **Smart Search** — Finds the most relevant content using Semantic Search
- 💬 **AI Answers** — Generates context-aware answers using Groq LLM (Llama 3.1)
- 🌐 **Clean UI** — Beautiful dark-themed web interface
- 🔤 **Multilingual** — Supports English and Hinglish responses
- ⚡ **Fast** — Instant responses powered by Groq's ultra-fast inference

---

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|---|---|---|
| Audio Transcription | OpenAI Whisper | Convert video/audio to text |
| Text Embeddings | Sentence-Transformers | Convert text to vectors |
| Vector Search | Scikit-learn | Find similar content |
| LLM | Groq API (Llama 3.1) | Generate answers |
| Backend | Flask | Web server |
| Data Processing | Pandas + NumPy | Handle data |
| Storage | Joblib | Save/load embeddings |
| Frontend | HTML + CSS + JavaScript | User interface |

---

## 🔄 How It Works
📹 Video File

↓

🎵 Convert to MP3 (MoviePy)

↓

📝 Transcribe to Text (OpenAI Whisper)

↓

✂️ Split into Chunks (Python)

↓

🔢 Generate Embeddings (Sentence-Transformers)

↓

💾 Save to CSV + Joblib

━━━━━━ When User Asks a Question ━━━━━━
❓ User Question

↓

🔢 Convert Question to Embedding

↓

🔍 Find Top 5 Similar Chunks (Cosine Similarity)

↓

🤖 Send Context + Question to Groq LLM

↓

✅ Get Accurate Answer

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.12+
- FFmpeg installed
- Groq API Key (free at console.groq.com)

### Step 1 — Clone Repository
```bash
git clone https://github.com/lovegupta1/rag-teaching-assistant.git
cd rag-teaching-assistant
```

### Step 2 — Install Dependencies
```bash
pip install flask openai-whisper moviepy sentence-transformers pandas scikit-learn joblib groq streamlit
```

### Step 3 — Add API Key
Create a `config.py` file:
```python
GROQ_API_KEY = "your_groq_api_key_here"
```
Get your free API key at: https://console.groq.com

### Step 4 — Add Your Videos
Place your MP4 video files in the `videos/` folder

### Step 5 — Process Videos
```bash
# Step 1: Convert videos to audio
python step1_video_to_audio.py

# Step 2: Transcribe audio to text
python step2_transcribe.py

# Step 3: Create text chunks
python step3_chunking.py

# Step 4: Generate embeddings
python step4_embeddings.py
```

### Step 6 — Run The App
```bash
python app.py
```

Open your browser and go to: `http://127.0.0.1:5000`

---

## 🖥️ Screenshots

> Chat interface with dark theme and real-time AI responses

---

## 🧠 RAG Architecture

**RAG (Retrieval-Augmented Generation)** combines:
1. **Retrieval** — Finding relevant information from the knowledge base
2. **Augmentation** — Adding that context to the prompt
3. **Generation** — LLM generates accurate answers based on context

This ensures answers are always grounded in your course content!

---

## 🚀 Future Improvements

- [ ] Support for PDF documents
- [ ] Multiple video upload support
- [ ] User authentication
- [ ] Chat history export
- [ ] Deploy on cloud platform

---

## 👨‍💻 Author

**Love Gupta**
- 🎓 B.Tech CSE — GLA University
- 💼 GitHub: [@lovegupta1](https://github.com/lovegupta1)
- 🔗 LinkedIn: [Love Gupta](https://linkedin.com/in/love-gupta-85b08b269)

---

## 📄 License

This project is licensed under the MIT License.

---

⭐ If you found this project helpful, please give it a star!
