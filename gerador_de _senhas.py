from cProfile import label
from cgitb import text
import random
import tkinter 
from tkinter import *



#_Importação de modulos_#

janela = Tk()
janela.geometry("600x400")
conteiner_1 = Frame(janela)
conteiner_1.pack()



#_janelas e conteiners_#

def senha_aleatoria():
    el_1 = random.choice(["A","B", "C","D","E","F","1","2", "3","4","5","a","b", "c", "d", "e"])
    el_2 = random.choice(["A","B", "C","D","E","F","1","2", "3","4","5","a","b", "c", "d", "e"])
    el_3 = random.choice(["A","B", "C","D","E","F","1","2", "3","4","5","a","b", "c", "d", "e"])
    el_4 = random.choice(["A","B", "C","D","E","F","1","2", "3","4","5","a","b", "c", "d", "e"])
    el_5 = random.choice(["A","B", "C","D","E","F","1","2", "3","4","5","a","b", "c", "d", "e"])
    el_6 = random.choice(["A","B", "C","D","E","F","1","2", "3","4","5","a","b", "c", "d", "e"])
    el_7 = random.choice(["A","B", "C","D","E","F","1","2", "3","4","5","a","b", "c", "d", "e"])
    el_8 = random.choice(["A","B", "C","D","E","F","1","2", "3","4","5","a","b", "c", "d", "e"])
    senha_final = (f"{el_1}{el_2}{el_3}{el_4}{el_5}{el_6}{el_7}{el_8}")
    senha["text"]=senha_final

text1 = Label(conteiner_1, text="Clique abaixo para obter a sua senha ")
text1.pack()

botão = Button(conteiner_1, text="Senha aleatoria", command=senha_aleatoria)
botão.pack()

senha = Label(conteiner_1, text="")
senha.pack()





janela.mainloop()


