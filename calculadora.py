##############
import sys 
def subtração():
	s=int(input('digite um numero\n:'))
	sla=int(input('digite um numero para subtrair \n:'))
	res=s - sla
	print('o resultado da subtração é {}'.format(res))
	
	
def multiplicação():
	s=int(input('digite um numero\n:'))
	sla=int(input('digite o numero que vc quer multiplicar\n :'))
	rest=s * sla 
	print('o resuotado da operação é {} '.format(rest))
	
	
def soma():
	soma=int(input('digite um numero \n:'))
	so=int(input('digite o numero que vc quer somar ao de cima\n'))
	result =soma + so
	print(' o resultado da operacão é {}'.format(result))
	
	
def divisão():
	divisao=int(input('digite um numero \n:'))
	divisor=int(input('digite o divisor\n:'))
	result=divisao / divisor
	print('o resultado da divisão é {}'.format(result))
	resto =divisao % divisor
	print(' o resto da divisão é {}'.format(resto))
	inteiro = divisao // divisor
	print('a divisão inteira é {} '.format(inteiro))
	

def potenciação():
	poten=int(input('digite a base\n:'))
	p=int(input('digite  o expoente\n:'))
	rest=poten ** p
	print('o resultado do calculo é {}'.format(rest))
	
operações=('subtração ','soma','divisão','multiplicação','potenciação','divisao')
po=input('digite o que vc quer fazer \n:')
if po == 'subtração':
	subtração()
if po == 'multiplicação':
	multiplicação()
if po == 'divisão':
	divisão()
if po == 'soma':
	soma()
if po == 'divisao':
	divisão()
if po == 'potenciação':
	potenciação()
if po != operações:
	print('digite uma operação válida!')
