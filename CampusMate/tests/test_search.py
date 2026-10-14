from app.utils.text_cleaner import clean_text

def test_clean_text_collapses_whitespace():
    assert clean_text("  exam   time table  ") == "exam time table"

def test_clean_text_handles_empty_value():
    assert clean_text("") == ""
