import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
bot.run(os.getenv("DISCORD_TOKEN"))

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


for filename in os.listdir("./src/discord_bot/cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"src.discord_bot.cogs.{filename[:-3]}")

bot = discord.Client(intents=intents)
