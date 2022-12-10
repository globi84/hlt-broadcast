param(
    $configFile
)

if (Test-Path $configFile){
    $config = (Get-Content $configFile | ConvertFrom-Json).webgui

    foreach ($app in $config.apps){
        if ($app.name -notlike "msedge*"){
            Get-Process $app.name.replace('.exe','') -ErrorAction Ignore | Stop-Process -Force -Confirm:$false -ErrorAction Ignore
        }

        $file = ($app.path +"\" + $app.name)
        $work = ($app.path)
        $file
        if($app.args){
            Start-Process -FilePath $file -WorkingDirectory $work -ArgumentList $app.args
        }else{
            Start-Process -FilePath $file -WorkingDirectory $work
        }
    }
}
