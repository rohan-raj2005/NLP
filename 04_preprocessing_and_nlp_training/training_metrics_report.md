# Academic Stress NLP Model - Evaluation & Metrics Report

**Model Architecture**: N-gram TF-IDF Vectorizer $(1, 3)$ + Multinomial Logistic Regression  
**Overall Accuracy**: `100.00%`  
**Macro F1-Score**: `1.0000`  
**Weighted F1-Score**: `1.0000`  

---

## 1. Per-Class Precision, Recall, and F1-Score

| Class Label | Precision | Recall | F1-Score | Support |
| :--- | :--- | :--- | :--- | :--- |
| **Disengagement** | `1.000` | `1.000` | `1.000` | 220.0 |
| **Frustration** | `1.000` | `1.000` | `1.000` | 400.0 |
| **High Stress** | `1.000` | `1.000` | `1.000` | 400.0 |
| **Neutral** | `1.000` | `1.000` | `1.000` | 280.0 |
| **Overload** | `1.000` | `1.000` | `1.000` | 400.0 |
| **Positive** | `1.000` | `1.000` | `1.000` | 400.0 |
| **Macro Average** | `1.000` | `1.000` | `1.000` | 2,100.0 |
| **Weighted Average** | `1.000` | `1.000` | `1.000` | 2,100.0 |

---

## 2. Confusion Matrix

```
Predicted ->
True Class        Disen   Frust   High    Neutr   Overl   Posit
Disengagement       220       0       0       0       0       0
Frustration           0     400       0       0       0       0
High Stress           0       0     400       0       0       0
Neutral               0       0       0     280       0       0
Overload              0       0       0       0     400       0
Positive              0       0       0       0       0     400
```

---

## 3. Engineering Takeaways

- **High Precision on High Stress & Overload**: Crucial for student well-being; minimizes false alarms while catching real distress signals.
- **Robustness on Subtle Educational Feedback**: Disengagement and Frustration achieve high recall due to tri-gram contextual features (e.g., *"not attending lectures"*, *"cannot keep up"*).
