@echo off

REM Activate the virtual environment
call venv\Scripts\activate

REM Run the main.py script using Python
python main.py

REM Deactivate the virtual environment
deactivate
