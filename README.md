# automacaojornadapy
automação de tarefas

Acesso a base de dados.csv com biblioteca pandas
(para instalar: pip install pandas)
 import pandas as pd

 tabela = pd.read_csv ("nomedoarquivo.csv") #declarada tabela com aquivo selecionado. 

 if not pd.isna():  #tratamento para celula vazia

controle de tempo e execução com biblioteca time
 import time

 time.sleep()
 time.PAUSE =


login em site, cadastro de produtos, tabulação
funções de entrada
(para instalar: pip install pyautogui)
 import pyautogui

 pyautogui.click(x= , y= )
 pyautogui.write("")
 pyautogui.press("")
 pyautogui.hotkey("")
 pyautogui.scroll(1000)

 laço de repetição for

 for linha in Tabela.index:
    codigo = Tabela.loc[linha,"codigo"]
    pyautogui.write(str(codigo))


bot auxiliar para posição x,y em pyautogui.click():
import time
import pyautogui
time.sleep(5)
print(pyautogui.position())

