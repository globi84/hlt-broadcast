@echo off
cd %~dp0bin\webgui

rem if not exist first_run.flag (
rem     start "first-run" /wait powershell /noprofile .\first_run.ps1
rem     echo %DATE% - %TIME% > first_run.flag
rem )

if exist env call "env/Scripts/Activate"
start /min python webgui.py

call "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" http://127.0.0.1:5000/
