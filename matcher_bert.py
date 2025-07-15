from sentence_transformers import SentenceTransformer, util

class BERTMatcher:
    def __init__(self):
        # Model ko CPU par forcefully load kar rahe hain to avoid meta tensor error
        self.model = SentenceTransformer('all-MiniLM-L6-v2', device='cpu')

    def calculate_score(self, resume_text, jd_text):
        if not resume_text or not jd_text:
            return 0.0

        resume_embedding = self.model.encode(resume_text, convert_to_tensor=True)
        jd_embedding = self.model.encode(jd_text, convert_to_tensor=True)

        similarity = util.pytorch_cos_sim(resume_embedding, jd_embedding)
        score = float(similarity[0][0]) * 100
        return round(score, 2)
