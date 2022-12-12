New-NetFirewallRule -DisplayName "Macro Deck 2" `
    -Enabled True `
    -Profile Any `
    -Direction Inbound `
    -Action Allow `
    -Protocol UDP `
    -Program "C:\program files\macro deck\macro deck 2.exe"

New-NetFirewallRule -DisplayName "Macro Deck 2" `
    -Enabled True `
    -Profile Any `
    -Direction Inbound `
    -Action Allow `
    -Protocol TCP `
    -Program "C:\program files\macro deck\macro deck 2.exe"

New-NetFirewallRule -DisplayName "OBS Studio" `
    -Enabled True `
    -Profile Any `
    -Direction Inbound `
    -Action Block `
    -Protocol UDP `
    -Program "C:\program files\obs-studio\bin\64bit\obs64.exe"

New-NetFirewallRule -DisplayName "OBS Studio" `
    -Enabled True `
    -Profile Any `
    -Direction Inbound `
    -Action Block `
    -Protocol TCP `
    -Program "C:\program files\obs-studio\bin\64bit\obs64.exe"
