# 🎓 Campus Knowledge Chatbot

An AI-powered campus assistant built using **Retrieval-Augmented Generation (RAG)** that answers student and campus-related queries using semantic search and LLMs.

---

# 🚀 Live Demo

## 🌐 Backend API

```bash
https://budget-aware-campus-knowledge-agent-1.onrender.com
```

## 📘 API Documentation

```bash
https://budget-aware-campus-knowledge-agent-1.onrender.com/docs
```

---

# ✨ Features

✅ AI-powered campus assistant
✅ Retrieval-Augmented Generation (RAG)
✅ Semantic similarity search using embeddings
✅ FastAPI backend API
✅ Beautiful responsive frontend UI
✅ Mobile + Tablet + Desktop responsive design
✅ Dark / Light mode support
✅ Source + page citation support
✅ Chat history sidebar
✅ Stop generation button
✅ PostgreSQL + pgvector support
✅ OpenRouter LLM integration

---

# 🛠️ Tech Stack

## Backend

* Python
* FastAPI
* SQLAlchemy
* PostgreSQL
* pgvector
* Sentence Transformers
* OpenRouter API

## Frontend

* HTML
* CSS
* JavaScript

## AI / NLP

* RAG (Retrieval-Augmented Generation)
* all-MiniLM-L6-v2 Embedding Model
* Llama 3 (via OpenRouter)

---

# 📂 Project Structure

```bash
CampusChatbot/
│
├── api/
│   └── server.py
│
├── backend/
│   ├── ingestion/
│   │   ├── chunk_data.py
│   │   ├── embed_store.py
│   │   └── load_data.py
│   │
│   ├── retrieval/
│   │   ├── qa_system.py
│   │   └── search.py
│   │
│   └── embeddings/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── data/
│
├── requirements.txt
├── README.md
└── .env
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Peesala-Naveen/Budget-Aware-Campus-Knowledge-Agent.git
```

```bash
cd Budget-Aware-Campus-Knowledge-Agent
```

---

# 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the root folder.

```env
OPENROUTER_API_KEY=your_api_key
DATABASE_URL=your_postgresql_url
```

⚠️ Never upload `.env` to GitHub.

---

# 🧠 Generate Embeddings

```bash
python -m backend.ingestion.embed_store
```

This will:

* Load PDF/text data
* Chunk documents
* Generate embeddings
* Store embeddings in PostgreSQL

---

# ▶️ Run FastAPI Server

```bash
uvicorn api.server:app --reload
```

Server runs at:

```bash
http://127.0.0.1:8000
```

---

# 🌐 Open Frontend

Open directly in browser:

```bash
frontend/index.html
```

OR visit:

```bash
http://127.0.0.1:8000
```

---

# 📘 API Endpoint

## POST `/ask`

### Request

```json
{
  "question": "What is Kuruksastra?"
}
```

### Response

```json
{
  "answer": "Kuruksastra is the cultural fest of SASTRA University.",
  "sources": [
    {
      "source": "source.pdf",
      "page": 5
    }
  ]
}
```

---

# 🎨 UI Features

* Responsive chatbot UI
* Mobile sidebar menu
* Smooth scrolling
* Loading animations
* Dark / Light mode
* Chat history
* Source display
* Modern gradient design

---

# 📱 Responsive Support

✅ Android Phones
✅ iPhones
✅ Tablets
✅ Laptops
✅ Desktop Monitors

---

# ☁️ Deployment

## Backend Deployment

Deployed on:

```bash
Render
```

## Database

Hosted on:

```bash
Supabase PostgreSQL + pgvector
```

---

# 🔥 Future Improvements

* Voice assistant support
* Streaming responses
* Authentication system
* Admin dashboard
* File uploads
* Multi-campus support
* Fine-tuned campus LLM

---

# 👨‍💻 Author

## Peesala Naveen

* 🎓 SASTRA University
* 💻 AI & Full Stack Developer
* 🌐 Web Development + Generative AI

### GitHub

```bash
https://github.com/Peesala-Naveen
```

### LinkedIn

```bash
https://linkedin.com/in/naveen-peesala-b41019301
```

---

# ⭐ If You Like This Project

Give this repository a ⭐ on GitHub.
