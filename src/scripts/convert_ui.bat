@echo off

cd src\gui

for %%f in (*.ui) do (
  pyside6-uic %%~nf.ui -o %%~nf.py
)

cd dialog
for %%f in (*.ui) do (
  pyside6-uic %%~nf.ui -o %%~nf.py
)