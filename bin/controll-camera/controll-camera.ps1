param(
    [Parameter(Mandatory)]
    [ValidateScript(
        {
            $config = (Get-Content "$PSScriptRoot\..\..\config.json" | ConvertFrom-Json).controllCamera
            $_ -in ($config.positions | Get-Member -MemberType NoteProperty | Select-Object -ExpandProperty Name)
        }
        )]
    [ArgumentCompleter(
        {
            param($cmd, $param, $wordToComplete)
            $config = (Get-Content "$PSScriptRoot\..\..\config.json"| ConvertFrom-Json).controllCamera
            [array] $validValues = ($config.positions | Get-Member -MemberType NoteProperty | Select-Object -ExpandProperty Name)
            $validValues -like "$wordToComplete*"
        }
    )]
    [string]$position = ""
)

$configFile = "$PSScriptRoot\..\..\config.json"

function Connect-Atem {
    param (
        [string]$atemSwitcherIP
    )
    $Global:atem = New-Object SwitcherLib.Switcher($atemSwitcherIP)
    $atem.Connect()
    $MEs = $atem.getmes()
    $me1 = $MEs[0]
    return $me1
}

function Move-Camera {
    param(
        [string]$cameraIP,
        [int]$position
    )
    $port = 1259
    [byte[]]$command = 0x81, 0x01, 0x04, 0x3F, 0x02, $position, 0xFF

    $udpClient = New-Object System.Net.Sockets.UdpClient(50000)

    $udpClient.Connect($cameraIP, $port)
    $udpClient.Send($command, $command.Length)
    $udpClient.Close()
}

if (Test-Path $configFile) {
    Add-Type -Path "$PSScriptRoot\lib\SwitcherLib.dll"
    $config = (Get-Content $configFile | ConvertFrom-Json).controllCamera

    # load config
    $camera         = $config.positions.($position).camera
    $cameraIP       = $config.cam.($camera.tostring())
    $cameraDirect   = $config.positions.($position).direct
    $atemSwitcherIP = $config.atemSwitcher
    $cameraPosition = $config.positions.($position).pos

    # connect to atem switcher
    $atemSwitcher = Connect-Atem $atemSwitcherIP


    if ($camera -eq $atemSwitcher.Program -and -not $cameraDirect){
        $keys = $config.cam | Get-Member -MemberType NoteProperty | Select-Object -ExpandProperty Name
        $tempCam = $keys | Where-Object {$_ -ne $camera}
        $tempCamIP = $config.cam.($tempCam.tostring())

        Move-Camera $tempCamIP 1

        Start-Sleep -Milliseconds 1500
        $atemSwitcher.Program = $tempCam
        Move-Camera $cameraIP $cameraPosition
        Start-Sleep 7
    }

    Move-Camera $cameraIP $cameraPosition
    Start-Sleep -Milliseconds 1500

    $atemSwitcher.Program = $camera

}
else {
    Write-Host "no config file found: $configFile"
}
