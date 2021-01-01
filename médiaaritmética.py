def média2():
	nota1=int(input('Digute a nota:'))
	nota2=int(input('Digute a nota:'))
	média=(nota1+nota2)
	md=(média/2)
	print('A media aritmética é {}'.format(md))

	
def média3():
	nota1=int(input('Digute a nota:'))
	nota2=int(input('Digute a nota:'))
	nota3=int(input('Digute a nota:'))	
	média=(nota1+nota2+nota3)
	md=(média/3)
	print('a média aritmética é {}'.format(md))


def média4():
	nota1=int(input('Digute a nota:'))
	nota2=int(input('Digute a nota:'))
	nota3=int(input('Digute a nota:'))
	nota4=int(input('Digute a nota:'))
	média=(nota1+nota2+nota3+nota4)
	md=(média/4)
	print('A media aritmética é {}'.format(md))




print('-----Programa de medição de médias aritméticas------')
a=1
import sys
while a > 0:
	
	
	definit=int(input('Qual a quantidade de média você vai usar?\n:'))
	

	
	if definit == 2:
		média2()
	if definit==3:
		média3()
	if definit==4:
		média4()
		
		
		
#eu acabei não usando o while por que esqueci
	
	

	