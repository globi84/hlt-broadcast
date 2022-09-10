@echo off
set pfad=%~dp0
del "%pfad%\..\..\Lieder\*" /Q
call  python "%pfad%\hlt-broadcast.py" %*
