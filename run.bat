@echo off

REM Activate venv
call .venv\Scripts\activate.bat

REM Run pytest with HTML report
REM pytest -v -s --html=Reports\report.html --self-contained-html testCases\Test_Login.py --browser Chrome
pytest -v -s --html=Reports\DataDriven_report.html testCases/DataDriven_TestLogin.py --browser Chrome

pause
