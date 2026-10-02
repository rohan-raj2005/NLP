# Test Execution & Quality Assurance Report

**Execution Timestamp**: 2026-10-02 13:17:23  
**Total Runtime**: `2.263 seconds`  
**Overall Status**: **PASSED (100% Green)**  

---

## 1. Test Suite Results Summary

| Test Suite | Tests Executed | Passed | Failed | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Preprocessing & Negation Engine** | 3 assertions | 3 | 0 |  PASSED |
| **Model Serialization & Calibration** | 4 assertions | 4 | 0 |  PASSED |
| **Edge Cases & Nuanced Distinctions** | 8 test cases | 8 | 0 |  PASSED |
| **Total** | **15 Checks** | **15** | **0** | **100% Pass** |

---

## 2. Key Edge Cases Verified

1. **Negation Flipping**: `"I am not stressed at all, the TA was super helpful"` correctly maps to `Positive` with low stress ($12/100$), successfully passing negation checks.
2. **Acute Panic Detection**: `"I am having severe anxiety and panic attacks"` triggers `High Stress` with an emergency-level index ($96/100$).
3. **Overload Separation**: High workload statements trigger `Overload` and Eisenhower coping strategies without false positive psychiatric panic alerts.
4. **Factual Neutrality**: Objective course statements correctly produce `Neutral` classifications.
