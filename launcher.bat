@echo off
echo [40;32mInstalling Requirements For You....[40;37m
echo.
pip install --upgrade -r requirements.txt
echo.
echo [40;32mLaunching Thunder Builder..[40;37m
timeout 2 >nul
python builder.py