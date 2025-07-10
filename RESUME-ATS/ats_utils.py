# ats_utils.py

REQUIRED_KEYWORDS = ["python", "java", "html", "css", "django", "streamlit", "sql", "machine learning"]

def calculate_score(text):
    text_lower = text.lower()
    matched = [kw for kw in REQUIRED_KEYWORDS if kw in text_lower]
    score = int((len(matched) / len(REQUIRED_KEYWORDS)) * 100)
    return score
