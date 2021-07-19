import sqlite3

conector = sqlite3.connect('clients.db') # O banco de dados também pode ser aramazenado na memoria com ":memory"
cursor= conector.cursor()


cursor.execute("""
CREATE TABLE clients (
  Nome 
  Idade 
  Saldo
);
""")

# Criação de tabela com  as colunas "Nome" , "Idade", "Saldo"
name = input('Digite seu nome :\n')
idade= int(input('DIgite sua idade :\n')
saldo = int(input('Digite seu saldo atual :\n')
cursor.executemany(""""
INSERT INTO clients (Nome, Idade, Saldo
VALUES (?, ?, ?)
""", (name, idade, saldo))
# aqui vc está adicionando dados na tabela 'clients' , ou seja , iserindo dados no seu banco de dados 
              
              
              
