
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def Hola(ctx):
    await ctx.send(f'Hola. este bot esta hecho para que aprendas sobre contaminacion en tu cas y como reducirla')
    with open('Saludo.png', 'rb') as s:
        
        picture1 = discord.File(s)
    
    await ctx.send(file=picture1)
    
@bot.command()
async def Como_Reciclar(ctx):
    await ctx.send("Para reciclar mas facil te recomiendo separar la basura en montones.Por ejemplo:Plastico,Vidrio,Carton y Papel")
    with open('Reciclaje.jpg', 'rb') as r:
        
        picture2 = discord.File(r)
    
    await ctx.send(file=picture2)

@bot.command()
async def Comida(ctx):
    await ctx.send(f"Con la comida puedes guardarla por ejemplo para la cena.No botarla.Si no quieres comerla fria puedes tambien calentarla")
    
@bot.command()
async def Basura_Normal(ctx):
    await ctx.send("Con esa la puedes tirar pero aqui van unos consejos de como minimizarla:Primero no compres cosas que no vas a usar ")
@bot.command()
async def Video(ctx):
    await ctx.send("https://youtu.be/g-GJ3vvOpbQ")
@bot.command()
async def Dispositivos_Electronicos(ctx):
    await ctx.send("Con los dispositivos eletronicos tu puedes reciclarlos para que se combiertan en otras cosas :)")

@bot.command()
async def Pilas(ctx):
    await ctx.send("Con las pilas puedes guardarlas en una caja y despues depositarlas al contenedor de reciclaje de pilas")
@bot.command()
async def Chao(ctx):
    await ctx.send("Adios.Gracias .Que te alla servido.:) ")
     
    with open('Chao.jpg', 'rb') as c:
       
        picture3 = discord.File(c)
   
    await ctx.send(file=picture3)

bot.run("")
