project:
  name: ResMatchAI
  description: >
    ResMatchAI is an AI-powered resume-to-job description matcher that automates candidate-job alignment using
    Gemini 1.5 Flash (via LangChain) and BERT semantic similarity. Designed with modular architecture and FAANG-level standards.

features:
  - Resume to JD comparison (PDF extraction)
  - Dual AI Scoring (Gemini via LangChain + BERT)
  - JD generation from keywords
  - Real-time Streamlit interface
  - Matching score, skill insights, and explanation

tech_stack:
  - Python
  - Streamlit
  - Google Gemini 1.5 Flash (via LangChain)
  - SentenceTransformers (BERT)
  - PyPDF2
  - dotenv

architecture:
  structure:
    - extractor.py: PDF text extraction
    - jd_generator.py: Generate JD from keywords
    - matcher_bert.py: BERT-based matching engine
    - langchain_gemini.py: LangChain + Gemini matcher
    - main.py: Streamlit frontend app
    - .env: API key
    - requirements.txt: Dependencies

usage:
  setup:
    - git clone https://github.com/your-username/ResMatchAI.git
    - cd ResMatchAI
    - python -m venv venv && source venv/bin/activate  # or venv\Scripts\activate on Windows
    - pip install -r requirements.txt
    - Create .env with: GEMINI_API_KEY=your_api_key
  run:
    - streamlit run main.py

api_limits:
  gemini_free_tier:
    limit: 15 requests per minute
    message: Use retry logic or upgrade to a paid plan

output:
  gemini:
    - Matching Score
    - Matching Skills
    - Missing Skills
    - Explanation
  bert:
    - Semantic Similarity Score (0-100%)

author:
  name: Ramkishan Rohila
  contact: ramkishannhr222@gmail.com
  github: https://github.com/ramkishan576

license: MIT
status: production-ready
