@echo off

net session 2> nul

if %ERRORLEVEL% == 0 (
    SET root=%~dp0
    echo ######################
    echo #
    echo # Install prereqisits
    echo #
    echo ######################
    timeout 2

    winget install OBSProject.OBSStudio
    winget install Zoom.Zoom
    winget install Python.Python.3.11

    echo ###################################################
    echo #
    echo # Install macrodeck from hand and do NOT start it
    echo #
    echo ###################################################
    timeout 10

    start "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" https://macrodeck.org/download
    echo press anykey when it is done
    pause

    echo ######################
    echo #
    echo # Copy Appconfig
    echo #
    echo ######################
    timeout 2

    xcopy "%root%\obs-studio" "%APPDATA%\obs-studio" /E /C /H /I /R /Y
    xcopy "%root%\Macro Deck" "%APPDATA%\Macro Deck" /E /C /H /I /R /Y

    echo ##################################
    echo #
    echo # Create Folder and config webgui
    echo #
    echo ##################################
    timeout 2

    powershell -NoProfile "Set-ExecutionPolicy RemoteSigned"
    powershell -NoProfile "bin/setup/setup.ps1"

) ELSE (
    echo run as admin
)
