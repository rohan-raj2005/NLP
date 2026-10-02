"""
setup_project.py - Environment & Directory Validator
Verifies all prerequisites, checks directory structures, and ensures the environment is ready.
"""

import sys
import os
import importlib

REQUIRED_PACKAGES = [
    ("numpy", "Core numerical math"),
    ("pandas", "Data manipulation & CSV parsing"),
    ("sklearn", "Scikit-learn NLP & Machine Learning"),
    ("joblib", "Model serialization"),
    ("requests", "HTTP communication"),
    ("matplotlib", "Visualization generation"),
]

def check_python_version():
    print(f"[*] Python Version: {sys.version.split()[0]} ({sys.platform})")
    if sys.version_info < (3, 8):
        print("[-] Warning: Python 3.8+ is recommended.")
    else:
        print("[+] Python version OK.")

def check_dependencies():
    print("\n[*] Checking required Python dependencies...")
    all_ok = True
    for pkg_name, desc in REQUIRED_PACKAGES:
        try:
            importlib.import_module(pkg_name)
            print(f"  [+] {pkg_name:<15} : Available ({desc})")
        except ImportError:
            print(f"  [-] {pkg_name:<15} : MISSING ({desc})")
            all_ok = False
    return all_ok

def verify_sections():
    print("\n[*] Verifying 9 Project Sections...")
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    sections = [
        "01_video_mapping_and_concept",
        "02_project_setup_and_architecture",
        "03_dataset_collection_and_exploration",
        "04_preprocessing_and_nlp_training",
        "05_backend_api_and_inference",
        "06_frontend_react_app",
        "07_testing_and_evaluation",
        "08_deployment_configuration",
        "09_hackathon_strategy_and_demo",
    ]
    for s in sections:
        spath = os.path.join(base_dir, s)
        status = "EXISTS" if os.path.isdir(spath) else "PENDING CREATION"
        print(f"  [{'+' if status == 'EXISTS' else '-'}] {s:<42} : {status}")

def main():
    print("=" * 65)
    print(" Academic Stress & Student Feedback NLP System - Setup Check")
    print("=" * 65)
    check_python_version()
    deps_ok = check_dependencies()
    verify_sections()
    print("=" * 65)
    if deps_ok:
        print("[+] All critical dependencies are verified and ready!")
    else:
        print("[-] Some dependencies are missing. Run: pip install -r requirements.txt")
    print("=" * 65)

if __name__ == "__main__":
    main()
