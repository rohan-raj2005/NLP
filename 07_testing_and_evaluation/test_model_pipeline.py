"""
test_model_pipeline.py - Pipeline Unit Tests
Tests serialization, preprocessing transformations, array dimensions, and probability calibration.
"""

import os
import sys
import numpy as np
import joblib

PREPROC_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "04_preprocessing_and_nlp_training"))
if PREPROC_DIR not in sys.path:
    sys.path.insert(0, PREPROC_DIR)

from text_preprocessor import TextPreprocessor

def test_preprocessor():
    print("[*] Testing TextPreprocessor...")
    p = TextPreprocessor(preserve_negations=True, expand_abbreviations=True)
    
    # 1. Contraction test
    c_res = p.clean_text("I can't and won't attend")
    assert "cannot" in c_res, "Contraction 'can't' failed to expand to 'cannot'"
    assert "will not" in c_res, "Contraction 'won't' failed to expand to 'will not'"
    
    # 2. Negation preservation test
    n_res = p.clean_text("I am not stressed")
    assert "not" in n_res.split(), "Negation word 'not' was erroneously stripped"
    
    # 3. Academic abbreviation test
    a_res = p.clean_text("prof and ta were in lab")
    assert "professor" in a_res, "Abbreviation 'prof' was not normalized to 'professor'"
    assert "teaching assistant" in a_res, "Abbreviation 'ta' was not normalized"
    print("  [+] TextPreprocessor: ALL PASSED")

def test_artifacts():
    print("[*] Testing Model Artifacts...")
    saved_dir = os.path.join(PREPROC_DIR, "saved_models")
    
    model = joblib.load(os.path.join(saved_dir, "stress_classifier.joblib"))
    vectorizer = joblib.load(os.path.join(saved_dir, "tfidf_vectorizer.joblib"))
    encoder = joblib.load(os.path.join(saved_dir, "label_encoder.joblib"))
    
    assert hasattr(model, "predict"), "Model artifact missing predict method"
    assert hasattr(vectorizer, "transform"), "Vectorizer missing transform method"
    assert len(encoder.classes_) == 6, f"Expected 6 classes, got {len(encoder.classes_)}"
    
    # Check probability sum == 1.0
    vec = vectorizer.transform(["sample student review"])
    probs = model.predict_proba(vec)[0]
    assert np.isclose(np.sum(probs), 1.0), "Predicted probabilities do not sum to 1.0"
    print("  [+] Model Artifacts: ALL PASSED")

def main():
    print("=" * 65)
    print(" NLP Pipeline Unit Tests")
    print("=" * 65)
    test_preprocessor()
    test_artifacts()
    print("=" * 65)
    print(" [+] Pipeline is fully valid and operational!")

if __name__ == "__main__":
    main()
