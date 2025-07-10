# processor.py

import nltk
import string

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download once if not already done
nltk.download('punkt')
nltk.download('stopwords')

def clean_and_tokenize(text):
    # Lowercase the text
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Tokenize
    tokens = word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered = [word for word in tokens if word not in stop_words]
    return filtered

def load_skills():
    with open("skills.txt", "r") as file:
        return [line.strip().lower() for line in file.readlines()]

def match_skills(tokens, skills):
    return list(set(tokens).intersection(skills))
