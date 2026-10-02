# Exploratory Data Analysis (EDA) Report

**Dataset**: `academic_stress_dataset.csv`  
**Total Records**: 2,100  
**Features**: `feedback_id, student_text, label, aspect, stress_level, sentiment, urgency, token_count, char_length`  
**Missing Values**: None detected ({'feedback_id': 0, 'student_text': 0, 'label': 0, 'aspect': 0, 'stress_level': 0, 'sentiment': 0, 'urgency': 0})  

---

## 1. Class Distribution

| Primary Class Label | Sample Count | Percentage | Primary Indicators |
| :--- | :--- | :--- | :--- |
| **Frustration** | 400 | 19.05% | `students`, `not`, `happy`, `slides` |
| **Overload** | 400 | 19.05% | `no`, `time`, `hours`, `night` |
| **High Stress** | 400 | 19.05% | `feel`, `am`, `every`, `about` |
| **Positive** | 400 | 19.05% | `not`, `professor`, `hours`, `teaching` |
| **Neutral** | 280 | 13.33% | `hours`, `final`, `midterm`, `textbook` |
| **Disengagement** | 220 | 10.48% | `because`, `just`, `get`, `completely` |

---

## 2. Textual Complexity & Token Statistics

- **Average Token Count per Comment**: `12.9` words
- **Median Token Count**: `13` words
- **Shortest Feedback**: `8` words
- **Longest Feedback**: `18` words
- **Standard Deviation**: `1.95` words

### Length Distribution by Label:
| Label | Mean Word Count | Min Words | Max Words |
| :--- | :--- | :--- | :--- |
| **Frustration** | 12.8 | 10 | 18 |
| **Neutral** | 10.6 | 8 | 13 |
| **Overload** | 13.9 | 11 | 16 |
| **High Stress** | 13.8 | 12 | 16 |
| **Positive** | 12.4 | 9 | 16 |
| **Disengagement** | 13.5 | 12 | 15 |

---

## 3. Aspect Domain Representation

| Aspect Domain | Frequency | Share |
| :--- | :--- | :--- |
| **Workload** | 400 | 19.0% |
| **Mental Well-being** | 400 | 19.0% |
| **Support** | 257 | 12.2% |
| **Examination** | 238 | 11.3% |
| **Teaching** | 234 | 11.1% |
| **Engagement** | 220 | 10.5% |
| **Course Content** | 219 | 10.4% |
| **Lab Work** | 68 | 3.2% |
| **Library/Resources** | 64 | 3.0% |

---

## 4. Key NLP Insights & Engineering Recommendations

1. **Balanced Multi-Class Spectrum**: High Stress, Overload, Frustration, and Positive classes each have 300+ balanced samples, ensuring robust multi-class discriminative power without acute majority-class bias.
2. **Negation Sensitivity Requirement**: Expressions such as *"not overwhelmed"*, *"not happy"*, and *"never felt so anxious"* highlight the absolute necessity of **negation preservation** during tokenization.
3. **N-gram Richness**: Multi-word expressions like *"panic attack"*, *"heavy workload"*, *"office hours"*, and *"problem set"* carry the highest discriminative weights. A sublinear $(1, 3)$ TF-IDF feature space is recommended.
