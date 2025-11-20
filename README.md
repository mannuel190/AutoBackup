# AutoBackup
Automatically backs up certain files/ folders in a specified location at a specified time of day using schedule.

set source_dir to the path you have items you wish to back up.
set destination_dir to the back up location.
set backup_time to the time you wish to back up items in source_dir.



@echo off
echo Updating winget sources...
winget source update

echo Installing apps...

winget install Spotify.Spotify --silent
winget install Valve.Steam --silent
winget install Discord.Discord --silent

winget install Git.Git --silent
winget install Python.Python.3 --silent
winget install GoLang.Go --silent
winget install Microsoft.VisualStudioCode --silent
winget install Docker.DockerDesktop --silent
winget install Postman.Postman --silent
winget install Hashicorp.Terraform --silent

winget install WinRAR.WinRAR --silent
winget install CPUID.HWMonitor --silent
winget install Logitech.GHUB --silent

echo Done!
pause