"""
test_endpoints.py - Automated REST API Verification
Starts a test server instance or sends requests to an active server,
verifying response status codes, payload structures, and prediction accuracy.
"""

import urllib.request
import json
import time

BASE_URL = "http://127.0.0.1:8000"

def test_api():
    print("=" * 65)
    print(" Testing Academic Stress Detection REST API Endpoints")
    print("=" * 65)
    
    # 1. Test /api/health
    print("\n[1] Testing GET /api/health ...")
    try:
        req = urllib.request.Request(f"{BASE_URL}/api/health")
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            print(f"  [+] Status Code: {resp.status}")
            print(f"  [+] Response   : {data}")
            assert resp.status == 200
            assert data.get("status") == "online"
    except Exception as e:
        print(f"  [-] Failed /api/health: {e}")
        return False

    # 2. Test POST /api/analyze
    print("\n[2] Testing POST /api/analyze ...")
    try:
        payload = json.dumps({"text": "I feel so anxious and overwhelmed by these sudden deadlines."}).encode('utf-8')
        req = urllib.request.Request(
            f"{BASE_URL}/api/analyze",
            data=payload,
            headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            print(f"  [+] Status Code: {resp.status}")
            print(f"  [+] Prediction : {data.get('predicted_label')} (Confidence: {data.get('confidence_pct')})")
            print(f"  [+] Stress Idx : {data.get('stress_index')}/100 | Urgency: {data.get('urgency')}")
            assert resp.status == 200
            assert "predicted_label" in data
            assert data.get("stress_index", 0) > 50
    except Exception as e:
        print(f"  [-] Failed /api/analyze: {e}")
        return False

    # 3. Test POST /api/batch
    print("\n[3] Testing POST /api/batch ...")
    try:
        batch_payload = json.dumps({
            "texts": [
                "The lectures were crystal clear and very helpful.",
                "I am having severe anxiety and cannot sleep before the exam.",
                "Grading was very slow and confusing."
            ]
        }).encode('utf-8')
        req = urllib.request.Request(
            f"{BASE_URL}/api/batch",
            data=batch_payload,
            headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            print(f"  [+] Status Code: {resp.status}")
            print(f"  [+] Batch Size : {data.get('batch_size')}")
            print(f"  [+] Avg Stress : {data.get('average_stress_index')}")
            print(f"  [+] Breakdown  : {data.get('label_distribution')}")
            assert resp.status == 200
            assert data.get("batch_size") == 3
    except Exception as e:
        print(f"  [-] Failed /api/batch: {e}")
        return False

    # 4. Test GET /api/insights
    print("\n[4] Testing GET /api/insights ...")
    try:
        req = urllib.request.Request(f"{BASE_URL}/api/insights")
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            print(f"  [+] Status Code   : {resp.status}")
            print(f"  [+] Total Reviews : {data.get('total_reviews_analyzed')}")
            print(f"  [+] Avg Class Idx : {data.get('average_stress_index')}")
            assert resp.status == 200
    except Exception as e:
        print(f"  [-] Failed /api/insights: {e}")
        return False

    print("\n" + "=" * 65)
    print(" [+] ALL REST API ENDPOINTS PASSED SUCCESSFULLY!")
    print("=" * 65)
    return True

if __name__ == "__main__":
    test_api()
