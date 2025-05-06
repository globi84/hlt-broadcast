@echo off

set root=%~dp0
net session > nul

if %ERRORLEVEL% == 0 (

    echo ######################
    echo #
    echo # Install prereqisits
    echo #
    echo ######################
    timeout 2

    winget install OBSProject.OBSStudio
    winget install Zoom.Zoom
    winget install Python.Python.3.12
    winget install MacroDeck.MacroDeck

    echo ######################
    echo #
    echo # Copy Appconfig
    echo #
    echo ######################
    timeout 2

    xcopy "%ROOT%obs-studio" "%APPDATA%\obs-studio" /E /C /H /I /R /Y
    xcopy "%ROOT%Macro Deck" "%APPDATA%\Macro Deck" /E /C /H /I /R /Y
    copy "%ROOT%config.json.skel" "%ROOT%config.json" /Y

    echo ##################################
    echo #
    echo # Custom Config
    echo #
    echo ##################################
    timeout 2

    powershell -NoProfile "Set-ExecutionPolicy RemoteSigned"
    powershell -NoProfile "%ROOT%bin/setup/create_speaker.ps1"
    powershell -NoProfile "%ROOT%bin/setup/webgui.ps1"
    powershell -NoProfile "%ROOT%bin/setup/firewall.ps1"
    powershell -NoProfile "%ROOT%bin/setup/set-env.ps1" %ROOT%

    echo ################################################
    echo #
    echo # TO DO's:
    echo # * Edit config.json
    echo # * check OBS Paths to media
    echo # * check path in macrodeck macros
    echo # * set password for obs-plugin in macrodeck
    echo #
    echo ################################################

    pause
    exit /b
) ELSE (
    echo run as admin
    pause
    exit /b
)
