import streamlit as st
from extractor import extract_resume_text, extract_name_email_experience
from ats_utils import calculate_score
from suggestions import get_improvement_suggestions
from resume_formatter import generate_pdf

def set_bg():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1498050108023-c5249f4df085");
            background-size: cover;
            background-attachment: fixed;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg()

st.markdown("""
    <style>
    .block-container {
        padding: 2rem 2rem;
        border-radius: 10px;
        background-color: rgba(255, 255, 255, 0.85);
        box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    }

    h1, h2, h3, .stTextInput label, .stTextArea label, .stSelectbox label, .stFileUploader label {
        color: #1c1c1c !important;  /* Darker heading */
        font-family: 'Segoe UI', sans-serif;
    }

    .stMarkdown p {
        color: #2c2c2c !important;
        font-size: 1rem;
    }

    .stButton button {
        background-color: #6c63ff;
        color: white;
        border-radius: 10px;
        padding: 0.5rem 1.5rem;
        font-weight: bold;
    }

    .stButton button:hover {
        background-color: #4e4ae8;
        transition: 0.3s ease-in-out;
    }

    .css-1d391kg {
        background-color: #ffffff !important;
        border-radius: 12px;
        padding: 15px;
        box-shadow: 0px 2px 10px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)


st.sidebar.title("📁 Navigation")
st.sidebar.markdown("Upload your resume, check ATS score, get suggestions.")
st.sidebar.markdown("---")
st.sidebar.markdown("🔗 [My LinkedIn](https://linkedin.com/in/yourname)")

st.set_page_config(page_title="Resume ATS Checker", layout="centered")

st.title("📄 Resume ATS Checker")
st.write("Upload your resume to check its ATS score and get suggestions!")

uploaded_file = st.file_uploader("Upload Resume (PDF or DOCX)", type=["pdf", "docx"])

if uploaded_file is not None:
    resume_text = extract_resume_text(uploaded_file)

    # ✅ Extracted text
    if resume_text.strip():
        st.subheader("🔍 Extracted Text")
        st.text_area("Resume Content", resume_text, height=250)
    else:
        st.warning("Could not extract any text from the uploaded resume.")

    # ✅ Candidate Info
    name, email, experience = extract_name_email_experience(resume_text)
    st.subheader("👤 Candidate Info")
    st.write(f"**Name:** {name}")
    st.write(f"**Email:** {email}")
    st.write(f"**Experience:** {experience}")

    # ✅ ATS Score
    score = calculate_score(resume_text)
    st.subheader("📊 ATS Score")
    st.write(f"**Score:** {score}%")
    st.progress(score / 100)

    
        
    

    # ✅ ATS Suggestions
    if score < 100:
        st.subheader("💡 Suggestions to Improve ATS-Friendliness")
        suggestions = get_improvement_suggestions(resume_text)
        for item in suggestions:
            if item["type"] == "error":
                st.markdown(f"❌ **{item['message']}**")
            elif item["type"] == "warning":
                st.markdown(f"⚠️ _{item['message']}_")
            elif item["type"] == "info":
                st.markdown(f"ℹ️ {item['message']}")
