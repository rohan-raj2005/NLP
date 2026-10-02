# 2-Minute Live Demo Script

1. **Open the Dashboard**: Navigate to `http://127.0.0.1:8000/`. Highlight the clean glassmorphic UI, live backend status (`Online`), and average dataset stress metrics.
2. **Single Inference - High Stress Case**:
   - Paste: *"I am having severe anxiety and panic attacks because of the upcoming final exam."*
   - Click **Analyze Reflection**.
   - Show: Predicted label `High Stress`, Stress Index `98/100`, Urgency `High`, Aspect `Mental Well-being`, and instant alert banner with student counseling hotline.
3. **Negation Robustness Demo**:
   - Paste: *"I am not stressed at all, the professor explains complex algorithms with great clarity!"*
   - Click **Analyze Reflection**.
   - Show: Correctly recognized as `Positive` (Stress Index `8/100`), demonstrating that the negation preprocessor did not misclassify the word "stressed".
4. **Batch Analysis Mode**:
   - Switch to the **Batch Upload / Multi-Line** tab.
   - Click **Load Sample Batch** and click **Process Batch**.
   - Show aggregate batch chart, distribution of categories, and emergency alert list.
