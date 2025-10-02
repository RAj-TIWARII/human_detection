@echo off
echo ========================================
echo Person Detection System - Installation
echo ========================================
echo.

REM Check Python installation
echo [1/5] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH!
    echo Please install Python 3.11 or 3.12 from python.org
    pause
    exit /b 1
)

REM Display Python version
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYVER=%%i
echo Found Python version: %PYVER%

REM Check if Python 3.13
echo %PYVER% | findstr /C:"3.13" >nul
if not errorlevel 1 (
    echo.
    echo WARNING: Python 3.13 detected!
    echo Python 3.13 is too new and may cause compatibility issues.
    echo Recommended: Python 3.11 or 3.12
    echo.
    echo Do you want to continue anyway? (Y/N)
    set /p continue=
    if /i not "%continue%"=="Y" exit /b 1
)

echo.
echo [2/5] Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo ERROR: Failed to create virtual environment!
    pause
    exit /b 1
)
echo Virtual environment created successfully!

echo.
echo [3/5] Activating virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment!
    pause
    exit /b 1
)

echo.
echo [4/5] Upgrading pip...
python -m pip install --upgrade pip

echo.
echo [5/5] Installing required packages...
echo This may take a few minutes...
pip install opencv-python numpy pillow
if errorlevel 1 (
    echo ERROR: Failed to install packages!
    echo Try running: pip install opencv-python numpy pillow
    pause
    exit /b 1
)

echo.
echo ========================================
echo Installation completed successfully! 
echo ========================================
echo.
echo To run the application:
echo   1. Activate environment: venv\Scripts\activate
echo   2. Run: python main.py
echo.
echo Or simply double-click: run.bat
echo.
pause