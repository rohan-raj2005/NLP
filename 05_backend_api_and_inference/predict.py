"""
predict.py - Standalone Inference & Recommendation Engine
Loads saved model artifacts, preprocesses text input, calculates calibrated probabilities,
assigns stress indices, and generates supportive intervention recommendations.
"""

import os
import sys
import json
import joblib
import numpy as np

# Add preprocessing module to path
PREPROC_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "04_preprocessing_and_nlp_training"))
if PREPROC_DIR not in sys.path:
    sys.path.insert(0, PREPROC_DIR)

from text_preprocessor import TextPreprocessor

SAVED_MODELS_DIR = os.path.join(PREPROC_DIR, "saved_models")

COPING_STRATEGIES = {
    "High Stress": [
        "Reach out to University Student Counseling Services (24/7 Helpline available).",
        "Practice 4-7-8 deep breathing: Inhale 4s, hold 7s, exhale 8s to calm the nervous system.",
        "Request an emergency 48-hour extension via your academic advisor or course coordinator.",
        "Take an immediate 30-minute cognitive break away from screens and academic material."
    ],
    "Overload": [
        "Use the Eisenhower Matrix: categorize your tasks into Urgent vs. Important.",
        "Break large deliverables down into 25-minute Pomodoro study sprints.",
        "Form or join a course study circle to distribute reading summaries and problem set reviews.",
        "Consult your professor or TA during office hours to prioritize core assignment objectives."
    ],
    "Frustration": [
        "Schedule a 1-on-1 meeting during TA office hours to review grading rubric details.",
        "Draft a structured, constructive feedback email highlighting specific unclear assignment prompts.",
        "Utilize peer discussion boards (Ed Discussion / Piazza / Canvas) to share alternative solution paths."
    ],
    "Disengagement": [
        "Reconnect with your core goals: remind yourself why you chose this degree or major.",
        "Start with a micro-goal: study for just 15 minutes without distraction today.",
        "Change your study environment: try the university library silent reading room or group hub.",
        "Speak with an academic success coach to realign your study strategies."
    ],
    "Positive": [
        "Share your positive feedback with the course team on the official end-of-semester survey!",
        "Consider applying as a Peer Tutor or Undergraduate Teaching Assistant for this course next term.",
        "Document effective study methods you used to help guide upcoming course cohorts."
    ],
    "Neutral": [
        "Continue keeping up with weekly course deadlines and syllabus milestones.",
        "Review upcoming exam dates and synchronize your calendar with assignment due dates."
    ]
}

ASPECT_KEYWORDS = {
    "Mental Well-being": ["anxiety", "panic", "mental health", "sleep", "crying", "depress", "burnout", "paralyz", "dread", "insomnia", "suicidal"],
    "Workload": ["deadline", "hours", "workload", "reading", "pset", "heavy", "volume", "overwhelm", "unsustainable", "back to back"],
    "Examination": ["exam", "midterm", "final", "test", "quiz", "grading", "rubric", "points", "grade", "gpa", "scored"],
    "Teaching": ["professor", "instructor", "lecturer", "teach", "slide", "explanation", "pace", "lecture"],
    "Support": ["ta", "office hour", "email", "portal", "lms", "crash", "queue", "response", "reply", "help"],
    "Course Content": ["syllabus", "textbook", "reading", "project", "assignment", "lab", "coding", "theory"]
}

