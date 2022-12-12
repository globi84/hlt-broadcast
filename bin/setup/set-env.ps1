param(
    $path
)

[System.Environment]::SetEnvironmentVariable('hlt-broadcast-root',$path,[System.EnvironmentVariableTarget]::User)
