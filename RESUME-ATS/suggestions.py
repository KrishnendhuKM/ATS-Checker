def get_improvement_suggestions(text):
    suggestions = []

    if "Objective" not in text:
        suggestions.append({
            "type": "error",
            "message": "Add an 'Objective' section to explain your career goal."
        })

    if "Experience" not in text and "Internship" not in text:
        suggestions.append({
            "type": "warning",
            "message": "Add work experience or internship section if available."
        })

    if "LinkedIn" not in text and "linkedin.com" not in text:
        suggestions.append({
            "type": "info",
            "message": "Add a LinkedIn profile link to enhance your credibility."
        })

    if "Skills" not in text:
        suggestions.append({
            "type": "error",
            "message": "Include a 'Skills' section with technical and soft skills."
        })

    if text.count("•") == 0 and "-" not in text:
        suggestions.append({
            "type": "warning",
            "message": "Use bullet points (• or -) to make content easier to read."
        })

    return suggestions
# suggestions.py

import re

def get_improvement_suggestions(text):
    suggestions = []

    # Check for name (very basic check)
    if not re.search(r"\bname\b|\bName\b", text):
        suggestions.append({"type": "error", "message": "Name not clearly mentioned."})

    # Check for email
    if not re.search(r"\b[\w.-]+?@\w+?\.\w+?\b", text):
        suggestions.append({"type": "error", "message": "Email is missing or invalid."})

    # Check for experience
    if not re.search(r"\b\d+\+?\s*(years|yrs)\b", text.lower()):
        suggestions.append({"type": "warning", "message": "No clear work experience mentioned."})

    # Check for LinkedIn
    if "linkedin.com" not in text.lower():
        suggestions.append({"type": "info", "message": "Consider adding a LinkedIn profile link."})

    # Suggest PDF if not
    if ".doc" in text.lower():
        suggestions.append({"type": "info", "message": "Use PDF format for better compatibility."})

    if len(suggestions) == 0:
        suggestions.append({"type": "info", "message": "Your resume looks good!"})

    return suggestions
