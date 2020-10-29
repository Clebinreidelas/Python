def cadastro():
	
	name=input("Digite o seu nome:")
	

	senha = input('Digite a sua senha:')
	s=len(senha)
	 
	if s < 8:
		print('sua senha está fraca')
	while s < 8:
		senha=input('Digite a sua senha:')
		j = len(senha)
		if  j  == 8:
			print('vc foi cadastrado!   ;)\n')
		if  j > 8:
			print('vc foi cadastrado    ;)\n')
	users=(name + name)
	senhas=(senha+senha)
	
		
	
		
		
s=1
while s > 0:
	sla=input('você quer se cadastrar ou fazer login?:\n')
	if sla == 'cadastro':
		cadastro()
