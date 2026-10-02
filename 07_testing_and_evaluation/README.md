# Section 7: Automated Testing & Evaluation Suite

Welcome to **Section 7** of the Academic Stress Detection & Student Feedback Platform.

This module houses all unit tests, negation benchmarks, edge case verifications, and automated test runners.

---

## 📁 Section Contents

| File | Purpose |
| :--- | :--- |
| [`test_cases.json`](file:///c:/Users/User/OneDrive/Desktop/NLP/07_testing_and_evaluation/test_cases.json) | Standardized JSON test scenarios across all 6 sentiment and stress classes. |
| [`test_stress_edge_cases.py`](file:///c:/Users/User/OneDrive/Desktop/NLP/07_testing_and_evaluation/test_stress_edge_cases.py) | Negation inversion tests, severe panic threshold checks, and subtle boundary verifications. |
| [`test_model_pipeline.py`](file:///c:/Users/User/OneDrive/Desktop/NLP/07_testing_and_evaluation/test_model_pipeline.py) | Preprocessor and serialized artifact sanity checks. |
| [`run_all_tests.py`](file:///c:/Users/User/OneDrive/Desktop/NLP/07_testing_and_evaluation/run_all_tests.py) | Master test runner producing [`test_results_report.md`](file:///c:/Users/User/OneDrive/Desktop/NLP/07_testing_and_evaluation/test_results_report.md). |
| [`test_results_report.md`](file:///c:/Users/User/OneDrive/Desktop/NLP/07_testing_and_evaluation/test_results_report.md) | Formatted test outcomes report. |

---

## 🧪 Verified Test Scenarios

1. **`TC_01` (Positive Feedback)**: Clear, appreciative instruction comments $\to$ `Positive` (Stress $<30/100$).
2. **`TC_02` (High Stress / Panic)**: Sleep deprivation & panic attacks $\to$ `High Stress` (Stress $>75/100$, Alert triggered).
3. **`TC_03` (Workload Overload)**: Compressed project deadlines $\to$ `Overload` (Stress $>60/100$).
4. **`TC_04` (Negation Positive)**: `"I am not stressed at all"` $\to$ `Positive` (Stress $<30/100$).
5. **`TC_05` (Negation Frustration)**: `"I am definitely not happy"` $\to$ `Frustration` (Stress $>40/100$).
6. **`TC_06` (Administrative Frustration)**: Slow grading turnaround $\to$ `Frustration`.
7. **`TC_07` (Academic Disengagement)**: Loss of motivation $\to$ `Disengagement`.
8. **`TC_08` (Neutral Logistics)**: Syllabus and portal facts $\to$ `Neutral`.

---

## 🚀 How to Execute Tests

```bash
# Run the entire test suite:
python run_all_tests.py
```
