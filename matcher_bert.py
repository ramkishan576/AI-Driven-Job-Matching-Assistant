# app/matcher_bert.py

from sentence_transformers import SentenceTransformer, util
import torch


# Load BERT model globally

_model = SentenceTransformer('all-MiniLM-L6-v2')


def bert_match_score(resume_text: str, jd_text: str) -> float:
    """
    Calculates semantic similarity score between a resume and job description using BERT embeddings.

    Args:
        resume_text (str): Extracted text from resume.
        jd_text (str): Raw job description text.

    Returns:
        float: Similarity score (0.0 - 100.0)
    """
    if not resume_text or not jd_text:
        return 0.0

    try:
        # Encode texts to embeddings
        resume_embedding = _model.encode(resume_text, convert_to_tensor=True)
        jd_embedding = _model.encode(jd_text, convert_to_tensor=True)

        # Compute cosine similarity
        similarity = util.pytorch_cos_sim(resume_embedding, jd_embedding)

        # Extract and convert score
        score = float(similarity[0][0]) * 100
        return round(score, 2)

    except Exception as e:
        print(f"[BERT Matching Error]: {e}")
        return 0.0
