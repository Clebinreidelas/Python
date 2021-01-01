import sys
a=1
while a > 0:
 	cpf=input('Digute aqui o seu cpf :\n')
 	a=len(cpf)
 	if a == 14:
 		print('Seu cpf é válido')
 		break
 	if a != 14:
 		print('Seu cpf não é válido,\ndigite novamente por favor\n ')
 	