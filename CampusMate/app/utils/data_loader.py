import pandas as pd
from app.config import FAQ_DATA_PATH

REQUIRED_COLUMNS = {"id", "category", "question", "answer"}

def load_faqs():
    if not FAQ_DATA_PATH.exists():
        raise FileNotFoundError(f"FAQ CSV not found: {FAQ_DATA_PATH}")
    df = pd.read_csv(FAQ_DATA_PATH).fillna("")
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"FAQ CSV is missing columns: {sorted(missing)}")
    return df.to_dict(orient="records")
