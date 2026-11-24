@echo off
cd /d "%~dp0"
echo Installing packages...
pip install -r requirements.txt
echo.
echo Starting server... Open http://localhost:8000 in your browser.
echo Do NOT close this window while downloading.
python server.py
pause
