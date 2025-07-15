from sentence_transformers import SentenceTransformer, util

class BERTMatcher:
    """
    A class that calculates semantic similarity between resume and job description using BERT.
    """

    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def calculate_score(self, resume_text: str, jd_text: str) -> float:
        """
        Compute similarity score between two texts.

        Returns:
            float: Percentage similarity score.
        """
        if not resume_text or not jd_text:
            return 0.0

        try:
            resume_emb = self.model.encode(resume_text, convert_to_tensor=True)
            jd_emb = self.model.encode(jd_text, convert_to_tensor=True)
            similarity = util.pytorch_cos_sim(resume_emb, jd_emb)
            score = float(similarity[0][0]) * 100
            return round(score, 2)
        except Exception as error:
            print(f"BERT Matcher Error: {error}")
            return 0.0
