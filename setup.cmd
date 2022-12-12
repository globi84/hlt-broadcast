@echo off

net session

if %ERRORLEVEL% 0 (
    winget install OBSProject.OBSStudio
    winget install Zoom.Zoom
    winget install Python.Python.3.11

    echo Install macrodeck from hand
    start "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" https://macrodeck.org/download
    echo press anykey when it is done
    pause



) ELSE (
    echo run as admin
)
