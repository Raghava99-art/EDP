import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
FAQ_DATA_PATH = Path(os.getenv("FAQ_DATA_PATH", PROJECT_ROOT / "data" / "college_faq.csv"))
SIMILARITY_THRESHOLD = float(os.getenv("SIMILARITY_THRESHOLD", "0.32"))
FEEDBACK_PATH = PROJECT_ROOT / "data" / "feedback.jsonl"
