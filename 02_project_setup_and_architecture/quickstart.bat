@echo off
title Academic Stress Detection System - Quickstart
color 0B
echo ======================================================================
echo   Academic Stress & Student Feedback NLP Intelligence Platform
echo ======================================================================
echo.
echo [1/4] Checking Python Environment...
python 02_project_setup_and_architecture\setup_project.py
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Environment check failed. Installing dependencies...
    pip install -r 02_project_setup_and_architecture\requirements.txt
)

echo.
echo [2/4] Verifying/Training NLP Model...
python 04_preprocessing_and_nlp_training\train.py

echo.
echo [3/4] Running Automated Test Suite...
python 07_testing_and_evaluation\run_all_tests.py

echo.
echo [4/4] Starting Web API and Dashboard Server...
echo API and Frontend will be accessible at http://127.0.0.1:8000
python 05_backend_api_and_inference\api_server.py
pause
