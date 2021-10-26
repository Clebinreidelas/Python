import datetime
import tkinter
from tkinter import *
from tkinter import ttk
from datetime import *
import sqlite3


#criando o banco de dados

bdd= sqlite3.connect("Agenda.db")
cursor= bdd.cursor()
cursor.execute("CREATE TABLE agendamentos (nome_usuario text , agendamentos text )")


#funções muito legais e uteis(que eu adicionarei depois já que agora eu to com preguiça  e tbm pq  n sei dar um input nisso dggbvfbhfghfbvdfhvfhgvdfvbhdfghfdbfgvbdfhyfvhbfjgvyf legal)
def agendamentos():
    cursor.execute("INSERT INTO agendamentos (agendamentos) VALUES (?)", agenda)

    
def amanhã():
    teste = datetime.now()
    tomorrow = teste.day + 1
    if tomorrow > 32 :
        pass
    else : 
        amnha = f'''
        Amanhã = {tomorrow}
        '''
               


    data_amanhã["text"] = tomorrow

    

def calendario():
    hora_data_TOTAL = datetime.now()
    texto = f'''
    data = {hora_data_TOTAL.day}/{hora_data_TOTAL.month}/{hora_data_TOTAL.year}
    hora = {hora_data_TOTAL.hour}:{hora_data_TOTAL.minute}:{hora_data_TOTAL.second}
    '''

    data_exibir["text"] = texto






    

janela = Tk()
janela.title("Calendario do cleb")
janela.geometry("380x200")

#coisas que aparecem na tela
#texto de boas-vindas
texto_1 = Label(janela, text= "Seja bem vindo ao calendario incrivel que o cleb montou para vc")
texto_1.grid(column=0, row=0)

#botão para mostrar o dia 

botão = Button(janela, text= "Clique aqui para ver a data de hoje" , command=calendario)
botão.grid(column=0, row=1)

#exibição do que o botão vai mostrar

data_exibir= Label(janela, text="")
data_exibir.grid(column=0, row=2)

#botão pra mostrar a data de amanhã

botão_amanha= Button(janela , text="Amanhã", command=amanhã)
botão_amanha.grid(column=1, row=1)

#exibição da data de amanhã

data_amanhã = Label(janela, text= "")
data_amanhã.grid(column=1, row=2)

#função pra agendar algum evento


'''
botão_agenda= Button(janela, text="Clique aqui se quiser agendar algo de importante", command= agendamentos )
botão_agenda.grid(column=2 , row=2)
'''

janela.mainloop()




    










