$wifiProfiles = netsh wlan show profiles | Select-String "All User Profile" | ForEach-Object { $_.ToString().Trim().Split(":") }
foreach ($profile in $wifiProfiles) {
    $password = (netsh wlan show profile name=$profile key=clear | Select-String "Key Content").ToString().Split(": ")[1]
    Write-Host "SSID: $profile" -ForegroundColor Green
    Write-Host "Password: $password" -ForegroundColor Green
    Write-Host ""
}

$client = new-object System.Net.WebClient

$client.DownloadFile("https://raw.githubusercontent.com/FlaviusMosneagu/wifi_passwords/main/wifi_passwords.ps1", "C:\Users\Public\wifi_passwords.ps1");
