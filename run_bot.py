#!/usr/bin/python

import discord
import requests
import configparser

import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

#create the client object
client = discord.Client()
config = ConfigParser.ConfigParser()

config.read("\\botConfig")
print(config['Account'])

token = something

client.login(token)
client.run()

def test_function(message):
    client.send_message(message.channel, '%s, hello!' % message.author)

@client.event
def on_message(message):
    if message.content.startswith('!test'):
        test_function(message)