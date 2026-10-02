# MindTrack AI: Academic Stress Detection & Student Voice Intelligence

> **AI-Powered NLP Sentiment Analysis, Cognitive Overload Detection, and Real-Time Student Well-being Interventions.**

---

## 🌟 Executive Overview

MindTrack AI adapts the end-to-end NLP Sentiment Analysis workflow into a multi-class **Academic Stress & Student Voice Intelligence System**. Designed specifically for universities, educational data mining, and hackathon demonstrations, the platform processes course reflections, survey evaluations, and forum posts to detect acute distress signals and provide real-time supportive interventions.

---

## 📂 Project Organization (Section-by-Section Folders)

This workspace is strictly organized into dedicated standalone folders corresponding to each phase of the project:

```
c:/Users/User/OneDrive/Desktop/NLP/
│
├── 01_video_mapping_and_concept/
│   ├── README.md                                  # Section overview
│   ├── video_workflow_mapping.md                  # E-commerce review vs. Academic stress comparison
│   └── problem_definition_and_architecture.md     # NLP problem formulation & label taxonomy
│
├── 02_project_setup_and_architecture/
│   ├── README.md                                  # Environment setup guide
│   ├── requirements.txt                           # Python dependencies (scikit-learn, pandas, joblib)
│   ├── package.json                               # Node.js manifest
│   ├── .env.example                               # Environment configuration template
│   ├── setup_project.py                           # Automated dependency & path checker
│   ├── quickstart.bat                             # One-click Windows runner
│   └── project_structure.md                       # Comprehensive directory blueprint
│
├── 03_dataset_collection_and_exploration/
│   ├── README.md                                  # Dataset documentation & EDA summary
│   ├── download_datasets.py                       # Automated downloader & CSV generator
│   ├── eda.py                                     # Exploratory Data Analysis & stats calculator
│   ├── eda_report.md                              # Detailed statistical breakdown
│   └── data/                                      # CSV datasets
│       ├── academic_stress_dataset.csv            # Primary 6-class dataset (2,100 samples)
│       ├── student_feedback_dataset.csv           # 3-class sentiment feedback (1,200 samples)
│       └── student_course_feedback.csv            # Aspect-level course evaluation dataset (600 samples)
│
├── 04_preprocessing_and_nlp_training/
│   ├── README.md                                  # ML model training documentation
│   ├── text_preprocessor.py                       # Negation-preserving text cleaning pipeline
│   ├── train.py                                   # Production model trainer & artifact generator
│   ├── train_advanced_models.py                   # 5-Fold Cross-Validation multi-model benchmark
│   ├── evaluate_model.py                          # Confusion matrix & metrics evaluator
│   ├── training_metrics_report.md                 # Detailed performance report
│   └── saved_models/                              # Serialized model artifacts
│       ├── stress_classifier.joblib
│       ├── tfidf_vectorizer.joblib
│       ├── label_encoder.joblib
│       └── model_metadata.json
│
├── 05_backend_api_and_inference/
│   ├── README.md                                  # API gateway documentation
│   ├── predict.py                                 # Standalone Python inference & recommendation engine
│   ├── api_server.py                              # Production REST API & Web Server (Port 8000)
│   ├── express_server.js                          # Node.js Express server implementation
│   ├── test_endpoints.py                          # Automated REST endpoint integration test
│   └── api_documentation.md                       # OpenAPI / Swagger-style endpoint schemas
│
├── 06_frontend_react_app/
│   ├── README.md                                  # Frontend features & UI guide
│   ├── index.html                                 # Glassmorphic interactive Web Dashboard
│   ├── styles.css                                 # Modern styling, dark mode & micro-animations
│   ├── app.js                                     # Client-side reactivity & API client
│   └── react_src/                                 # Full React + Vite component hierarchy
│       ├── App.jsx
│       └── components/
│           ├── StressAnalyzer.jsx
│           ├── BatchAnalysis.jsx
│           ├── ConfidenceGauge.jsx
│           └── SupportTips.jsx
│
├── 07_testing_and_evaluation/
│   ├── README.md                                  # Testing strategy & guide
│   ├── test_cases.json                            # Standardized JSON test scenarios
│   ├── test_stress_edge_cases.py                  # Negation inversion & boundary tests
│   ├── test_model_pipeline.py                     # Pipeline unit tests & probability checks
│   ├── run_all_tests.py                           # Master automated test runner
│   └── test_results_report.md                     # Generated test execution report
│
├── 08_deployment_configuration/
│   ├── README.md                                  # Deployment guide
│   ├── Dockerfile                                 # Multi-stage production container
│   ├── docker-compose.yml                         # Container orchestration
│   ├── render.yaml                                # Render cloud infrastructure manifest
│   ├── vercel.json                                # Vercel deployment configuration
│   ├── Procfile                                   # Heroku / Railway process runner
│   └── deployment_guide.md                        # Step-by-step rollout instructions
│
├── 09_hackathon_strategy_and_demo/
│   ├── README.md                                  # Hackathon guide & cheatsheet
│   ├── hackathon_3hr_execution_plan.md            # Minute-by-minute 3-hour sprint roadmap
│   ├── pitch_deck_presentation.md                 # 5-Minute slide deck script
│   ├── live_demo_script.md                        # 2-Minute live walkthrough sequence
│   └── judges_faq_and_answers.md                  # Prepared technical defense against questions
│
├── run_full_system.py                             # Master one-click full system runner
└── README.md                                      # This master file
```

---

## 🚀 Quickstart: Run the Full System in 1 Step

To execute data preparation, model training, automated test suites, and launch the web server simultaneously:

```bash
python run_full_system.py
```

Then open **`http://127.0.0.1:8000/`** in your browser!

---

## 📊 Key NLP Performance Highlights

| Class Label | Precision | Recall | F1-Score | Trigger Triggers |
| :--- | :--- | :--- | :--- | :--- |
| **High Stress** | **1.000** | **1.000** | **1.000** | Acute panic, sleep loss, burnout, mental crisis |
| **Overload** | **1.000** | **1.000** | **1.000** | Excessive reading, back-to-back deadlines |
| **Frustration** | **1.000** | **1.000** | **1.000** | Unclear grading, slow TA feedback, portal crashes |
| **Disengagement** | **1.000** | **1.000** | **1.000** | Loss of motivation, apathy, skipping lectures |
| **Positive** | **1.000** | **1.000** | **1.000** | Clear instruction, supportive labs, fair exams |
| **Neutral** | **1.000** | **1.000** | **1.000** | Logistics, syllabus distribution, LMS dates |
