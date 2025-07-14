# app/matcher_gemini.py
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_resume_with_jd(resume_text, jd_text):
    prompt = f"""
You are an expert recruitment AI assistant. 
Compare the following Resume with the Job Description and return structured output in this format:

---
Matching Score (0-100): <score>
Matching Skills: <comma-separated>
Missing Skills: <comma-separated>
Explanation: <1-2 lines>
---

Resume:
{resume_text}

Job Description:
{jd_text}
"""
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f" Gemini Error: {e}"