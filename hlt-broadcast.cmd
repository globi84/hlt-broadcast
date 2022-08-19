@echo off
set pfad=%~dp0

call  "%pfad%\.venv\Scripts\python.exe" "%pfad%\hlt-broadcast.py" %*
