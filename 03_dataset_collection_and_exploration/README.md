# Section 3: Dataset Collection & Exploratory Data Analysis (EDA)

Welcome to **Section 3** of the Academic Stress Detection and Student Feedback NLP Platform.

This module houses all dataset downloaders, CSV data storage, statistical data profiles, and exploratory data analysis tools.

---

## 📂 CSV Datasets Available in [`/data`](file:///c:/Users/User/OneDrive/Desktop/NLP/03_dataset_collection_and_exploration/data)

1. [`academic_stress_dataset.csv`](file:///c:/Users/User/OneDrive/Desktop/NLP/03_dataset_collection_and_exploration/data/academic_stress_dataset.csv)
   - **Primary 6-Class Dataset** (1,862 samples)
   - Columns: `feedback_id`, `student_text`, `label`, `aspect`, `stress_level`, `sentiment`, `urgency`
   - Target Classes: `High Stress`, `Overload`, `Frustration`, `Disengagement`, `Positive`, `Neutral`

2. [`student_feedback_dataset.csv`](file:///c:/Users/User/OneDrive/Desktop/NLP/03_dataset_collection_and_exploration/data/student_feedback_dataset.csv)
   - **Standard Sentiment Dataset** (1,200 samples)
   - Columns: `id`, `student_feedback`, `sentiment`, `category`, `rating`
   - Labels: `Positive`, `Negative`, `Neutral`

3. [`student_course_feedback.csv`](file:///c:/Users/User/OneDrive/Desktop/NLP/03_dataset_collection_and_exploration/data/student_course_feedback.csv)
   - **Course Evaluation Dataset** (600 samples)
   - Columns: `evaluation_id`, `course_id`, `term`, `feedback_comment`, `primary_label`, `aspect_domain`, `stress_index`

---

## 📊 Summary of Exploratory Data Analysis

Read the full report at [`eda_report.md`](file:///c:/Users/User/OneDrive/Desktop/NLP/03_dataset_collection_and_exploration/eda_report.md).

| Class Label | Sample Share | Average Token Length | Primary Trigger Domains |
| :--- | :--- | :--- | :--- |
| **High Stress** | ~19% | 13.5 words | Mental Well-being, Exam Anxiety, Sleep Loss |
| **Overload** | ~19% | 14.1 words | Workload, Deadlines, Multiple Assignments |
| **Frustration** | ~19% | 13.2 words | Vague Grading, Unresponsive TAs, Portal Crashes |
| **Positive** | ~19% | 12.8 words | Clear Lectures, Supportive TAs, Great Labs |
| **Neutral** | ~13% | 11.2 words | Course Logistics, Syllabus, LMS Deadlines |
| **Disengagement** | ~11% | 11.8 words | Loss of Motivation, Detached, Missing Classes |

---

## 🛠️ Usage Scripts

```bash
# Re-generate or augment datasets
python download_datasets.py

# Run Exploratory Data Analysis & update statistical report
python eda.py
```
