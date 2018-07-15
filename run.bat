@echo off
set botname=RAGE 
set project=main.py

set title=title %botname% - Python
:loop
color e
%title% 
cls
echo Iniciando Bot... (Para sair feche a janela)
echo.
python %project%
echo.
color 4e
echo ERRO CRITICO!! 
echo Informacoes acima  
echo.
echo Pressione qualquer tecla para tentar novamente
pause>nul 
goto loop 

