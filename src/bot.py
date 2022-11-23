import discord
from discord.ext import commands
import responses
from dotenv import load_dotenv
import os

#class CustomHelpCommand(commands.HelpCommand):
#    def __init__(self):
#        super().__init__

#    async def send_bot_help(self, mapping):
#        for cog in mapping:
#            await self.get_destination().send(f'{cog.quilified_name}: {[command.name for command in mapping[cog]]}')

#    async def send_cog_help(self, cog: Cog, /) -> None:
#        await self.get_destination().send(f'{cog.qualified_name}: {[command.name for command in cog.get_commands()]}')

#    async def send_group_help(self, group):
#        await self.get_destination().send(f'{group.name}: {[command.name for index, command in enumerate(group.commands)]}')

#    async def send_command_help(self, command):
#        await self.get_destination().send(command.name)

    

# Configure the token key
def configure():
    load_dotenv()


async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    configure()
    token = os.getenv('token_key')
    chanel_number = 1044095575282425906

    intents = discord.Intents.all()
    intents.members = True
    intents.message_content = True
    intents.typing = False
    intents.presences = False
    client = commands.Bot(command_prefix='$', intents=intents)

    def get_channel(number):
        return client.get_channel(number)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        # begin a private conversation with the bot initiated
        # by a question mark ?hello
        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    @client.event
    async def on_member_join(member):
        channel = get_channel(chanel_number)
        await channel.send(f'{member} Hello and welcome to the server!')

    @client.event
    async def on_member_remove(member):
        channel = get_channel(chanel_number)
        await channel.send(f'{member} has left the server.')

    # add more events
    # add more commands

    client.run(token)
