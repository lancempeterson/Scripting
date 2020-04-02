@ECHO OFF

set loop=0
:loop

adb shell input tap 300 400 
timeout 5
adb shell input tap 50 700 
timeout 10
adb shell input tap 600 200
timeout 10
adb shell input tap 0 0 
timeout 5
adb shell input tap 750 200 
timeout 10
adb shell input tap 0 0 
timeout 5
adb shell input tap 1350 700 
timeout 5
adb shell input tap 1350 650 
timeout 5
adb shell input tap 0 0 
timeout 10

set /a loop=%loop%+1 
if "%loop%"=="50" goto next
goto loop

:next
echo done!
