@echo off
echo ===================================
echo  Website Optimization Tool
echo ===================================

echo Step 1: Checking Python installation...
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Error: Python is not installed or not in PATH
    pause
    exit /b 1
)

echo Step 2: Installing required packages...
pip install csscompressor rjsmin

if %ERRORLEVEL% NEQ 0 (
    echo Error: Failed to install required packages
    pause
    exit /b 1
)

echo Step 3: Running optimization script...
python simple_minify.py

if %ERRORLEVEL% NEQ 0 (
    echo Error: Failed to run optimization script
    pause
    exit /b 1
)

echo.
echo ===================================
echo  Optimization completed!
echo  Please check the output above for any errors.
echo ===================================
pause
