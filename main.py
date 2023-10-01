import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")  
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.event
async def on_member_join(member):
    channel = member.guild.get_channel(1234567890)  
    if channel:
        await channel.send(f'Welcome, {member.mention}!')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello, {ctx.author.mention}!')

bot.run('YOUR_BOT_TOKEN')
