import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

class LangchainGeminiMatcher:
    """
    Uses Gemini through LangChain to analyze resume and job description.
    """

    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("Gemini API key not found in environment.")

        self.llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            google_api_key=self.api_key
        )

        self.prompt = PromptTemplate(
            input_variables=["resume", "jd"],
            template="""
You are an expert job matcher AI.
Analyze the candidate resume and job description.

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

        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)

    def analyze(self, resume_text: str, jd_text: str) -> str:
        """
        Analyze the resume and JD using LangChain + Gemini.
        """
        return self.chain.run({"resume": resume_text, "jd": jd_text}).strip()
