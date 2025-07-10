# ats_checker.py

import re

def check_ats_friendly(text):
    suggestions = []

    # Check 1: Must contain email
    if not re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text):
        suggestions.append("❗ Add a valid email address near the top.")

    # Check 2: Must contain phone number
    if not re.search(r"\+?\d[\d\s\-]{8,}", text):
        suggestions.append("❗ Add a valid phone number.")

    # Check 3: Avoid tables (common in PDFs with layout elements)
    if "table" in text.lower():
        suggestions.append("⚠ Avoid using tables. ATS can't read them properly.")

    # Check 4: Use standard section headings
    headings = ['summary', 'experience', 'education', 'skills', 'projects']
    if not any(h in text.lower() for h in headings):
        suggestions.append("❗ Use standard headings like 'Experience', 'Education', 'Skills'.")

    # Check 5: Font clues (optional, we simulate this for now)
    # Could add OCR/pdf font reader later
    if "Calibri" not in text and "Arial" not in text:
        suggestions.append("ℹ Use standard fonts like Arial or Calibri.")

    # Check 6: Name at top (basic heuristic)
    lines = text.strip().split('\n')
    if len(lines) > 0 and len(lines[0].split()) < 2:
        suggestions.append("⚠ Make sure your full name is clearly written at the top.")

    return suggestions
