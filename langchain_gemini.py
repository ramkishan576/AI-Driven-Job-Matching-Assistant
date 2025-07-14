# langchain_gemini.py

import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def get_gemini_chain():
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=GEMINI_API_KEY)

    prompt = PromptTemplate(
        input_variables=["resume", "jd"],
        template="""
You are an expert job matcher AI. Analyze the candidate resume and job description.

Resume:
{resume}

Job Description:
{jd}

Return your output in this format:

---
Matching Score (0-100): <score>
Matching Skills: <comma-separated>
Missing Skills: <comma-separated>
Explanation: <1-2 lines>
---
"""
    )

    chain = LLMChain(llm=llm, prompt=prompt)
    return chain

def analyze_with_langchain(resume_text, jd_text):
    chain = get_gemini_chain()
    result = chain.run({"resume": resume_text, "jd": jd_text})
    return result.strip()