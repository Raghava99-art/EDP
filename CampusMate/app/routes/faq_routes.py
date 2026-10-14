from fastapi import APIRouter, Query
from app.services.search_engine import get_search_engine

router = APIRouter(tags=["FAQs"])

@router.get("/faqs")
def list_faqs(category: str | None = Query(default=None)):
    faqs = get_search_engine().faqs
    if category:
        faqs = [faq for faq in faqs if faq["category"].casefold() == category.casefold()]
    return {"count": len(faqs), "faqs": [
        {"id": str(f["id"]), "category": f["category"], "question": f["question"]}
        for f in faqs
    ]}

@router.get("/categories")
def categories():
    values = sorted({str(f["category"]) for f in get_search_engine().faqs})
    return {"categories": values}
