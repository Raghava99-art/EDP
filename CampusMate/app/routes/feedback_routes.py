from fastapi import APIRouter
from app.models.faq_model import FeedbackRequest
from app.services.analytics_service import record_feedback, feedback_summary

router = APIRouter(tags=["Feedback"])

@router.post("/feedback")
def feedback(request: FeedbackRequest):
    record_feedback(request.model_dump())
    return {"saved": True, "message": "Thank you for your feedback."}

@router.get("/feedback/summary")
def summary():
    return feedback_summary()
