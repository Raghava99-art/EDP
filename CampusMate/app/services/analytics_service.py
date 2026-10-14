from collections import Counter
import json
from app.config import FEEDBACK_PATH

def record_feedback(payload: dict):
    FEEDBACK_PATH.parent.mkdir(parents=True, exist_ok=True)
    with FEEDBACK_PATH.open("a", encoding="utf-8") as file:
        file.write(json.dumps(payload, ensure_ascii=False) + "\n")

def feedback_summary():
    if not FEEDBACK_PATH.exists():
        return {"total": 0, "helpful": 0, "unhelpful": 0}
    records = []
    with FEEDBACK_PATH.open(encoding="utf-8") as file:
        for line in file:
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    counts = Counter(str(item.get("helpful", False)).lower() for item in records)
    return {"total": len(records), "helpful": counts["true"], "unhelpful": counts["false"]}
