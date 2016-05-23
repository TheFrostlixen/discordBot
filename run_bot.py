import discord
import asyncio
import requests
import configparser

import logging

logging.basicConfig(level=logging.INFO)

#create the client object
client = discord.Client()
config = configparser.ConfigParser()

config.read("botConfig")


token = config.get('Account', 'token')
print(discord.__version__)

@client.event
async def on_message(message):
    print("Asdf")
    if message.content.startswith('!test'):
        print("asdfasdf")
        await client.send_message(message.channel, '%s, hello!' % message.author)
        
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(token)





