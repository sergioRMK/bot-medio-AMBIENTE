import os ,random
import random
import discord
from discord.ext import commands
from bot_logic import gen_pass
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
img_alm = ["ayudar.jpg"]
@bot.event
async def on_ready():
    print(f'Hemos iniciado sección como {bot.user}')

@bot.command()
async def hola(ctx):
    await ctx.send(f'hola, soy un bot que ayudara a como cuidar al medio ambiente')

@bot.command()
async def tip(ctx):
    await ctx.send(f'para cuidar al medio ambiente puedes reciclar en los dintintos basureros que son para cada material en especifico')

@bot.command()
async def chao(ctx):
    await ctx.send(f'chaoo, gracias por haber confiado en mis capacidades')

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)

@bot.command()
async def adc(ctx, a: int, b: int):
    await ctx.send(a - b)
@bot.command()
async def test(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f'{len(args)} arguments: {arguments}')

@bot.command()
async def ayud(ctx):
    with open("image/ayudar.jpg", "rb") as f:

        picture = discord.File(f)
        
    await ctx.send(file=picture)
    
@bot.command()
async def ayudar(ctx):
    img_random = random.choice(img_alm) 
    with open(f'ambiente/{img_random}', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

bot.run("MTE2MjgyMDA5ODM0ODgxMDMzMA.Go7mjJ.MQAOvvWPzfKsu-qmzaLB--YP1nPVVirba8QdQs")
