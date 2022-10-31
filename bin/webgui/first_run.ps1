$configFile = "$PSScriptRoot\config.json"

$defaultSpeaker = @{
    "Bischofschaft" = @(
        "Bischof",
        "Ratgeber1",
        "Ratgeber2"
    );
    "Pfahl" = @(
        "Pfahl_Prae",
        "Pfahl_Rat_1",
        "Pfahl_Rat_2"
    );
    "Sprecher" = @(
        "1. Sprecher",
        "2. Sprecher",
        "3. Sprecher"
    )
}

if (Test-Path $configFile){
    $config = Get-Content $configFile -encoding UTF8 | ConvertFrom-Json

    if (-not (Test-Path "$PSScriptRoot\$($config.destination)")){
        mkdir "$PSScriptRoot\$($config.destination)"
    }else{
        Write-Host "$($config.destination) already exist."
    }

    foreach ($speaker in ($config.sprecher | Get-Member -MemberType NoteProperty).Name){
        if (-not (Test-Path "$PSScriptRoot\$($config.sprecher.$speaker)")){
            $Folder = "$PSScriptRoot\$($config.sprecher.$speaker)"
            mkdir $Folder -Force
            foreach ($file in $defaultSpeaker.$speaker){
                New-Item -Path "$Folder\$($file).txt" -Value "Vorname Name"
                New-Item -Path "$Folder\$($file)_info.txt" -Value $file
            }

        }else{
            Write-Host "$($config.sprecher.$speaker) already exist."
        }
    }
}else{
    Write-Error "no configfile found: $configFile"
}
