"""
train_advanced_models.py - Multi-Model NLP Benchmark
Compares multiple machine learning architectures:
1. Multinomial Logistic Regression
2. Linear Support Vector Classifier (LinearSVC with Calibrated probabilities)
3. Multinomial Naive Bayes
4. Random Forest Classifier
5. Soft-Voting Ensemble
"""

import os
import sys
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedKFold, cross_validate
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.calibration import CalibratedClassifierCV
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.preprocessing import LabelEncoder

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from text_preprocessor import TextPreprocessor

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "03_dataset_collection_and_exploration", "data", "academic_stress_dataset.csv")

def benchmark_models():
    print("=" * 75)
    print(" Benchmarking Multi-Class NLP Models on Academic Stress Dataset")
    print("=" * 75)
    
    df = pd.read_csv(DATA_PATH)
    preprocessor = TextPreprocessor()
    df['cleaned_text'] = preprocessor.transform_series(df['student_text'])
    
    le = LabelEncoder()
    y = le.fit_transform(df['label'])
    
    vectorizer = TfidfVectorizer(ngram_range=(1, 3), sublinear_tf=True, min_df=1)
    X = vectorizer.fit_transform(df['cleaned_text'])
    
    models = {
        "Logistic Regression (L2)": LogisticRegression(C=3.0, max_iter=1000, class_weight='balanced'),
        "Calibrated Linear SVC": CalibratedClassifierCV(LinearSVC(C=1.5, dual='auto', random_state=42)),
        "Multinomial Naive Bayes": MultinomialNB(alpha=0.1),
        "Random Forest (n=150)": RandomForestClassifier(n_estimators=150, max_depth=20, random_state=42),
        "Voting Ensemble (Soft)": VotingClassifier(
            estimators=[
                ('lr', LogisticRegression(C=3.0, max_iter=1000)),
                ('svc', CalibratedClassifierCV(LinearSVC(C=1.5, dual='auto', random_state=42))),
                ('nb', MultinomialNB(alpha=0.1))
            ],
            voting='soft'
        )
    }
    
    results = []
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    
    print(f"\nEvaluating with 5-Fold Stratified Cross-Validation (N = {len(df)}):")
    print("-" * 75)
    print(f"{'Model Architecture':<30} | {'Acc (Mean ± Std)':<18} | {'Macro F1 (Mean ± Std)':<20}")
    print("-" * 75)
    
    for name, model in models.items():
        scores = cross_validate(
            model, X, y, cv=cv, scoring=['accuracy', 'f1_macro'], n_jobs=-1
        )
        acc_mean, acc_std = scores['test_accuracy'].mean(), scores['test_accuracy'].std()
        f1_mean, f1_std = scores['test_f1_macro'].mean(), scores['test_f1_macro'].std()
        
        results.append({
            "model": name,
            "accuracy": f"{acc_mean*100:.2f}% ± {acc_std*100:.2f}%",
            "macro_f1": f"{f1_mean:.4f} ± {f1_std:.4f}",
            "f1_num": f1_mean
        })
        print(f"{name:<30} | {acc_mean*100:.2f}% (±{acc_std*100:.2f}%)   | {f1_mean:.4f} (±{f1_std:.4f})")

    print("-" * 75)
    best_model = max(results, key=lambda x: x['f1_num'])
    print(f"[+] Top Performing Architecture: {best_model['model']} (Macro F1 = {best_model['macro_f1']})")
    print("=" * 75)

if __name__ == "__main__":
    benchmark_models()
