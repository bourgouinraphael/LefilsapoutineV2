import discord
from discord.ext import commands
from config import *

client = commands.Bot(command_prefix=".", description="Le fils a Poutine", intents=discord.Intents.all())

@client.event
async def on_ready():
    print("On")

for file in os.listdir("extensions"):
    if file[-3:] == ".py":
        try:
            client.load_extension(f"extensions.{file[:-3]}")
        except:
            pass

client.run(TOKEN)
