@ECHO OFF

set loop=0
:loop

rem adb shell service list > ServicesResult.txt 2>&1
adb shell ps -A > ServicesResult.txt 2>&1

set /a loop=%loop%+1 
if "%loop%"=="1" goto next
goto loop

:next
echo done!