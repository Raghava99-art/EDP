import re

def clean_text(text: str) -> str:
    """Normalize whitespace and remove control characters from user text."""
    text = re.sub(r"[\x00-\x1f\x7f]", " ", str(text or ""))
    return re.sub(r"\s+", " ", text).strip()
