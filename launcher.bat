rem On lance d'abord debut

@echo off
python.exe "debut.py"
call compilator.bat
python.exe "executable_asy.py"
taskkill /f /im AcroRd32.exe

rem Ensuite, on boucle sur executable_asy jusqu'à ce qu'un fichier fin.txt soit créé, ce qui ne se produit que si l'utilisateur
rem entre la commande quit 

:loop
@echo off
call compilator.bat
python.exe "executable_asy.py"
@taskkill /f /im AcroRd32.exe
If exist fin.txt goto fin
If not exist fin goto loop

rem On supprime ensuite les fichiers provisoires créés par le programme

:fin
del stockvar.txt
del fin.txt
call renommer.bat
del renommer.bat