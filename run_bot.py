import discord
import asyncio
import requests
import configparser
import random

import logging

logging.basicConfig(level=logging.INFO)
random.seed()

#create the client object
client = discord.Client()
config = configparser.ConfigParser()

config.read("bot.config")

LUNCH_OPTIONS = ["In-N-Out", "Panda Express", "Canes", "Chipotle", "McDonalds", "Jack in the Box"]

token = config.get('Account', 'token')
print(discord.__version__)

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        await client.send_message(message.channel, '@%s, hello!' % message.author)
    if message.content.startswith('!roll'):        
        await client.send_message(message.channel, '%s' % random.randint(0,100))
    if message.content.startswith('!lunch'):
        temp = random.randint(0, len(LUNCH_OPTIONS) -1)
        await client.send_message(message.channel, 'I think you should go to %s for lunch.' % LUNCH_OPTIONS[temp])
        
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(token)





