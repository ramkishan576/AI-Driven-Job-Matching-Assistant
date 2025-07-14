import streamlit as st
from extractor import extract_text_from_pdf
from matcher_bert import bert_match_score
from langchain_gemini import analyze_with_langchain

st.set_page_config(page_title="AI Resume Matcher", layout="centered")
st.title("AI-Powered Resume to JD Matcher")

uploaded_file = st.file_uploader("Upload Resume (PDF Only)", type=["pdf"])
jd_text = st.text_area("Paste Job Description Below")

if uploaded_file and jd_text:
    with st.spinner("Analyzing Resume with Gemini (LangChain) and BERT..."):
        resume_text = extract_text_from_pdf(uploaded_file)

        # Gemini via LangChain
        gemini_result = analyze_with_langchain(resume_text, jd_text)

        # BERT score
        bert_score = bert_match_score(resume_text, jd_text)

    st.success("Analysis Complete")

    st.subheader("Gemini (LangChain) Output")
    st.markdown(gemini_result)

    st.subheader("BERT-Based Similarity Score")
    st.info(f"BERT Match Score: {bert_score:.2f}%")
    st.progress(int(bert_score) if bert_score <= 100 else 100)

st.markdown("---")
st.caption("Built using Gemini 1.5 Flash and BERT with LangChain integration.")
