from fastapi import APIRouter, HTTPException
from app.models.faq_model import ChatRequest
from app.services.answer_service import answer_question
from app.utils.text_cleaner import clean_text

router = APIRouter(tags=["Chat"])

@router.post("/chat")
def chat(request: ChatRequest):
    question = clean_text(request.question)
    if len(question) < 2:
        raise HTTPException(status_code=422, detail="Please enter a longer question.")
    return answer_question(question, category=request.category)
