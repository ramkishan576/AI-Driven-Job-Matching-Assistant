from extractor import PDFExtractor
from jd_generator import JDGenerator
from matcher_bert import BERTMatcher
from langchain_gemini import LangchainGeminiMatcher

import streamlit as st

# Initialize components
pdf_extractor = PDFExtractor()
jd_generator = JDGenerator()
bert_matcher = BERTMatcher()
gemini_matcher = LangchainGeminiMatcher()

st.set_page_config(page_title="AI Resume Matcher", layout="centered")
st.title("AI-Powered Resume to JD Matcher")

# Resume Upload
uploaded_file = st.file_uploader("Upload Resume (PDF Only)", type=["pdf"])

# JD Section
jd_mode = st.radio("Choose JD Input Method", ["Paste JD", "Generate JD using AI"])

jd_text = ""
if jd_mode == "Paste JD":
    jd_text = st.text_area("Paste Job Description")
elif jd_mode == "Generate JD using AI":
    keyword_input = st.text_input("Enter Role or Keywords")
    if st.button("Generate JD"):
        if keyword_input.strip():
            jd_text = jd_generator.generate(keyword_input)
            st.text_area("Generated JD", value=jd_text, height=300)
        else:
            st.warning("Please provide valid keywords.")

# Run Matching
if uploaded_file and jd_text:
    with st.spinner("Analyzing resume with BERT and Gemini..."):
        resume_text = pdf_extractor.extract_text(uploaded_file)

        gemini_output = gemini_matcher.analyze(resume_text, jd_text)
        bert_score = bert_matcher.calculate_score(resume_text, jd_text)

    st.success("Analysis Complete")

    st.subheader("Gemini Output (LangChain)")
    st.text(gemini_output)

    st.subheader("BERT Similarity Score")
    st.text(f"Match Score: {bert_score:.2f}%")
