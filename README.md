# AI-Driven-Job-Matching-Assistant

**ResMatchAI** is an AI-powered resume-to-job description matcher that helps automate and optimize candidate-job alignment using advanced language models (Gemini 1.5 Flash via LangChain) and semantic similarity (BERT). Built with FAANG-level architecture, this tool provides accurate skill matching, gap detection, and intelligent reasoning for resume screening and talent acquisition.

---

## Features

- **Resume vs JD Comparison**  
  Extracts resume text from PDF and compares it against any job description.

- **Dual AI Scoring Engine**  
  - Gemini 1.5 Flash via LangChain for structured skill-based output  
  - BERT for semantic similarity scoring (0–100%)

- **Real-Time Analysis**  
  Built on Streamlit for seamless browser-based interaction.

- **Output Highlights**  
  - Matching Score  
  - Matched & Missing Skills  
  - Explanation for match results

- **Modular & Extensible Architecture**  
  Clean code separation (`extractor`, `bert`, `langchain`, `gemini`) ready for CI/CD and production integration.

---

##  Project Structure




---

##  Tech Stack

| Technology         | Purpose                            |
|--------------------|-------------------------------------|
| Python             | Core programming language           |
| Streamlit          | Web UI frontend                     |
| Gemini 1.5 Flash   | Advanced LLM scoring (via LangChain)|
| LangChain          | LLM prompt orchestration            |
| SentenceTransformers | BERT embeddings & similarity     |
| PyPDF2             | Resume text extraction              |
| dotenv             | Secure API key management           |

---

##  How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ResMatchAI.git
cd ResMatchAI


4. Configure API Key
Create a .env file at the root level:

ini
Copy
Edit
GEMINI_API_KEY=your_google_gemini_api_key
