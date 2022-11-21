from config import token
import discord
intents = discord.Intents.all()
intents.members=True
intents.typing = False
intents.presences = False


from discord.ext import commands
#initialize the bot with the commands imported from discord.ext and use '!' as command prefix to call the bot
client = commands.Bot(command_prefix='!', intents=intents)

# async is a special type of function, on_ready is also a function that it will execute automatically when it is ready to receive command
#event is when encounter with certain condition, it will run certain code
@client.event
async def on_ready():
    print("I am still alive!!")
    print("-------------------")

#define our own funciton here i just type in hello first, ctx is like taking inputs from disord, so the user will type in !hello to excecute the coomand in discord
@client.command()
async def hello(ctx):
    await ctx.send("Welcome to Google Student Developer Club@GRC/competitive programming club!")

@client.event
async def on_member_join(memebr):
    channel= client.get_channel(1044095575282425906)
    await channel.send("hello and welcome to our club server")
    #these two lines below were just trying out something 
    #await channel.send(f"{member.mention} hello and welcome to our club server'")
    #f"{member} welcome to the server!'

#not a really useful event since the user who left can't see this message
#@client.event
#async def on_member_remove(memebr):
#    channel= client.get_channel(1044095575282425906)
#    await channel.send("so sad you leave, but you are always welcome to come back! although you can't see this:(")

#token -> never want to reveal this!!
client.run(token)

