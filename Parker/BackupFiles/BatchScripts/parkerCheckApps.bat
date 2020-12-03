@ECHO OFF

set loop=0
:loop

adb shell input tap 20 500
adb shell input tap 20 500
adb shell screencap -p /sdcard/currentApps.png
timeout 4
adb pull /sdcard/currentApps.png 

set /a loop=%loop%+1 
if "%loop%"=="1" goto next
goto loop

:next
echo done!