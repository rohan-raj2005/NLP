# 3-Hour Hackathon Execution Plan

## Phase 1: Problem Formulation & Architecture Setup (0:00 - 0:45)
* Translate e-commerce sentiment tutorial into academic stress classification.
* Define 6 target classes: High Stress, Overload, Frustration, Disengagement, Neutral, Positive.
* Run `02_project_setup_and_architecture/setup_project.py`.

## Phase 2: Data Synthesis & Model Training (0:45 - 1:30)
* Generate synthetic survey datasets with realistic academic prompts via `download_datasets.py`.
* Implement negation-preserving text preprocessor and N-Gram TF-IDF feature extractor.
* Train Multinomial Logistic Regression and benchmark with 5-Fold Stratified CV.

## Phase 3: REST API & Interactive UI Dashboard (1:30 - 2:30)
* Build REST API endpoints (`/api/analyze`, `/api/batch`, `/api/health`, `/api/insights`).
* Assemble interactive glassmorphic dashboard with live stress gauge, sentiment badges, and batch CSV processor.

## Phase 4: Verification, Edge Case Testing & Demo Polish (2:30 - 3:00)
* Run automated edge case suite `run_all_tests.py`.
* Rehearse live demonstration flow using predefined showcase test inputs.
