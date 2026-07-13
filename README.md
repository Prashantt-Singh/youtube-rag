# 🌍 Multilingual YouTube RAG Assistant

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-00A67E?style=for-the-badge)
![Groq](https://img.shields.io/badge/Groq-LLM-black?style=for-the-badge)
![FAISS](https://img.shields.io/badge/FAISS-VectorDB-purple?style=for-the-badge)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

**Multilingual YouTube RAG Assistant** is an AI-powered **Retrieval-Augmented Generation (RAG)** application that allows users to paste a YouTube video URL, automatically process its transcript, and ask natural language questions about the video's content.

The application supports **both English and Hindi transcripts** using multilingual embeddings. It performs semantic search over the transcript to retrieve the most relevant sections and generates context-aware answers in English using Groq's **Llama 3.3-70B** Large Language Model. The application also displays the timestamp of the retrieved content for easy navigation.

---

# 🚀 Features

- 🎥 Process any YouTube video using its URL
- 🌐 Supports English and Hindi transcripts
- 📄 Automatic Transcript Processing
- 🤖 AI-powered Question Answering
- 📚 Retrieval-Augmented Generation (RAG)
- 🔍 Semantic Search using Multilingual Embeddings
- ⚡ FAISS Vector Search for Fast Retrieval
- 🧠 Groq Llama-3.3-70B-Versatile
- 📍 Displays the timestamp of the retrieved content
- 💬 Interactive Streamlit Interface
- 🐳 Docker Support

---

# 🏗️ Project Structure

```text
RAG_YOUTUBE/
│
├── app.py
├── Dockerfile
├── requirements.txt
├── README.md
│
├── RAG/
│   ├── rag.py
│   ├── transcript.py
│   ├── embedding.py
│   ├── vector_store.py
│   ├── llm.py
│   ├── prompt.py
│   └── utils.py
│
├── Data/
├── Vectorstore/
└── .streamlit/
```

---

# ⚙️ Tech Stack

| Category | Technology |
|----------|------------|
| Frontend | Streamlit |
| Language | Python |
| AI Framework | LangChain |
| LLM | Groq (Llama-3.3-70B-Versatile) |
| Embeddings | HuggingFace Sentence Transformers |
| Embedding Model | sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 |
| Vector Database | FAISS |
| Transcript Extraction | youtube-transcript-api |
| Environment Variables | python-dotenv |
| Containerization | Docker |

---

# 🏗️ System Architecture

```text
               YouTube URL
                    │
                    ▼
          Extract Video ID
                    │
                    ▼
        Fetch Video Transcript
                    │
                    ▼
       Create LangChain Documents
                    │
                    ▼
     Recursive Character Chunking
                    │
                    ▼
      Generate Multilingual Embeddings
                    │
                    ▼
        Store Embeddings in FAISS
──────────────────────────────────────────────
           User asks Question
                    │
                    ▼
         Generate Query Embedding
                    │
                    ▼
        FAISS Similarity Search
                    │
                    ▼
      Retrieve Relevant Chunks
                    │
                    ▼
          Build Context Prompt
                    │
                    ▼
      Groq Llama-3.3-70B LLM
                    │
                    ▼
        Generate English Answer
                    │
                    ▼
      Return Answer + Timestamp
```

---

# 📂 Modules

## `app.py`

Main Streamlit application.

Responsible for:

- User Interface
- YouTube URL Input
- Question Input
- Displaying Answers
- Displaying Timestamps

---

## `utils.py`

Utility functions.

Responsible for:

- Extracting the YouTube Video ID from the URL

---

## `transcript.py`

Fetches transcripts using **youtube-transcript-api**.

Features:

- English Transcript Support
- Hindi Transcript Support
- Transcript Error Handling

---

## `embedding.py`

Loads the multilingual Hugging Face embedding model.

Embedding Model:

```text
sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
```

---

## `vector_store.py`

Responsible for:

- Creating LangChain Documents
- Transcript Chunking
- Embedding Generation
- FAISS Vector Store
- Similarity Search

---

## `llm.py`

Loads the Groq Large Language Model.

Model Used:

```text
llama-3.3-70b-versatile
```

---

## `prompt.py`

Contains the RAG prompt template.

Ensures:

- Answers are generated only from retrieved context
- Responses are in English
- Prevents hallucinations when context is unavailable

---

## `rag.py`

Main RAG pipeline.

Responsible for:

- Transcript Processing
- Document Chunking
- Embedding Generation
- FAISS Index Creation
- Similarity Retrieval
- LLM Response Generation
- Timestamp Extraction

---

# 💡 Example Workflow

1. Paste a YouTube video URL.
2. Click **Process Video**.
3. Ask a question in natural language.
4. The application retrieves the most relevant transcript chunks.
5. Groq LLM generates an answer using the retrieved context.
6. The relevant timestamp is displayed along with the answer.

---

# ▶️ Installation

## Clone the Repository

```bash
git clone https://github.com/Prashantt-Singh/youtube-rag.git
```

## Navigate to the Project

```bash
cd youtube-rag
```

## Create a Virtual Environment

```bash
python -m venv .venv
```

### Activate the Environment

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Create a `.env` File

Create a `.env` file in the project root.

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

---

# 🐳 Docker

Run the application inside a Docker container without installing Python or the project dependencies locally.

## Build the Docker Image

```bash
docker build -t youtube-rag .
```

## Run the Docker Container

```bash
docker run --rm --env-file .env -p 8501:8501 youtube-rag
```

Once the container starts successfully, open:

```text
http://localhost:8501
```

---

# ▶️ Run the Project

```bash
streamlit run app.py
```

---

# 📈 Future Improvements

- 🔗 Clickable YouTube Timestamp Links
- 💬 Chat History
- 📺 Multiple Video Support
- ⚡ Transcript Caching
- ☁️ Cloud Deployment
- 🎨 Improved UI
- 🌍 More Language Support
- 📱 Mobile Responsive Interface
- 🔄 Hybrid Search (BM25 + FAISS)

---

# 📚 RAG Workflow

```text
YouTube URL
      │
      ▼
Transcript
      │
      ▼
Documents
      │
      ▼
Chunking
      │
      ▼
Embeddings
      │
      ▼
FAISS
      │
      ▼
User Query
      │
      ▼
FAISS Similarity Search
      │
      ▼
Relevant Chunks
      │
      ▼
Prompt
      │
      ▼
Groq LLM
      │
      ▼
Answer + Timestamp
```

---

# 🤝 Contributing

Contributions, suggestions, and feature requests are welcome.

Feel free to fork this repository and submit a pull request.

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

## Prashant Singh

**B.Tech Computer Science & Information Technology (CSIT)**

- 💻 GitHub: https://github.com/Prashantt-Singh
- 🌐 LinkedIn: https://www.linkedin.com/in/prashant-singh-97aaa6328/

---

⭐ **If you found this project helpful, consider giving it a star on GitHub. Your support is appreciated!**