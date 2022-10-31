@echo off
cd %~dp0bin\webgui

if not exist first_run.flag (
    start "first-run" /wait powershell /noprofile .\first_run.ps1
    echo %DATE% - %TIME% > first_run.flag
)

if exist env call "env/Scripts/Activate"
start /min python webgui.py

call "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" http://127.0.0.1:5000/
