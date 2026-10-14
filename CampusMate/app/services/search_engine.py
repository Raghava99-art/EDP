from functools import lru_cache
import numpy as np
from sentence_transformers import SentenceTransformer
from app.utils.data_loader import load_faqs
from app.utils.text_cleaner import clean_text

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

class FAQSearchEngine:
    def __init__(self):
        self.faqs = load_faqs()
        self.model = SentenceTransformer(MODEL_NAME)
        self.texts = [
            f"Question: {row['question']} Category: {row['category']} Answer: {row['answer']}"
            for row in self.faqs
        ]
        self.embeddings = self.model.encode(self.texts, normalize_embeddings=True)

    def search(self, question: str, category=None, top_k=3):
        question = clean_text(question)
        if not question:
            return []
        query_embedding = self.model.encode([question], normalize_embeddings=True)[0]
        scores = np.dot(self.embeddings, query_embedding)
        candidates = []
        for index, score in enumerate(scores):
            faq = self.faqs[index]
            if category and faq["category"].casefold() != category.casefold():
                continue
            candidates.append({
                "id": str(faq["id"]),
                "category": faq["category"],
                "question": faq["question"],
                "answer": faq["answer"],
                "similarity": round(float(score), 4),
            })
        return sorted(candidates, key=lambda item: item["similarity"], reverse=True)[:top_k]

@lru_cache(maxsize=1)
def get_search_engine():
    return FAQSearchEngine()
