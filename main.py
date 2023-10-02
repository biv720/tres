import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!") 

initial_extensions = ['cogs.mod']

for extension in initial_extensions:
    bot.load_extension(extension)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

bot.run('YOUR_BOT_TOKEN')
