import discord
from discord.ext import commands
import asyncio
from configparser import ConfigParser
import requests
import logging

#logging.basicConfig(level=logging.INFO)
print("Using DISCORD.PY v" + discord.__version__)

# Read token and settings from config file
config = ConfigParser()
config.read("config/bot.config")
token = config.get('Account', 'token')
desc = config.get('Settings', 'desc')
symbol = config.get('Settings', 'symbol')

# Create the bot client object
bot = commands.Bot(command_prefix=symbol, description=desc)


''' BOT COMMAND DEFINITIONS '''
@bot.command()
async def add(left : int, right : int):
	await bot.say(left + right)

@bot.command()
async def status():
	await bot.say("Currently online and ready.")


''' BOT EVENT DEFINITIONS '''
@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')

bot.run(token)
