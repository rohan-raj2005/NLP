# Academic Stress & Sentiment AI - REST API Documentation

This specification documents all REST API endpoints available in the backend service.

---

## Base URL
```
http://127.0.0.1:8000
```

---

## 1. Health & Status Check

- **Method**: `GET`
- **Endpoint**: `/api/health`
- **Description**: Verifies service liveness, uptime, and loaded model architecture.

### Sample Response:
```json
{
  "status": "online",
  "service": "Academic Stress & Sentiment AI",
  "uptime_seconds": 142.3,
  "model_architecture": "TF-IDF (1-3 Grams) + Multinomial Logistic Regression",
  "classes": [
    "Disengagement",
    "Frustration",
    "High Stress",
    "Neutral",
    "Overload",
    "Positive"
  ]
}
```

---

## 2. Single Student Text Analysis

- **Method**: `POST`
- **Endpoint**: `/api/analyze`
- **Headers**: `Content-Type: application/json`

### Request Body:
```json
{
  "text": "I am having severe anxiety and panic attacks because of the upcoming final exam."
}
```

### Response Schema:
```json
{
  "student_text": "I am having severe anxiety and panic attacks because of the upcoming final exam.",
  "cleaned_text": "severe anxiety panic attacks upcoming final exam",
  "predicted_label": "High Stress",
  "confidence": 0.9372,
  "confidence_pct": "93.7%",
  "stress_index": 96,
  "urgency": "High",
  "aspect": "Mental Well-being",
  "sentiment": "Negative",
  "probabilities": {
    "High Stress": 0.9372,
    "Overload": 0.0381,
    "Frustration": 0.0152,
    "Disengagement": 0.0051,
    "Neutral": 0.0024,
    "Positive": 0.0020
  },
  "recommendations": [
    "Reach out to University Student Counseling Services (24/7 Helpline available).",
    "Practice 4-7-8 deep breathing: Inhale 4s, hold 7s, exhale 8s to calm the nervous system.",
    "Request an emergency 48-hour extension via your academic advisor or course coordinator."
  ],
  "is_alert_required": true
}
```

---

## 3. Batch Feedback Analysis

- **Method**: `POST`
- **Endpoint**: `/api/batch`
- **Headers**: `Content-Type: application/json`

### Request Body:
```json
{
  "texts": [
    "The professor explains complex algorithms with great clarity!",
    "3 project deadlines and 2 midterms in 48 hours is impossible.",
    "TA took over a month to return our graded homework."
  ]
}
```

### Response Schema:
```json
{
  "batch_size": 3,
  "average_stress_index": 48.7,
  "label_distribution": {
    "Positive": 1,
    "Overload": 1,
    "Frustration": 1
  },
  "high_stress_alerts_count": 0,
  "results": [ ... ]
}
```

---

## 4. Class-Wide Survey Insights

- **Method**: `GET`
- **Endpoint**: `/api/insights`
- **Description**: Returns dataset-level statistics and stress percentage metrics.
