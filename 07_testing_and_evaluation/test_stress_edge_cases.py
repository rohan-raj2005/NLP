"""
test_stress_edge_cases.py - Negation & Edge Case Testing Suite
Validates model predictions on critical linguistic boundary cases (negation, extreme distress, neutral facts).
"""

import os
import sys
import json

# Add predict module to path
PREDICT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "05_backend_api_and_inference"))
if PREDICT_DIR not in sys.path:
    sys.path.insert(0, PREDICT_DIR)

from predict import AcademicStressPredictor

def run_edge_case_tests():
    print("=" * 70)
    print(" Running NLP Stress & Negation Edge Case Tests")
    print("=" * 70)

    predictor = AcademicStressPredictor()
    test_cases_path = os.path.join(os.path.dirname(__file__), "test_cases.json")
    
    with open(test_cases_path, "r", encoding="utf-8") as f:
        cases = json.load(f)

    passed = 0
    failed = 0

    for tc in cases:
        inp = tc["input"]
        res = predictor.predict(inp)
        pred_label = res["predicted_label"]
        stress_idx = res["stress_index"]

        is_label_correct = (pred_label == tc["expected_label"])
        
        # Check stress threshold constraints
        stress_ok = True
        if "expected_stress_min" in tc and stress_idx < tc["expected_stress_min"]:
            stress_ok = False
        if "expected_stress_max" in tc and stress_idx > tc["expected_stress_max"]:
            stress_ok = False

        if is_label_correct and stress_ok:
            passed += 1
            print(f"  [PASS] {tc['id']} - {tc['category']:<28} | Pred: {pred_label:<14} | Stress: {stress_idx:>3}/100")
        else:
            failed += 1
            print(f"  [FAIL] {tc['id']} - {tc['category']:<28} | Pred: {pred_label:<14} (Expected: {tc['expected_label']}) | Stress: {stress_idx:>3}/100")

    print("-" * 70)
    print(f"Results: {passed} Passed, {failed} Failed out of {len(cases)} Edge Tests.")
    print("=" * 70)
    return passed == len(cases)

if __name__ == "__main__":
    success = run_edge_case_tests()
    sys.exit(0 if success else 1)
