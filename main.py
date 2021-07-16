import discord
from discord.ext import commands,tasks
import random
from itertools import cycle

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print('o bot tá on ')
    change_status.start()
	
#|Status|#

bot_status = cycle(['Vai se fuder adm ', 'Programando em Python', 'Ela partiu bixo ,tô só a tristeza','vai se fuder serj ',
'siga o meu criador no twitter imediatamente (@Henrique_clebs)'])

@tasks.loop(seconds=300)
async def change_status():
    await client.change_presence(activity=discord.Game(next(bot_status)))

####################################################################################################


@bot.event
async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('Ola'):
            await message.channel.send('ola ')
        if message.content.startswith('bom dia'):
            await message.channel.send('bom dia amigo')
        if message.content.startswith('fds?'):
            await message.channel.send('obrigado amigo')
        if message.content.startswith('sergio viadão'):
            await message.channel.send('bom dia amigo')
        if message.content.startswith('clebsom '):
            await message.channel.send('verdade')
        if message.content.startswith('adeus'):
            await message.channel.send('obrigado amigo')
        if message.content.endswith(' ?'):
           
            await message.channel.send(resposta)     
        if message.content.startswith('oi'):
            await message.channel.send('bom dia gasosa')
        if message.content.startswith('bom dia'):
            await message.channel.send('olá')
        
    async def on_message(self, message):
        if message.author.id == self.user.id:
                return

        if message.content.startswith('bodia'):
            await message.reply('bodia', mention_author=True)
        if message.content.startswith('olaá'):
            await message.reply('olá', mention_author=True)
    

#######################################################################################################


client = MyClient()
client.run('token')





























































