import discord.py
from discord.ext import commands

client=commands.Bot(command_prefix='!')

@client.event
async def on_ready():
	print('seu bot esta online') 		
    change_status.start()
	
#|Status|#

bot_status = cycle(['status da sua escolha '])

@tasks.loop(seconds=15)
async def change_status():
    await client.change_presence(activity=discord.Game(next(bot_status)))#script lara status do bot 
    
'''bloco de codigo que detecta quando um membro entra na guild(servidor) e envia uma mensagem'''
	
@client.event
async def on_member_join(member):
	await ctx.send('Seja bem vindo {}'.format(member))
	
#################################
@client.command()
async def '''nome do comando e o que ele deve fazer ''' (ctx):
	#script do comando
	
	
	
	
client.run('token')
	
