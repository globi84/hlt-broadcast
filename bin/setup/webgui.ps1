$Env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

pip install -r "$PSScriptRoot\..\webgui\requirements.txt"
