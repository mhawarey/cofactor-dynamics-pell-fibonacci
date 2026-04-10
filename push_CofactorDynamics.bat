@echo off
echo ============================================================
echo  CofactorDynamics-Pell-Fibonacci
echo ============================================================

echo Pushing to GitHub...
cd /d "C:\Github\CofactorDynamics-Pell-Fibonacci"
git init
git add .
git commit -m "Supplementary verification code for cofactor dynamics and Pell equations in GCD-Fibonacci recurrences"
git branch -M main
gh repo create CofactorDynamics-Pell-Fibonacci --public --source=. --push --description "Verification code for: Cofactor Dynamics and Pell Equations in GCD-Augmented Fibonacci Recurrences (DOI: 10.65737/AIRMCS2026571)"

echo.
echo DONE — https://github.com/mhawarey/CofactorDynamics-Pell-Fibonacci
pause
