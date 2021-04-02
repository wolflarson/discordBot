#!/bin/python

import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = "iojumper"
client = discord.Client()

async def gg(message):
	"""this function returns gg"""
	await message.channel.send("gg")

async def showHelp(message):
    helpArray = [
    "currently supported commands are.",
    "!gg   - returns gg",
    "!weather - takes a city name as input (default Detroit), returns the forcast",
    "!help - shows this help message"
    ]
    for i in helpArray:
       await message.channel.send(i)

async def showWeather(message):
    await message.channel.send(i)
    # http://wttr.in/detroit

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    # Printer server guid
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    # list members
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)

    if message.content == '!gg':
        await gg(message)


    if message.content == '!help':
       await showHelp(message)


client.run(TOKEN)

