import discord
import asyncio
from configparser import ConfigParser
import requests
import logging

#logging.basicConfig(level=logging.INFO)
print("Using DISCORD.PY v" + discord.__version__)

#create the client object
client = discord.Client()

config = ConfigParser()
config.read("bot.config")
token = config.get('Account', 'token')

@client.event
async def on_message(message):
	if message.content.startswith('!test'):
		await client.send_message(message.channel, '@%s, hello!' % message.author)
	elif message.content.startswith('!status'):
		await client.send_message(message.channel, 'Online and fully operational.')
		
@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

client.run(token)
