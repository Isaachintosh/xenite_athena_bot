#Athena a primeira deusa xenite bot do discord
#Iniciativa Revista Xenite

# Carregar as variáveis de ambiente
from dotenv import load_dotenv
load_dotenv()

# from random import randint
import os
import discord
from discord.ext import commands

from utils import read_text_file, get_random_str_from_array


CAMINHO_MAIN_PY = os.path.dirname(__file__)

PIADAS   = read_text_file(f'{CAMINHO_MAIN_PY}/db/piadas.txt')
TOPICOS  = read_text_file(f'{CAMINHO_MAIN_PY}/db/topicos.txt')
CITACOES = read_text_file(f'{CAMINHO_MAIN_PY}/db/quotes.txt')


# Definindo os intents necessários
intents = discord.Intents.default()
intents.members = True
intents.message_content = True


## OPÇÃO 1
bot = commands.Bot(command_prefix="!", description="Athena Bot", intents=intents)

# Evento on_ready
@bot.event
async def on_ready():
    print(f'Logado como {bot.user.name}')

# Comando piadas
@bot.command()
async def piada(ctx):
    await ctx.send(get_random_str_from_array(PIADAS))

# Comando citação
@bot.command()
async def citacao(ctx):
    await ctx.send(get_random_str_from_array(CITACOES))

# Comando topico
@bot.command()
async def topico(ctx):
    await ctx.send(get_random_str_from_array(TOPICOS))

bot.run(os.getenv('TOKEN'))



## OPÇÃO 2
# client = discord.Client(description="Athena Bot", intents=intents)

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.startswith('!piada'):
#         await message.channel.send(get_random_str_from_array(PIADAS))

#     if message.content.startswith('!citacao'):
#         await message.channel.send(get_random_str_from_array(CITACOES))

#     if message.content.startswith('!topico'):
#         await message.channel.send(get_random_str_from_array(TOPICOS))

# client.run(os.getenv('TOKEN'))