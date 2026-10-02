# Section 6: Frontend User Interface & Interactive Dashboard

Welcome to **Section 6** of the Academic Stress Detection & Student Feedback Platform.

This module contains both:
1. **Interactive Glassmorphic Web App** (`index.html`, `styles.css`, `app.js`): Zero-build, runs instantly in any browser when `api_server.py` is started or standalone.
2. **React + Vite Source Tree** (`react_src/`): Complete component hierarchy for React developers (`App.jsx`, `StressAnalyzer.jsx`, `BatchAnalysis.jsx`, `ConfidenceGauge.jsx`, `SupportTips.jsx`).

---

## 🌟 Key UI Features

- **Real-Time NLP Prediction**: Instant text analysis with confidence probability gauges.
- **Negation Preset Testing**: Quick buttons for testing complex sentiment edge cases (e.g. *"not stressed"*, *"cannot keep up"*).
- **Academic Stress Gauge (0 - 100)**: Color-coded visual indicator of cognitive burnout and urgency.
- **Actionable Coping Interventions**: Auto-generated evidence-based student support recommendations.
- **Batch Course Survey Insights**: Class-wide sentiment breakdown table and distress percentage metrics.
- **Modern Glassmorphism Design**: Dark mode, ambient gradients, micro-animations, and responsive layout.

---

## 🚀 How to Launch the UI

### Method 1: Integrated Python Server (Recommended)
```bash
python ../05_backend_api_and_inference/api_server.py
```
Open your browser at `http://127.0.0.1:8000/`.

### Method 2: Direct File Open
Double click [`index.html`](file:///c:/Users/User/OneDrive/Desktop/NLP/06_frontend_react_app/index.html) to open in your default browser. It includes a built-in client-side predictor fallback.
