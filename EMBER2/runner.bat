@echo off
setlocal enabledelayedexpansion

REM Define the input CSV file
set "input_csv=new.csv"  REM Replace with your actual CSV file path

REM Create an output directory if it doesn't exist
if not exist output (
    mkdir output
)

REM Read the CSV file line by line
for /f "tokens=2,3 delims=," %%a in (%input_csv%) do (
    REM Skip the header row
    if /i not "%%a"=="Gene" (
        REM Debugging output
        echo Processing gene: %%a
        REM Call the Python script with the extracted values
        python predict.py -i "%%b" -o "output\%%a"
        echo Processing done gene: %%a
    )
)

endlocal
