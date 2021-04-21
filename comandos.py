import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='.', intents=intents)


@bot.command()
async def say(ctx,arg):
    await ctx.send(arg)


@bot.command()
async def soma(ctx , num1 : int, num2 : int):
    await ctx.send(num1 + num2)


@bot.command()
async def mdb(ctx:int):
    beleza = random.choice(1,100)
    if beleza == 100:
        await ctx.send('vc tem {} de beleza , o que te torna lindo pra carai '.format(beleza))
    if beleza < 10 : 
        await ctx.send('vc tem {} de beleza o que te torna feio pra disgraça lklklklklk'.format(beleza))
    if beleza < 40 > 10 :
        await ctx.send('vc tem {} de beleza o que te torna mais ou menos , entt namore cmg imediatamente '.format(beleza))
    if beleza > 80 : 
        await ctz.send('vc tem {} de beleza o que te torna lindo pra carai , tá quase no meu nivel '.format(beleza))
    if beleza > 50 < 80:
        await ctx.send('vc é bonito pq tem {} de beleza e é só isso seu baitola'.format(beleza))
    print('%mdb funcionando')



@bot.command()
async def mdf(ctx:int):
    feiura= random.choice(0,100)
    beleza = feiura - 100
    if feiura == 100:
        await ctx.send('vc tem {}% de feiura , o que te torna um clebsom , indiretamente vc tem {}% de beleza '.format(feiura,beleza))
    if feiura < 10:
        await ctx.send('vc tem {}% de feiura , o que é impossivel , logo vc tem {}% de beleza'.format(feiura,beleza))
    if feiura < 40 > 10 :
        await ctx.send('vc tem {}% de feiura , o que te torna meio termo , ou seja n precisa saber sua beleza'.format(feiura))
    if feiura > 80 :
        await ctx.send('vc tem {}% de feiura , o que torna horrivel , quase a nivel serj')
    if feiura > 50 < 80:
        await ctx.send('vc tem {}% de feiura , o que te torna gatinho uiuiuiiuii , e {}% de beleza'.format(feiura,beleza))
    print('%mdf funcionando')


#_________ajuda______#
@bot.command()
async def ajuda(ctx:str):
    print('%ajuda funcionando')
    await ctx.send('Olá sou um bot bem viadão pra discord,\nmeu nome é goku corinthians( ou goku pros mais intímos), gosto muito de dar a bunda e meu voto sempre vai ser do bozo a menos que ele tenha um filho com o lula-chan\ndesculpe pelos erros ortograficos e erros de programação,\né que meio que meu dono me fez ao som de gorillaz( puta banda bosta meu deus),\nbem é isso , essa é minha apresentação e fds os termos de uso do discord\nabaixo vão alguns dos neus comandos\n"%mdf":com esse comando vc pode ver o  quão feio vc é\n##como usar:##\n"%mdf"\n%mdb:com esse comando vc pode ver quão lindo(a) vc é\n##como usar:##\n"%mdb"\n"%soun":com esse comando vc terá uma resposta com sim ou não sobre aquela pergunta que vc quer fazer a sua mãe mas ela com certeza n sabe o que responder pq está mto ocupada ouvindo raça negra\n##como usar:##\n"%soun" (pergunta(sem a interrogação por conta da resposta automatica))\n"%dado":com esse comando vc poderá usar um dado virtual , caso seu amigo não tenha dado em casa(só na rua)\n##como usar:##\n"%dado"\n')
    print('%ajuda funcionando')



#_________dado_______#
@bot.command()
async def dado(ctx:int):
    dado= random.choice(1,6)
    await ctx.send(' o numero sorteado foi o numero `{}` '.fomat(dado))
    print('%dado funcionando')

#___________soun______________#

@bot.command()
async def soun(ctx):
    resposta=random.choice('eu acho que ', 'com certeza ','talvez ')
    son=random.choice('sim ', 'não')
    await ctx.send('{}{}'.format(resposta,son))
    print('%soun funcionando')

#___________userinfo_____________#
@bot.command()
async def userinfo(ctx: commands.Context, user: discord.User):
    user_id = user.id
    username = user.name
    avatar  = avatar.user.url
    await ctx.send(' baitola ai: {} -- {}\n{}'.format(user_id, username, avatar))

#_________avatar_________#
@bot.command()
async def avatar(ctx: commands.Context , user : discord.User):
    avatar = avatar.user.url
    await ctx.send('{}'.format(avatar))






    



















client.run('NzQ2MDk2MzQyNTE4MDcxMzY2.Xz7WXQ.tz3YIIyQz5gFZXXnmL2q-LdB1MA')
print('cliente funcionando')

