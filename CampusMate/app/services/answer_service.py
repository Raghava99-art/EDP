from app.config import SIMILARITY_THRESHOLD
from app.services.search_engine import get_search_engine

def answer_question(question: str, category=None):
    results = get_search_engine().search(question, category=category, top_k=3)
    if not results:
        return {
            "answer": "I couldn't find a matching FAQ. Try another category or contact your college office.",
            "matched": False, "results": []
        }
    best = results[0]
    if best["similarity"] < SIMILARITY_THRESHOLD:
        return {
            "answer": "I'm not confident enough to answer that from the current FAQ list. Please rephrase your question or contact the relevant college office.",
            "matched": False, "results": results
        }
    return {"answer": best["answer"], "matched": True, "results": results}
