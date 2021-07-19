import discord 
import os
from itertools import cycle
from discord import commands, tasks


client = commands.Bot(command_prefix = '!', help_command = None)


@client.event
async def on_ready():
  print(f'{client.user} está on')
  


# comando para exportar comandos de uma determinada categoria 
@client.command()
async def load (ctx, extension):
  if ctx.author.id == owner.id :



@client.command()
async def unload(ctx, extension):
  if ctx.author.id == owner.id :
    
@client.command()
async def reload(ctx, extension):
  if ctx.author.id == owner.id :

