# Section 5: Backend API & Inference Gateway

Welcome to **Section 5** of the Academic Stress Detection & Student Feedback NLP System.

This module provides the standalone Python inference engine, the production REST API server, Node.js Express bridges, and automated endpoint verification suites.

---

## 📁 Section Contents

| File | Purpose |
| :--- | :--- |
| [`predict.py`](file:///c:/Users/User/OneDrive/Desktop/NLP/05_backend_api_and_inference/predict.py) | Standalone Python prediction engine with stress index computation and coping recommendation generation. |
| [`api_server.py`](file:///c:/Users/User/OneDrive/Desktop/NLP/05_backend_api_and_inference/api_server.py) | High-performance Python HTTP REST API server with static frontend hosting. |
| [`express_server.js`](file:///c:/Users/User/OneDrive/Desktop/NLP/05_backend_api_and_inference/express_server.js) | Alternative Node.js Express server bridge with child process Python runner. |
| [`test_endpoints.py`](file:///c:/Users/User/OneDrive/Desktop/NLP/05_backend_api_and_inference/test_endpoints.py) | Automated integration test script for validating REST endpoints. |
| [`api_documentation.md`](file:///c:/Users/User/OneDrive/Desktop/NLP/05_backend_api_and_inference/api_documentation.md) | Comprehensive REST API documentation with schema specifications. |

---

## 🚀 Running the API Server

```bash
# Start the Python REST API & Web Dashboard
python api_server.py

# In another terminal, run endpoint test suite:
python test_endpoints.py
```

### CLI Prediction Mode:
```bash
python predict.py "I am feeling completely overwhelmed by these midterms."
```
