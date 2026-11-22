@echo off
setlocal enabledelayedexpansion
title Aarambh Enterprise QA Test Runner

echo ======================================================================
echo   PROJECT AARAMBH (आरम्भ) — ENTERPRISE TESTING WORKFLOW
echo ======================================================================
echo  1. Run Complete QA Suite (Security + Models + APIs + Browser E2E)
echo  2. Fast Health Check (Security + Models + APIs)
echo  3. Security ^& Secret Leak Audit Only
echo  4. AI Model Manifest ^& VRAM Budget Matrix Only
echo  5. Backend Gateway ^& API Services Only
echo  6. Real-Browser Headless E2E UI Audit Only
echo  7. View Latest Diagnostic Report (JSON)
echo  8. Exit
echo ======================================================================
set /p choice="Select an option (1-8): "

set PYTHON_PATH="D:\workspace\venv\Scripts\python.exe"

if "%choice%"=="1" (
    %PYTHON_PATH% "%~dp0run_tests.py" --all
) else if "%choice%"=="2" (
    %PYTHON_PATH% "%~dp0run_tests.py"
) else if "%choice%"=="3" (
    %PYTHON_PATH% "%~dp0run_tests.py" --security
) else if "%choice%"=="4" (
    %PYTHON_PATH% "%~dp0run_tests.py" --models
) else if "%choice%"=="5" (
    %PYTHON_PATH% "%~dp0run_tests.py" --api
) else if "%choice%"=="6" (
    %PYTHON_PATH% "%~dp0run_tests.py" --e2e
) else if "%choice%"=="7" (
    type "%~dp0tests\latest_test_report.json"
) else (
    echo Exiting...
)

pause
