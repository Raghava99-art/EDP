from pydantic import BaseModel, Field
from typing import Optional

class ChatRequest(BaseModel):
    question: str = Field(min_length=2, max_length=500)
    category: Optional[str] = None

class FeedbackRequest(BaseModel):
    question: str = Field(min_length=1, max_length=500)
    faq_id: str = Field(min_length=1, max_length=100)
    helpful: bool
    comment: Optional[str] = Field(default=None, max_length=500)
