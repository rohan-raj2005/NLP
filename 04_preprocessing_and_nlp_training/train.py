"""
train.py - Academic Stress & Student Feedback NLP Model Trainer
Preprocesses text, computes TF-IDF representations (1-3 grams), trains calibrated classifiers,
evaluates performance across classes, and persists versioned joblib models and metadata.
"""

import os
import sys
import json
import joblib
import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, accuracy_score, f1_score, precision_score, recall_score

# Add current folder to sys.path to import text_preprocessor
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from text_preprocessor import TextPreprocessor

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "03_dataset_collection_and_exploration", "data", "academic_stress_dataset.csv")
SAVED_MODELS_DIR = os.path.join(BASE_DIR, "saved_models")
os.makedirs(SAVED_MODELS_DIR, exist_ok=True)

def train_model():
    print("=" * 65)
    print(" Training NLP Academic Stress & Student Feedback Classifier")
    print("=" * 65)
    
    # 1. Load Dataset
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(f"Dataset not found at {DATA_PATH}. Run download_datasets.py first.")
        
    df = pd.read_csv(DATA_PATH)
    print(f"[*] Loaded dataset: {len(df)} samples from {os.path.basename(DATA_PATH)}")
    
    # 2. Preprocess Text
    preprocessor = TextPreprocessor(preserve_negations=True, expand_abbreviations=True)
    print("[*] Preprocessing student texts (contraction expansion, negation preservation)...")
    df['cleaned_text'] = preprocessor.transform_series(df['student_text'])
    
    # 3. Label Encoding
    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(df['label'])
    class_names = list(label_encoder.classes_)
    print(f"[*] Target Classes ({len(class_names)}): {class_names}")
    
    # 4. Train / Test Split
    X_train_raw, X_test_raw, y_train, y_test = train_test_split(
        df['cleaned_text'], y, test_size=0.20, random_state=42, stratify=y
    )
    print(f"[*] Split data: {len(X_train_raw)} training, {len(X_test_raw)} test samples")
    
    # 5. TF-IDF Vectorization
    print("[*] Fitting N-Gram TF-IDF Vectorizer (ngram_range=(1, 3), sublinear_tf=True)...")
    vectorizer = TfidfVectorizer(
        ngram_range=(1, 3),
        max_features=5000,
        sublinear_tf=True,
        min_df=1
    )
    X_train_tfidf = vectorizer.fit_transform(X_train_raw)
    X_test_tfidf = vectorizer.transform(X_test_raw)
    print(f"[*] Vocabulary size: {len(vectorizer.vocabulary_)} features")
    
    # 6. Train Calibrated Logistic Regression
    print("[*] Training Multinomial Logistic Regression model...")
    model = LogisticRegression(
        C=3.0,
        max_iter=1000,
        class_weight='balanced',
        solver='lbfgs',
        random_state=42
    )
    model.fit(X_train_tfidf, y_train)
    
    # 7. Evaluate on Test Set
    y_pred = model.predict(X_test_tfidf)
    acc = accuracy_score(y_test, y_pred)
    macro_f1 = f1_score(y_test, y_pred, average='macro')
    weighted_f1 = f1_score(y_test, y_pred, average='weighted')
    macro_prec = precision_score(y_test, y_pred, average='macro')
    macro_rec = recall_score(y_test, y_pred, average='macro')
    
    print("\n" + "=" * 65)
    print(f" EVALUATION METRICS ON TEST SPLIT (N = {len(y_test)})")
    print("=" * 65)
    print(f"  Accuracy       : {acc * 100:.2f}%")
    print(f"  Macro F1-Score : {macro_f1:.4f}")
    print(f"  Weighted F1    : {weighted_f1:.4f}")
    print(f"  Macro Precision: {macro_prec:.4f}")
    print(f"  Macro Recall   : {macro_rec:.4f}")
    print("=" * 65)
    
    report = classification_report(y_test, y_pred, target_names=class_names, output_dict=True)
    print("\nClass-by-Class Breakdown:")
    for cls in class_names:
        metrics = report[cls]
        print(f"  {cls:<18} | Precision: {metrics['precision']:.3f} | Recall: {metrics['recall']:.3f} | F1: {metrics['f1-score']:.3f}")
        
    # 8. Save Artifacts
    model_path = os.path.join(SAVED_MODELS_DIR, "stress_classifier.joblib")
    vectorizer_path = os.path.join(SAVED_MODELS_DIR, "tfidf_vectorizer.joblib")
    encoder_path = os.path.join(SAVED_MODELS_DIR, "label_encoder.joblib")
    metadata_path = os.path.join(SAVED_MODELS_DIR, "model_metadata.json")
    
    joblib.dump(model, model_path)
    joblib.dump(vectorizer, vectorizer_path)
    joblib.dump(label_encoder, encoder_path)
    
    metadata = {
        "model_name": "Academic Stress & Sentiment Classifier",
        "model_architecture": "TF-IDF (1-3 Grams) + Multinomial Logistic Regression",
        "timestamp": datetime.now().isoformat(),
        "classes": class_names,
        "vocabulary_size": len(vectorizer.vocabulary_),
        "test_metrics": {
            "accuracy": round(float(acc), 4),
            "macro_f1": round(float(macro_f1), 4),
            "weighted_f1": round(float(weighted_f1), 4),
            "macro_precision": round(float(macro_prec), 4),
            "macro_recall": round(float(macro_rec), 4)
        },
        "per_class_metrics": {
            cls: {
                "precision": round(report[cls]["precision"], 4),
                "recall": round(report[cls]["recall"], 4),
                "f1_score": round(report[cls]["f1-score"], 4),
                "support": report[cls]["support"]
            } for cls in class_names
        }
    }
    
    with open(metadata_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)
        
    print("\n[+] Persisted Model Artifacts:")
    print(f"  - Model       : {model_path}")
    print(f"  - Vectorizer  : {vectorizer_path}")
    print(f"  - Encoder     : {encoder_path}")
    print(f"  - Metadata    : {metadata_path}")
    print("=" * 65)
    return metadata

if __name__ == "__main__":
    train_model()
