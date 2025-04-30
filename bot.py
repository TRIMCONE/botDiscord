import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot aktif sebagai {bot.user}')

@bot.command()
async def halo(ctx):
    await ctx.send("Halo dari Railway!")

bot.run(os.getenv("TOKEN"))
