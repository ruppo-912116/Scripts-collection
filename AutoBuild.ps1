Set-Location -Path [Path_to_webapp_react]
if(Test-Path -Path '.\build'){
    Write-Output ""
    Write-Output "Removing old build file"
    Write-Output "-----------------------"
    Remove-Item .\build -Recurse
}
Write-Output ""
Write-Output "Running npm build process now...."
Write-Output "---------------------------------"
npm start
if(Test-Path -Path "..\build"){
    Remove-Item ..\build -Recurse
}
mkdir ..\build
Copy-Item .\build\* -Recurse -Destination ..\build -PassThru
