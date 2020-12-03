@ECHO OFF

set loop=0
:loop

adb shell input tap 20 650
timeout 36
adb shell input tap 1350 700
timeout 2
adb shell input tap 1350 650 
timeout 5
adb shell input tap 0 0 
timeout 10

set /a loop=%loop%+1 
if "%loop%"=="1" goto next
goto loop

:next
echo done!