class AcademicStressPredictor:
    def __init__(self):
        self.preprocessor = TextPreprocessor(preserve_negations=True, expand_abbreviations=True)
        self.model = None
        self.vectorizer = None
        self.label_encoder = None
        self.metadata = None
        self._load_artifacts()

    def _load_artifacts(self):
        model_path = os.path.join(SAVED_MODELS_DIR, "stress_classifier.joblib")
        vectorizer_path = os.path.join(SAVED_MODELS_DIR, "tfidf_vectorizer.joblib")
        encoder_path = os.path.join(SAVED_MODELS_DIR, "label_encoder.joblib")
        metadata_path = os.path.join(SAVED_MODELS_DIR, "model_metadata.json")

        if not (os.path.exists(model_path) and os.path.exists(vectorizer_path) and os.path.exists(encoder_path)):
            raise FileNotFoundError(f"Model artifacts missing in {SAVED_MODELS_DIR}. Run train.py first.")

        self.model = joblib.load(model_path)
        self.vectorizer = joblib.load(vectorizer_path)
        self.label_encoder = joblib.load(encoder_path)

        if os.path.exists(metadata_path):
            with open(metadata_path, "r", encoding="utf-8") as f:
                self.metadata = json.load(f)

    def _detect_aspect(self, text: str) -> str:
        text_lower = text.lower()
        for aspect, keywords in ASPECT_KEYWORDS.items():
            if any(kw in text_lower for kw in keywords):
                return aspect
        return "General Academic"

    def _calculate_stress_index(self, label: str, confidence: float, proba_dict: dict) -> int:
        weights = {
            "High Stress": 100,
            "Overload": 80,
            "Frustration": 65,
            "Disengagement": 50,
            "Neutral": 25,
            "Positive": 5
        }
        # Weighted expectation of stress
        expected_stress = sum(proba_dict.get(k, 0.0) * weights.get(k, 20) for k in weights)
        return int(np.clip(round(expected_stress), 0, 100))

    def predict(self, raw_text: str) -> dict:
        if not raw_text or not raw_text.strip():
            return {
                "error": "Empty input provided.",
                "student_text": "",
                "predicted_label": "Neutral",
                "confidence": 0.0,
                "stress_index": 0,
                "urgency": "Low",
                "aspect": "General",
                "probabilities": {},
                "recommendations": []
            }

        cleaned = self.preprocessor.clean_text(raw_text)
        tfidf_vec = self.vectorizer.transform([cleaned])
        
        # Probabilities
        if hasattr(self.model, "predict_proba"):
            probs = self.model.predict_proba(tfidf_vec)[0]
        else:
            decision = self.model.decision_function(tfidf_vec)[0]
            probs = np.exp(decision) / np.sum(np.exp(decision))

        pred_idx = np.argmax(probs)
        pred_label = self.label_encoder.inverse_transform([pred_idx])[0]
        confidence = float(probs[pred_idx])

        class_names = list(self.label_encoder.classes_)
        proba_dict = {cls: round(float(p), 4) for cls, p in zip(class_names, probs)}

        stress_index = self._calculate_stress_index(pred_label, confidence, proba_dict)
        aspect = self._detect_aspect(raw_text)

        if stress_index >= 75:
            urgency = "High"
        elif stress_index >= 45:
            urgency = "Medium"
        else:
            urgency = "Low"

        recommendations = COPING_STRATEGIES.get(pred_label, COPING_STRATEGIES["Neutral"])

        return {
            "student_text": raw_text,
            "cleaned_text": cleaned,
            "predicted_label": pred_label,
            "confidence": round(confidence, 4),
            "confidence_pct": f"{confidence * 100:.1f}%",
            "stress_index": stress_index,
            "urgency": urgency,
            "aspect": aspect,
            "sentiment": "Positive" if pred_label == "Positive" else ("Neutral" if pred_label == "Neutral" else "Negative"),
            "probabilities": proba_dict,
            "recommendations": recommendations,
            "is_alert_required": stress_index >= 75
        }

    def predict_batch(self, text_list: list) -> list:
        return [self.predict(t) for t in text_list]

if __name__ == "__main__":
    predictor = AcademicStressPredictor()
    test_inputs = [
        "I am having severe anxiety and panic attacks because of the upcoming final exam.",
        "I'm not stressed at all, the professor explains complex algorithms with great clarity!",
        "Three heavy project deadlines in 48 hours is completely impossible.",
        "Teaching assistants took over a month to return our graded homework.",
        "The course syllabus was distributed on the first day of class."
    ]
    
    print("=" * 70)
    print(" Standalone NLP Predictor - Test Inferences")
    print("=" * 70)
    for sample in test_inputs:
        res = predictor.predict(sample)
        print(f"\n[Input] {sample}")
        print(f" -> Label       : {res['predicted_label']} (Confidence: {res['confidence_pct']})")
        print(f" -> Stress Index: {res['stress_index']}/100 | Urgency: {res['urgency']} | Aspect: {res['aspect']}")
        print(f" -> Top Advice  : {res['recommendations'][0]}")
    print("=" * 70)
