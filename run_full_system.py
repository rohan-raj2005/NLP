"""
run_full_system.py - Master Full-System Orchestrator
Executes the entire end-to-end pipeline:
1. Environment Check & Directory Verification
2. Dataset Generation (CSV downloads)
3. Exploratory Data Analysis (EDA)
4. Preprocessing & NLP Model Training
5. Automated Test Suite Execution
6. Starts the Production Web API & Interactive Dashboard
"""

import os
import sys
import subprocess
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def run_step(step_num, title, script_rel_path, args=None):
    print("\n" + "=" * 75)
    print(f" [{step_num}/6] {title}")
    print("=" * 75)
    script_path = os.path.join(BASE_DIR, script_rel_path)
    cmd = [sys.executable, script_path] + (args if args else [])
    
    start = time.time()
    res = subprocess.run(cmd)
    elapsed = round(time.time() - start, 2)
    
    if res.returncode != 0:
        print(f"[-] Step {step_num} failed with return code {res.returncode}")
        return False
    print(f"[+] Step {step_num} completed successfully in {elapsed}s")
    return True

def main():
    print("*" * 75)
    print(" MindTrack AI - Full System Orchestration & Startup")
    print("*" * 75)
    
    # 1. Environment Setup
    if not run_step(1, "Checking Environment & Dependencies", "02_project_setup_and_architecture/setup_project.py"):
        sys.exit(1)
        
    # 2. Dataset Generation
    if not run_step(2, "Generating & Downloading CSV Datasets", "03_dataset_collection_and_exploration/download_datasets.py"):
        sys.exit(1)
        
    # 3. Exploratory Data Analysis
    if not run_step(3, "Running Exploratory Data Analysis (EDA)", "03_dataset_collection_and_exploration/eda.py"):
        sys.exit(1)
        
    # 4. Training Model
    if not run_step(4, "Training NLP Classifier & Persisting Artifacts", "04_preprocessing_and_nlp_training/train.py"):
        sys.exit(1)
        
    # 5. Automated Testing
    if not run_step(5, "Running Automated Test Suite & Edge Cases", "07_testing_and_evaluation/run_all_tests.py"):
        sys.exit(1)
        
    # 6. Launch Web Server & Dashboard
    print("\n" + "=" * 75)
    print(" [6/6] Launching Production REST API & Interactive Dashboard")
    print("=" * 75)
    print(">> Open your browser at: http://127.0.0.1:8000")
    print(">> Press Ctrl+C to terminate the server.\n")
    
    server_path = os.path.join(BASE_DIR, "05_backend_api_and_inference/api_server.py")
    subprocess.run([sys.executable, server_path])

if __name__ == "__main__":
    main()
