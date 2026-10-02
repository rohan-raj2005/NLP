# Video Workflow Mapping & Architecture Translation

## From E-Commerce Tutorial to Academic Stress Platform

### 1. Data Ingestion & Preprocessing
* **Standard Video Pipeline:** Simple lowercase conversion, regex punctuation stripping, removal of all stopwords.
* **Academic Stress Pipeline:** Negation preservation (`not`, `no`, `never` are retained or converted into `not_word` tokens) to distinguish *"not overwhelmed"* from *"overwhelmed"*. Contraction expansion (`can't` -> `cannot`, `i'm` -> `i am`).

### 2. Feature Extraction
* **Standard Video Pipeline:** Unigram CountVectorizer (Bag of Words).
* **Academic Stress Pipeline:** Sublinear TF-IDF with Unigrams, Bigrams, and Trigrams (`ngram_range=(1, 3)`), capturing complex contextual phrases like `"cannot sleep"`, `"impossible deadlines"`, and `"very helpful lectures"`.

### 3. Machine Learning Classification
* **Standard Video Pipeline:** Binary Logistic Regression / Naive Bayes.
* **Academic Stress Pipeline:** Multinomial Logistic Regression with L2 regularization and probability calibration across 6 granular stress and sentiment categories.

### 4. Downstream Actionability
* **Standard Video Pipeline:** Simple positive/negative output string.
* **Academic Stress Pipeline:** Computes a continuous **Stress Index (0-100)**, categorizes **Urgency (Low/Med/High)**, performs **Aspect Mining**, and suggests **Evidence-Based Coping Strategies** with automated emergency counseling alert triggers.
