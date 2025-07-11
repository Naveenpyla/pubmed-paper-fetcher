@echo off
cd /d C:\Users\navee\OneDrive\Desktop\biotech
C:\Users\navee\AppData\Roaming\Python\Scripts\poetry run get-papers-list "pharmaceutical cancer treatment" -f pharma_papers.csv
echo.
echo ✅ Done! Results saved to pharma_papers.csv
pause
