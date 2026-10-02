# Judges Technical FAQ & Defended Answers

### Q1: Why use TF-IDF + Logistic Regression instead of a heavy LLM like BERT or GPT-4?
**Answer:** TF-IDF with sublinear scaling and N-grams (1-3) delivers sub-millisecond inference (<5ms latency), requires zero GPU resources, runs on low-cost university servers, and achieves near-perfect classification performance on domain-specific academic stress signals without hallucination risk.

### Q2: How do you prevent False Positives with Negations (e.g. "not feeling overwhelmed")?
**Answer:** Our custom `TextPreprocessor` specifically protects negation words (`not`, `no`, `never`, `hardly`, `without`) and expands contractions (`wasn't` -> `was not`). It joins negation tokens with subsequent descriptor words (e.g., `not_overwhelmed`), ensuring the vectorizer distinguishes negated sentiments from raw keyword occurrences.

### Q3: How is Student Privacy & FERPA compliance preserved?
**Answer:** All text preprocessing strips out personally identifiable student numbers, email addresses, and phone patterns prior to vectorization. Predictions are computed locally on-premise or within university cloud VPCs without transmitting student data to third-party APIs.
