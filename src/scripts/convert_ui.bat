@echo off

cd src\gui

for %%f in (*.ui) do (
  pyside6-uic %%~nf.ui -o %%~nf.py
)

cd dialog\interface
for %%f in (*.ui) do (
  pyside6-uic %%~nf.ui -o %%~nf.py
)