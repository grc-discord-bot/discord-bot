from config import token
import discord
intents = discord.Intents.all()
intents.typing = False
intents.presences = False


from discord.ext import commands
#initialize the bot with the commands imported from discord.ext and use '!' as command prefix to call the bot
client = commands.Bot(command_prefix='!', intents=intents)

# async is a special type of function, on_ready is also a function that it will execute automatically when it is ready to receive command
@client.event
async def on_ready():
    print("I am still alive!!")
    print("-------------------")

#define our own funciton here i just type in hello first, ctx is like taking inputs from disord, so the user will type in !hello to excecute the coomand in discord
@client.command()
async def hello(ctx):
    await ctx.send("Welcome to Google Student Developer Club@GRC/competitive programming club!")

#token -> never want to reveal this
client.run(token)