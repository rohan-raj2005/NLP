# Section 4: Text Preprocessing & NLP Model Training

Welcome to **Section 4** of the Academic Stress & Student Feedback NLP System.

This module houses the entire machine learning pipeline: domain-specific text preprocessing, N-gram TF-IDF feature extraction, multi-model cross-validation benchmarks, model serialization, and evaluation metrics generation.

---

## 📁 Section Contents

| File | Purpose |
| :--- | :--- |
| [`text_preprocessor.py`](file:///c:/Users/User/OneDrive/Desktop/NLP/04_preprocessing_and_nlp_training/text_preprocessor.py) | Negation-aware text cleaning, contraction expansion (`can't` $\to$ `cannot`), and educational term normalization. |
| [`train.py`](file:///c:/Users/User/OneDrive/Desktop/NLP/04_preprocessing_and_nlp_training/train.py) | Main training script that generates versioned model artifacts in `/saved_models`. |
| [`train_advanced_models.py`](file:///c:/Users/User/OneDrive/Desktop/NLP/04_preprocessing_and_nlp_training/train_advanced_models.py) | 5-Fold Stratified Cross-Validation benchmark across 5 distinct ML architectures. |
| [`evaluate_model.py`](file:///c:/Users/User/OneDrive/Desktop/NLP/04_preprocessing_and_nlp_training/evaluate_model.py) | Confusion matrix generator and metrics reporter. |
| [`training_metrics_report.md`](file:///c:/Users/User/OneDrive/Desktop/NLP/04_preprocessing_and_nlp_training/training_metrics_report.md) | Markdown evaluation report with per-class precision, recall, and F1 scores. |
| [`saved_models/`](file:///c:/Users/User/OneDrive/Desktop/NLP/04_preprocessing_and_nlp_training/saved_models) | Serialized artifacts: `stress_classifier.joblib`, `tfidf_vectorizer.joblib`, `label_encoder.joblib`, `model_metadata.json`. |

---

## 🧪 Model Performance Benchmark (5-Fold CV)

| Model Architecture | 5-Fold Accuracy | Macro F1-Score | Inference Latency |
| :--- | :--- | :--- | :--- |
| **Calibrated Linear SVC** | **99.62%** (±0.13%) | **0.9965** | < 2 ms |
| **Multinomial Logistic Regression** | **99.57%** (±0.21%) | **0.9961** | < 2 ms |
| **Soft-Voting Ensemble** | **99.62%** (±0.27%) | **0.9961** | < 5 ms |
| **Multinomial Naive Bayes** | **99.41%** (±0.43%) | **0.9931** | < 1 ms |
| **Random Forest (n=150)** | **93.88%** (±1.83%) | **0.9338** | ~15 ms |

---

## 🚀 How to Run Training & Evaluation

```bash
# 1. Train production model and save artifacts
python train.py

# 2. Run multi-model benchmark
python train_advanced_models.py

# 3. Generate detailed evaluation report
python evaluate_model.py
```
