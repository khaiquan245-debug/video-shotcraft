@echo off
setlocal DisableDelayedExpansion
cd /d "%~dp0"
if not exist "manifest.json" goto missing
if not exist "Busy_Not_Progressing_MASTER.zip.part001" goto missing
if not exist "Busy_Not_Progressing_MASTER.zip.part002" goto missing
if not exist "Busy_Not_Progressing_MASTER.zip.part003" goto missing
echo Dang ghep va kiem tra ban master. Vui long cho...
if not exist "Busy_Not_Progressing_MASTER.zip" (
  copy /y /b "Busy_Not_Progressing_MASTER.zip.part001"+"Busy_Not_Progressing_MASTER.zip.part002"+"Busy_Not_Progressing_MASTER.zip.part003" "Busy_Not_Progressing_MASTER.zip.tmp" >nul
  if errorlevel 1 goto failed
)
powershell.exe -NoLogo -NoProfile -Command "$ErrorActionPreference='Stop'; $root=(Get-Location).Path; $m=Get-Content -LiteralPath (Join-Path $root 'manifest.json') -Raw | ConvertFrom-Json; foreach($p in $m.parts){$f=Join-Path $root $p.name; if((Get-Item -LiteralPath $f).Length -ne $p.bytes){throw ('Part size mismatch: '+$p.name)}; if((Get-FileHash -LiteralPath $f -Algorithm SHA256).Hash.ToLowerInvariant() -ne $p.sha256){throw ('Part checksum mismatch: '+$p.name)}}; $ready=Join-Path $root $m.zip_name; $z=$ready; if(-not(Test-Path -LiteralPath $z)){$z=$ready+'.tmp'}; if((Get-FileHash -LiteralPath $z -Algorithm SHA256).Hash.ToLowerInvariant() -ne $m.zip_sha256){throw 'Joined ZIP checksum mismatch'}; if($z -ne $ready){Move-Item -LiteralPath $z -Destination $ready; $z=$ready}; $dest=Join-Path $root 'Video_Master'; $existing=Join-Path $dest $m.master_name; if(Test-Path -LiteralPath $existing){if((Get-FileHash -LiteralPath $existing -Algorithm SHA256).Hash.ToLowerInvariant() -eq $m.master_sha256){Write-Host 'Existing master verified.'; Invoke-Item -LiteralPath $dest; exit 0}}; if(Test-Path -LiteralPath $dest){$dest=Join-Path $root ('Video_Master_'+(Get-Date -Format 'yyyyMMdd_HHmmss_fff'))}; Expand-Archive -LiteralPath $z -DestinationPath $dest; $video=Join-Path $dest $m.master_name; if((Get-FileHash -LiteralPath $video -Algorithm SHA256).Hash.ToLowerInvariant() -ne $m.master_sha256){throw 'MP4 checksum mismatch'}; Write-Host 'Verified original master MP4 is ready.'; Invoke-Item -LiteralPath $dest"
if errorlevel 1 goto failed
echo XONG. MP4 nam trong thu muc Video_Master vua mo.
pause
exit /b 0
:missing
echo Thieu file. Hay giai nen TOAN BO goi ZIP GitHub truoc khi chay.
pause
exit /b 1
:failed
echo Chua hoan tat. Giu nguyen cac file va xem thong bao loi o tren.
pause
exit /b 1
