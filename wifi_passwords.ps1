$wifiProfiles = netsh wlan show profiles | Select-String "All User Profile" | ForEach-Object { $_.ToString().Trim().Split(":")[1] }
foreach ($profile in $wifiProfiles) {
    $newProfile = $profile.Trim()
    $password = (netsh wlan show profile name=$newProfile key=clear | Select-String "Key Content").ToString().Trim().Split(":")[1]
    Write-Host "SSID: $newProfile" -ForegroundColor Green
    Write-Host "Password: $password" -ForegroundColor Green
    Write-Host ""
}
