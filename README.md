# DISCORD JOCKEY
---
DiscordJockey is a community-driven radio station, in the form of a  [Discord](https://discord.gg) chat bot. Designed to accept commands through both PMs and a special in-server text channel, it will play any song it can find on the internet via a voice channel. 

Currently in extremely early stages. This file will be updated as features are added to the platform.


## Installation
This bot is an implementation of the Discord Bot API wrapper in Python by [Rapptz](https://github.com/Rapptz/discord.py). 

Run `python3 -m pip install -U https://github.com/Rapptz/discord.py/archive/master.zip#egg=discord.py[voice]` to install his latest version of the Python API wrapper, then clone this repo and insert your App Bot User's token into `bot.config`. To add the bot to your server, go to `https://discordapp.com/oauth2/authorize?client_id={bot client id}&scope=bot&permissions=0` and add it through Discord's interface. Then simply execute `run_bot.py`.
