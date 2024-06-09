import discord 
from main import * 
 
# Membaca token dari file token.txt 
with open("token.txt", "r") as f: 
    token = f.read() 
 
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def passw(ctx, long = 5):
    await ctx.send(genn_pass(panjang))

bot.run(token)
