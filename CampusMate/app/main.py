from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.chat_routes import router as chat_router
from app.routes.faq_routes import router as faq_router
from app.routes.feedback_routes import router as feedback_router

app = FastAPI(title="CampusGuide AI", version="1.0.0",
              description="Semantic FAQ retrieval API for college information.")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router, prefix="/api")
app.include_router(faq_router, prefix="/api")
app.include_router(feedback_router, prefix="/api")

@app.get("/")
def root():
    return {"name": "CampusGuide AI", "docs": "/docs"}

@app.get("/api/health")
def health():
    return {"status": "ok", "service": "CampusGuide AI"}
