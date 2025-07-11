# use .\auto_push.bat to run this script
# --- IGNORE ---
# this script automatically stages, commits, and pushes changes to the repository.
# --- IGNORE ---


@echo off
git add .
git commit -m "Auto-update: %date% %time%"
git push
pause
