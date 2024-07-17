import discord
import os
from discord.ext import commands
import random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hola(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def tes(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f'{len(args)} arguments: {arguments}')

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

meme = os.listdir("images")

@bot.command()
async def mem(ctx):
    img_name = random.choice(meme)
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file = picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def get_dog_image_url():    
    url = "https://random.dog/woof.json"
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('dog')
async def dog(ctx):
    image_url = get_dog_image_url()
    await ctx.send(image_url)

@bot.command()
async def que_es_contaminacion(ctx):
    await ctx.send("La contaminación ambiental es la presencia de componentes nocivos, bien sean de naturaleza biológica, química o de otra clase, en el medioambiente, de modo que supongan un perjuicio para los seres vivos que habitan un espacio, incluyendo, por supuesto, a los seres humanos.")

cont = os.listdir("cont_images")

@bot.command()
async def imagenes_de_contaminacion(ctx):
    img_cont = random.choice(cont)
    with open(f'cont_images/{img_cont}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file = picture)

memes = os.listdir("cont_meme")

@bot.command()
async def memes_de_contaminacion(ctx):
    img_cont_mem = random.choice(memes)
    with open(f'cont_meme/{img_cont_mem}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file = picture)

bot.run("")
