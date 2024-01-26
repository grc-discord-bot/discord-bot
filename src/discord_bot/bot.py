import logging

import discord
from discord.ext import commands

from src.discord_bot import responses

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
landed_channel_id = 1044095575282425906

bot = commands.Bot(command_prefix="$", intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandNotFound):
        return
    logging.exception(f'Error executing command "{ctx.message.content}"', exc_info=error)

    # Create a new file and log the error there
    with open('error.log', 'a') as f:
        f.write(f'{error} command: {ctx.message.content}\n')


async def send_to_landed_channel(message):
    channel = bot.get_channel(landed_channel_id)
    if channel:
        await channel.send(message)


async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
        to_send = f'Welcome {member.mention} to {guild.name}!'
        await guild.system_channel.send(to_send)
        await member.send(
            f'Hello {member.name}! Welcome. '
            f'Check out the announcements channel for important information about the club. '
            f'https://discord.com/channels/1043278905806692442/1043279855938191381')

        # Send a message to the landed channel
        await send_to_landed_channel(f'{member.name} has joined {guild.name}!')


async def on_member_remove(member):
    guild = member.guild
    if guild.system_channel is not None:
        to_send = f'Goodbye {member.mention} from {guild.name}!'
        await guild.system_channel.send(to_send)

        # Send a message to the landed channel
        await send_to_landed_channel(f'{member.name} has left {guild.name}!')


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


@bot.command()
async def _help(ctx):
    response = responses.get_response('help')
    await ctx.send(response)


@bot.command()
async def hello(ctx):
    response = responses.get_response('hello')
    await ctx.send(response)


@bot.command()
async def resources(ctx):
    response = responses.get_response('resources')
    await ctx.send(response)


@bot.command()
async def events(ctx):
    response = responses.get_response('events')
    await ctx.send(response)


@bot.command()
async def join(ctx):
    response = responses.get_response('join')
    await ctx.send(response)


@bot.command()
async def contact(ctx):
    response = responses.get_response('contact')
    await ctx.send(response)


# Example from: https://github.com/Rapptz/discord.py/blob/v2.2.2/examples/views/counter.py
# Define a simple View that gives us a counter button
class Counter(discord.ui.View):

    # Define the actual button
    # When pressed, this increments the number displayed until it hits 5.
    # When it hits 5, the counter button is disabled and it turns green.
    # note: The name of the function does not matter to the library
    @discord.ui.button(label='0', style=discord.ButtonStyle.red)
    async def count(self, interaction: discord.Interaction, button: discord.ui.Button):
        number = int(button.label) if button.label else 0
        if number + 1 >= 5:
            button.style = discord.ButtonStyle.green
            button.disabled = True
        button.label = str(number + 1)

        # Make sure to update the message with our updated selves
        await interaction.response.edit_message(view=self)


@bot.command()
async def counter(ctx: commands.Context):
    """Starts a counter for pressing."""
    await ctx.send('Press!', view=Counter())


class Roles(discord.ui.View):
    def __int__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Role 1", custom_id='Role 1', style=discord.ButtonStyle.green)
    async def button_1(self, interaction, button):
        role = 1085837013753790536
        user = interaction.user
        if role in [y.id for y in user.roles]:
            await user.remove_roles(user.guild.get_role(role))
            await interaction.response.send_message("Role 1 removed", ephemeral=True)
        else:
            await user.add_roles(user.guild.get_role(role))
            await interaction.response.send_message("Role 1 added", ephemeral=True)


@bot.command()
async def roles(ctx: commands.Context):
    embed = discord.Embed(title="Roles", description="Click the buttons to add/remove roles", color=0x00ff00)
    await ctx.send(embed=embed, view=Roles())
