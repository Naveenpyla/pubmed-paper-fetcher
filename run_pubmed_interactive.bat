@echo off
set /p query=Enter your PubMed search query:
set /p filename=Enter filename to save results (e.g., cancer.csv):
cd /d C:\Users\navee\OneDrive\Desktop\biotech
C:\Users\navee\AppData\Roaming\Python\Scripts\poetry run get-papers-list "%query%" -f %filename%
echo.
echo ✅ Done! Results saved to %filename%
pause
