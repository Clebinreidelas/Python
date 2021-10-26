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
        
    #acho que fiz isso aqui tudo e ficou meio cagadao , acho que no final vou optar por uma API de datas , pq essa porcaria pea o horario da maquina
               


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
#basicamente isso aqui cria a janela , dps da um titulo super criativo  e por ultimo seta o tamanho padrão da janela 

##coisas que aparecem na tela 
#texto de boas-vindas
texto_1 = Label(janela, text= "Seja bem vindo ao calendario incrivel que o cleb montou para vc")
texto_1.grid(column=0, row=0)
#isso aqui vai mostrar a primeira informação quando vc abrir o calendario e onde ela vai ficar (é pra isso que todos os objetos "grid" servem )

#botão para mostrar o dia 

botão = Button(janela, text= "Clique aqui para ver a data de hoje" , command=calendario)
botão.grid(column=0, row=1)
# um botão que vai mostrar a data de hj 
"""
meu deus 
meu senhor 
me ajuda 
por favor 
é na escola no trabalho ou faculdade 
tô viciado 
no zap zap zap
"""
#ignore a  musica acimaakdfhdsjg rdgdnfhgyfbh

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
   '''isso aqui em cima  é um projeto de agendamentos que eu to fazendo , mas n sei se vai sair do papel , pq n faço ideia de como fazer essa bagaça funcionar , mas basicamente ele vai colocar tudo em um banco de dados
   e é isso , quando chegar a hora ele simplesmente vai te avisar que vc é pra vc se lembrar que é pra fazer algo que dfjgxbjbhfj'''
    
janela.mainloop()





''' Depois eu faço um .exe dessa bagaça e posto aqui espero que não esteja horrivel '''
''' adeus a vc que leu todo esse incrivel programa e quer me matar por ser tão burro'''




    

    









