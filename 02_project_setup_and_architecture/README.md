# Section 2: Project Setup & Architecture

Welcome to **Section 2** of the Academic Stress & Student Feedback NLP System.

This module provides all configuration, dependency manifests, automation scripts, and environment templates required to initialize, configure, and manage the full stack development environment.

---

## 📁 Section Contents

| File | Purpose |
| :--- | :--- |
| [`requirements.txt`](file:///c:/Users/User/OneDrive/Desktop/NLP/02_project_setup_and_architecture/requirements.txt) | Python dependencies for Data Science, NLP preprocessing, Scikit-learn, and Web APIs. |
| [`package.json`](file:///c:/Users/User/OneDrive/Desktop/NLP/02_project_setup_and_architecture/package.json) | Node.js backend & frontend dependency manifest (Express, CORS, React, Lucide icons). |
| [`.env.example`](file:///c:/Users/User/OneDrive/Desktop/NLP/02_project_setup_and_architecture/.env.example) | Environment variable template for server ports, model paths, and API keys. |
| [`setup_project.py`](file:///c:/Users/User/OneDrive/Desktop/NLP/02_project_setup_and_architecture/setup_project.py) | Automated Python environment validation and directory verification script. |
| [`quickstart.bat`](file:///c:/Users/User/OneDrive/Desktop/NLP/02_project_setup_and_architecture/quickstart.bat) | One-click Windows startup script to launch training, API server, and web dashboard. |
| [`project_structure.md`](file:///c:/Users/User/OneDrive/Desktop/NLP/02_project_setup_and_architecture/project_structure.md) | Comprehensive folder tree and component responsibilities breakdown. |

---

## 🚀 Quick Setup Instructions

### 1. Python Virtual Environment Setup (Recommended)
```bash
# Create a virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
.\venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Install all dependencies
pip install -r requirements.txt
```

### 2. Verify Environment
```bash
python setup_project.py
```
