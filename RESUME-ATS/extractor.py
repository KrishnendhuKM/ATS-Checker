import re
from pdfminer.high_level import extract_text as extract_pdf_text
from docx import Document

def extract_resume_text(uploaded_file):
    if uploaded_file.name.endswith(".pdf"):
        return extract_pdf_text(uploaded_file)
    elif uploaded_file.name.endswith(".docx"):
        doc = Document(uploaded_file)
        return "\n".join([para.text for para in doc.paragraphs])
    else:
        return ""

def extract_name_email_experience(text):
    # Extract email
    email_match = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    email = email_match.group(0) if email_match else "Not found"

    # Extract name (very basic: use first 2 words if they are capitalized at the beginning)
    lines = text.strip().split("\n")
    name = "Not found"
    for line in lines:
        words = line.strip().split()
        if len(words) >= 2 and words[0][0].isupper() and words[1][0].isupper():
            name = words[0] + " " + words[1]
            break

    # Extract experience in years (look for patterns like "X years" or "X+ years")
    exp_match = re.search(r'(\d+)\+?\s+years?', text, re.IGNORECASE)
    experience = exp_match.group(0) if exp_match else "Not found"

    return name, email, experience
