#!/bin/python

import os
import random

#https://discordpy.readthedocs.io/en/latest/logging.html
import logging
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = "iojumper"
client = discord.Client()

async def showHelp():
    # this list should be alphabetical
    help = '''currently supported commands are.
    !gg   - returns gg
    !help - shows this help message
    !joke - A joke! lol!
    !weather - takes a city name as input (default Detroit), returns the forcast
    '''
    return help

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    # Printer server guid
    # guild = discord.utils.get(client.guilds, name=GUILD)
    # print(
    #     f'{client.user} is connected to the following guild:\n'
    #     f'{guild.name}(id: {guild.id})'
    # )

    # list members
    # members = '\n - '.join([member.name for member in guild.members])
    # print(f'Guild Members:\n - {members}')

@client.event
async def on_message(message):
    # ideally we want to do all the discord ineractions here. just return the value we are going to send
    if message.author == client.user:
        return

    if message.content.startswith( '!gg' ):
        logger.info(str(message.author) + " is running !gg on " + str(message.guild))
        await message.channel.send("gg")

    if message.content.startswith( '!help' ):
        logger.info(str(message.author) + " is running !help on " + str(message.guild))
        await message.channel.send(await showHelp())

    if message.content.startswith( '!weather' ):
        logger.info(str(message.author) + " is running !weather on " + str(message.guild))
        from misc import sendWeather
        await message.channel.send(await sendWeather(message))

    if message.content.startswith( '!joke' ):
        logger.info(str(message.author) + " is running !joke on " + str(message.guild))
        from misc import sendJoke
        await message.channel.send(await sendJoke(message))

logger.warning('hi')
client.run(TOKEN)
