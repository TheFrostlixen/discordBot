import discord
import asyncio
import requests
import logging
from voice import VoiceEntry, VoiceState
from music import Music
from configparser import ConfigParser
from discord.ext import commands

if not discord.opus.is_loaded():
	discord.opus.load_opus('opus')

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
bot.add_cog(Music(bot))

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
