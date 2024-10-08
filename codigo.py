
# https://dlp.hashtagtreinamentos.com/python/intensivao/login
# login
# importar a base de dados
# cadastrar 1 produto
# repetir o processo
#biblioteca pyautogui 
'''pyautogui.write
   pyautogui.click
   pyautogui.press
   pyautogui.hotkey
   pyautogui.PAUSE
   pyautogui.scrol(5000)
   
   tabela = pandas.read(csv)'''
import pandas as pd
import pyautogui
import time

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")

pyautogui.click(x=970, y=622)

time.sleep(3)

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(4)


#repetição

pyautogui.click(x=1855, y=51)

pyautogui.click(x=885, y=510)
pyautogui.write("cecelzinho@gmail.com")
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.press("tab")
pyautogui.press("enter")


#banco de dados comm pandas
Tabela = pd.read_csv("produtos.csv")
#print(Tabela)


#codigo
#marca
#tipo

#categoria
#preço unitário
#custo
#obs



# para cada linha na minha tabela.index 

for linha in Tabela.index:

    
    pyautogui.click(x=645, y=363)

    codigo = Tabela.loc[linha,"codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    marca = Tabela.loc[linha,"marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    tipo = Tabela.loc[linha,"tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    categoria = Tabela.loc[linha,"categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    preco_unitario = Tabela.loc[linha,"preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    custo = Tabela.loc[linha,"custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    obs = Tabela.loc[linha,"obs"]
    if not pd.isna(obs):   
        pyautogui.write(str(obs))
    pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.scroll(5000)




