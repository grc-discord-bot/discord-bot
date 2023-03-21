import discord
from discord.ext import commands

from src.discord_bot import responses

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.event
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
        to_send = f'Welcome {member.mention} to {guild.name}!'
        await guild.system_channel.send(to_send)
        await member.send(
            f'Hello {member.name}! Welcome. '
            f'check out the announcements channel for important information about the club. '
            f'https://discord.com/channels/1043278905806692442/1043279855938191381')


@bot.event
async def on_member_leave(member):
    guild = member.guild
    if guild.system_channel is not None:
        to_send = f'Goodbye {member.mention} from {guild.name}!'
        await guild.system_channel.send(to_send)


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
