@echo off

cd src\gui\ui\main

for %%f in (*.ui) do (
  pyside6-uic %%~nf.ui -o %%~nf.py
)

@REM cd dialog\interface
@REM for %%f in (*.ui) do (
@REM   pyside6-uic %%~nf.ui -o %%~nf.py
@REM )