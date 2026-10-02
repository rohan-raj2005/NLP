# Project Directory Structure & Blueprint

This document outlines the complete architectural taxonomy of the workspace.

---

## 🌳 Directory Tree

```
c:/Users/User/OneDrive/Desktop/NLP/
│
├── 01_video_mapping_and_concept/             # Conceptual Foundation
│   ├── README.md                             # Executive summary
│   ├── video_workflow_mapping.md             # E-commerce vs. Student Stress mapping
│   └── problem_definition_and_architecture.md# Formal NLP classification schema
│
├── 02_project_setup_and_architecture/        # Configuration & Environment
│   ├── README.md                             # Setup guide
│   ├── requirements.txt                      # Python dependencies
│   ├── package.json                          # Node.js dependencies
│   ├── .env.example                          # Environment template
│   ├── setup_project.py                      # Diagnostic verification script
│   ├── quickstart.bat                        # One-click Windows runner
│   └── project_structure.md                  # This file
│
├── 03_dataset_collection_and_exploration/    # Data Layer
│   ├── README.md                             # Dataset overview & EDA guide
│   ├── download_datasets.py                  # Downloader for open academic datasets
│   ├── eda.py                                # Exploratory Data Analysis script
│   ├── eda_report.md                         # Detailed statistical report
│   └── data/
│       ├── student_feedback_dataset.csv      # Primary multi-class dataset (3,000+ entries)
│       ├── academic_stress_dataset.csv       # Specialized stress & burnout dataset
│       └── student_course_feedback.csv       # Course-level aspect evaluation data
│
├── 04_preprocessing_and_nlp_training/        # Machine Learning Layer
│   ├── README.md                             # Training workflow & evaluation
│   ├── text_preprocessor.py                  # Negation-aware text cleaning pipeline
│   ├── train.py                              # Baseline & production model trainer
│   ├── train_advanced_models.py              # Multi-model benchmark (LR, SVC, RF, Voting)
│   ├── evaluate_model.py                     # Metric generator & confusion matrix
│   ├── training_metrics_report.md            # Detailed performance breakdown
│   └── saved_models/
│       ├── stress_classifier.joblib          # Trained ML model artifact
│       ├── tfidf_vectorizer.joblib           # Fitted TF-IDF vectorizer
│       ├── label_encoder.joblib              # Label encoder mapping
│       └── model_metadata.json               # Model parameters, version, & metrics
│
├── 05_backend_api_and_inference/             # Backend & API Gateway
│   ├── README.md                             # API documentation & usage
│   ├── predict.py                            # Standalone Python inference engine
│   ├── api_server.py                         # Production Python REST API (FastAPI/HTTP)
│   ├── express_server.js                     # Node.js Express server implementation
│   ├── test_endpoints.py                     # Automated endpoint verification
│   └── api_documentation.md                  # Swagger-style REST endpoint specs
│
├── 06_frontend_react_app/                    # User Interface Layer
│   ├── README.md                             # Frontend documentation & features
│   ├── index.html                            # Interactive Glassmorphic Web Dashboard
│   ├── styles.css                            # Modern styling & micro-animations
│   ├── app.js                                # Frontend reactivity & API client
│   └── react_src/                            # Modular React components
│       ├── App.jsx
│       ├── index.css
│       └── components/
│           ├── StressAnalyzer.jsx
│           ├── BatchAnalysis.jsx
│           ├── ConfidenceGauge.jsx
│           └── SupportTips.jsx
│
├── 07_testing_and_evaluation/                # Quality Assurance & Testing
│   ├── README.md                             # Testing guide & benchmarks
│   ├── test_cases.json                       # Comprehensive test scenarios
│   ├── test_stress_edge_cases.py             # Negation, sarcasm, & stress edge tests
│   ├── test_api_integration.py               # REST API integration tests
│   ├── run_all_tests.py                      # Master automated test runner
│   └── test_results_report.md                # Generated test outcomes report
│
├── 08_deployment_configuration/              # DevOps & Containerization
│   ├── README.md                             # Deployment guide
│   ├── Dockerfile                            # Docker container specification
│   ├── docker-compose.yml                    # Multi-container orchestration
│   ├── vercel.json                           # Vercel deployment manifest
│   ├── render.yaml                           # Render cloud configuration
│   ├── Procfile                              # Heroku / Railway process file
│   └── deployment_guide.md                   # Cloud rollout walk-through
│
├── 09_hackathon_strategy_and_demo/           # Presentation & Hackathon Strategy
│   ├── README.md                             # Hackathon guide
│   ├── hackathon_3hr_execution_plan.md       # 3-Hour sprint timeline & milestones
│   ├── pitch_deck_presentation.md            # Slide deck script & key talking points
│   ├── live_demo_script.md                   # Live demo step-by-step walkthrough
│   └── judges_faq_and_answers.md             # Defense against technical questions
│
└── README.md                                 # Master Repository Readme
```
