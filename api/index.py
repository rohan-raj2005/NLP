"""
index.py - Vercel Serverless Function Handler
Handles REST API requests:
- GET /api/health
- GET /api/insights
- GET /api/support-tips
- POST /api/analyze
- POST /api/batch
"""

import os
import sys
import json
import time
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse
import pandas as pd

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

from predict import AcademicStressPredictor, COPING_STRATEGIES

DATA_PATH = os.path.join(CURRENT_DIR, "data", "academic_stress_dataset.csv")

PREDICTOR = None
START_TIME = time.time()

def get_predictor():
    global PREDICTOR
    if PREDICTOR is None:
        PREDICTOR = AcademicStressPredictor()
    return PREDICTOR

class handler(BaseHTTPRequestHandler):
    def _send_cors_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")

    def _send_json(self, status_code: int, data: dict):
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self._send_cors_headers()
        self.end_headers()
        self.wfile.write(json.dumps(data, indent=2).encode("utf-8"))

    def do_OPTIONS(self):
        self.send_response(200)
        self._send_cors_headers()
        self.end_headers()

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path.rstrip('/')

        # 1. Health
        if path == "/api/health" or path.endswith("/health"):
            predictor = get_predictor()
            uptime = round(time.time() - START_TIME, 2)
            self._send_json(200, {
                "status": "online",
                "service": "Academic Stress & Sentiment AI (Vercel Serverless)",
                "uptime_seconds": uptime,
                "model_architecture": predictor.metadata.get("model_architecture", "TF-IDF + Logistic Regression") if predictor.metadata else "Loaded",
                "classes": list(predictor.label_encoder.classes_) if predictor.label_encoder else []
            })
            return

        # 2. Insights
        if path == "/api/insights" or path.endswith("/insights"):
            if os.path.exists(DATA_PATH):
                df = pd.read_csv(DATA_PATH)
                class_dist = df['label'].value_counts().to_dict()
                aspect_dist = df['aspect'].value_counts().to_dict()
                avg_stress = round(float(df['stress_level'].mean() * 20), 1)
                total_samples = len(df)
            else:
                class_dist = {"High Stress": 400, "Overload": 400, "Frustration": 400, "Positive": 400, "Neutral": 280, "Disengagement": 220}
                aspect_dist = {"Workload": 500, "Examination": 450, "Mental Well-being": 400, "Teaching": 400, "Support": 350}
                avg_stress = 66.9
                total_samples = 2100

            self._send_json(200, {
                "total_reviews_analyzed": total_samples,
                "average_stress_index": avg_stress,
                "class_distribution": class_dist,
                "aspect_breakdown": aspect_dist,
                "high_stress_pct": round((class_dist.get("High Stress", 0) / max(total_samples, 1)) * 100, 1)
            })
            return

        # 3. Support Tips
        if path == "/api/support-tips" or path.endswith("/support-tips"):
            self._send_json(200, {
                "coping_catalog": COPING_STRATEGIES,
                "emergency_hotline": "University Mental Health Support: 1-800-273-TALK",
                "wellness_resources": [
                    {"title": "Pomodoro Focus Timer", "url": "https://pomofocus.io"},
                    {"title": "Guided 4-7-8 Breathing", "url": "https://www.headspace.com"},
                    {"title": "Student Academic Counseling", "url": "#counseling"}
                ]
            })
            return

        self._send_json(404, {"error": f"Endpoint '{path}' not found."})

    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path.rstrip('/')

        content_length = int(self.headers.get('Content-Length', 0))
        body_data = self.rfile.read(content_length).decode('utf-8')
        
        try:
            payload = json.loads(body_data) if body_data else {}
        except json.JSONDecodeError:
            self._send_json(400, {"error": "Invalid JSON format in request body."})
            return

        # 1. /api/analyze
        if path == "/api/analyze" or path.endswith("/analyze"):
            text = payload.get("text", "")
            if not text:
                self._send_json(400, {"error": "Missing 'text' parameter in payload."})
                return

            predictor = get_predictor()
            result = predictor.predict(text)
            self._send_json(200, result)
            return

        # 2. /api/batch
        if path == "/api/batch" or path.endswith("/batch"):
            texts = payload.get("texts", [])
            if not isinstance(texts, list) or len(texts) == 0:
                self._send_json(400, {"error": "Payload must contain a non-empty 'texts' array."})
                return

            predictor = get_predictor()
            results = predictor.predict_batch(texts)
            
            stress_indices = [r["stress_index"] for r in results if "stress_index" in r]
            avg_stress = round(sum(stress_indices) / len(stress_indices), 1) if stress_indices else 0
            label_counts = {}
            for r in results:
                lbl = r.get("predicted_label", "Unknown")
                label_counts[lbl] = label_counts.get(lbl, 0) + 1

            high_stress_cases = [r for r in results if r.get("is_alert_required", False)]

            self._send_json(200, {
                "batch_size": len(texts),
                "average_stress_index": avg_stress,
                "label_distribution": label_counts,
                "high_stress_alerts_count": len(high_stress_cases),
                "results": results
            })
            return

        self._send_json(404, {"error": f"Endpoint '{path}' not found."})
