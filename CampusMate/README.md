# CampusMate  — Smart Student Helpdesk

A college FAQ chatbot using sentence embeddings and cosine similarity. It includes a FastAPI backend, a React/Vite frontend, sample FAQ data, feedback storage, and search evaluation scripts.

> The included FAQs are demonstration data. Replace them with verified information from your college before real use.

## Features
- Natural-language semantic FAQ search
- Ranked answers with similarity scores
- Low-confidence fallback instead of pretending to know
- Category filtering
- Helpful/unhelpful feedback endpoint
- CSV-based FAQ data
- Basic tests and a search evaluation script

## Requirements
- Python 3.10+
- Node.js 18+ and npm

## 1. Run the backend (Windows PowerShell)
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Backend API: http://127.0.0.1:8000  
Interactive API docs: http://127.0.0.1:8000/docs

The first run downloads the sentence-transformer model `all-MiniLM-L6-v2`. Internet access is required for this first download.

## 2. Run the frontend
Open a second terminal:
```powershell
cd frontend
npm install
npm run dev
```
Open the local URL shown by Vite, usually http://localhost:5173.

## 3. Run tests
From the project root:
```powershell
pytest
```

## 4. Evaluate example queries
```powershell
python scripts/evaluate_search.py
```

## API
- `GET /api/health` — health status
- `GET /api/faqs?category=Admissions` — list FAQs
- `POST /api/chat` — retrieve an answer
- `POST /api/feedback` — record answer feedback

Example request:
```json
{"question":"How do I apply for a scholarship?","category":null}
```

## Folder guide
- `app/services/search_engine.py`: embedding-based retrieval
- `app/services/answer_service.py`: answer and confidence fallback
- `app/routes/`: API endpoints
- `data/college_faq.csv`: demonstration knowledge base
- `tests/`: automated tests
- `frontend/src/`: React UI

## Important
This is a learning project, not an official college service. Do not upload private student information. Similarity scores are retrieval signals, not guaranteed probabilities of correctness.
