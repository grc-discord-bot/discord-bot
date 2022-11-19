import discord
from discord.ext import commands

#initialize the bot with the commands imported from discord.ext and use '!' as command prefix to call the bot
client=commands.Bot(command_prefix='!')

# async is a special type of function, on_ready is also a function that it will execute automatically when it is ready to receive command
@client.event
async def on_ready():
    print("I am still alive!!")
    print("-------------------")
    