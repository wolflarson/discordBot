#!/bin/python

import os
import random
import json
import aiohttp
import asyncio

#https://discordpy.readthedocs.io/en/latest/logging.html
import logging
logger = logging.getLogger('discord')
logger.setLevel(logging.WARNING)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = "iojumper"
client = discord.Client()

async def gg(message):
	await message.channel.send("gg no re")

async def sendJoke(message):
    async with aiohttp.ClientSession() as session:
        jokeBaseURL = "https://api.chucknorris.io/jokes/random"
        async with session.get(jokeBaseURL) as resp:
            getJokeObject = await resp.text()
            getJokeAsJSON = json.loads(getJokeObject)

    await message.channel.send(getJokeAsJSON["value"])

async def showHelp(message):
    helpArray = [
    "currently supported commands are.",
    "!gg   - returns gg",
    "!weather - takes a city name as input (default Detroit), returns the forcast",
    "!help - shows this help message",
    "!joke - A joke! lol!"
    ]
    for i in helpArray:
       await message.channel.send(i)

async def sendWeather(message):
    # check if a city is set
    messageList = message.content.split(" ")
    isCitySet = len(messageList)
    logger.info("message length is " + str(isCitySet))
    if isCitySet > 1:
        city = message.content.split(" ")[1]
        logger.info("city set to" + city)
    else:
        city = "detroit"
        logger.info("city set to" + city)

    # create an empty string to hold the weather report
    weather = ""
    headers = {'content-type': 'text/plain'}
    async with aiohttp.ClientSession() as session:
        weatherBaseURL = "http://wttr.in/" + str(city) + "?T"
        # gather the full weather rport, split it line by line then just grab the first 6 lines
        async with session.get(weatherBaseURL,headers=headers) as resp:
            fullWeatherReport = await resp.text()
            split = fullWeatherReport.splitlines()
            count = 0
            for i in split:
                # this is the same as weather = weather + i in case I forget cuz I'm dumb
                weather += i
                weather += "\n"
                count += 1
                if count > 6:
                    break
    await message.channel.send(weather)


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
    if message.author == client.user:
        return

    if message.content == '!gg':
        await gg(message)

    if message.content == '!help':
       await showHelp(message)

    if message.content.startswith( '!weather' ):
        await sendWeather(message)

    if message.content.startswith( '!joke' ):
        await sendJoke(message)

logger.warning('hi')
client.run(TOKEN)
