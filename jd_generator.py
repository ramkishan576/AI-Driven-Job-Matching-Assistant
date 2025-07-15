import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

class JDGenerator:
    """
    Class to generate job descriptions using Gemini.
    """

    def __init__(self):
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def generate(self, keywords: str) -> str:
        """
        Generate a job description based on input keywords.

        Args:
            keywords (str): Comma-separated skills and role input.

        Returns:
            str: A professional job description.
        """
        prompt = f"""
Act as a professional HR recruiter.
Write a formal Job Description based on the following role and keywords:

Keywords:
{keywords}

Format:
- Job Title
- Role Summary
- Key Responsibilities
- Required Skills
- Preferred Skills
- Experience
"""

        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as error:
            return f"Error generating JD: {error}"
