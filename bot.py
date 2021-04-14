#!/bin/python

import os
import random
import argparse
# cleanMessage
import re
# for url encoding
import urllib.parse

#https://discordpy.readthedocs.io/en/latest/logging.html
import logging
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

import discord
from dotenv import load_dotenv

# misc.py in the same folder as this file
import misc

load_dotenv()
GUILD = "iojumper"
client = discord.Client()

async def showHelp():
    # this list should be alphabetical
    help = '''currently supported commands are.
    !btc - lists the current bitcoin price
    !gg  - returns gg
    !google <term> - returns the first link from the google search
    !help - shows this help message
    !joke - A joke! lol!
    !weather <city> - returns the current weather. can be an important location.
    '''
    return help

async def cleanMessage(message, positionsToReturn):
    #positionsToReturn should be 0 = the entire message without the command returned,1 = first word without the command
    #only allow a-z A-Z 0-9
    message = re.sub(r"[^a-zA-Z0-9 ]","",message)
    messageArray = message.split(" ")
    # remove the command
    del messageArray[0]
    if int(positionsToReturn) == 0:
        # return the entire thing
        message = ' '.join(messageArray)
        return(message)

    if int(positionsToReturn) == 1:
        # return the first word only
        message = ''.join(messageArray[0])
        return(message)

    #urllib.parse.quote_plus()

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

    if message.content.startswith( '!ping' ):
        logger.info(str(message.author) + " is running !ping on " + str(message.guild))
        await message.channel.send("pong")

    if message.content.startswith( '!pong' ):
        logger.info(str(message.author) + " is running !pong on " + str(message.guild))
        await message.channel.send("ping")

    if message.content.startswith( '!help' ):
        logger.info(str(message.author) + " is running !help on " + str(message.guild))
        await message.channel.send(await showHelp())

    if message.content.startswith( '!weather' ):
        logger.info(str(message.author) + " is running !weather on " + str(message.guild))
        await message.channel.send(await misc.sendWeather(message))

    if message.content.startswith( '!joke' ):
        logger.info(str(message.author) + " is running !joke on " + str(message.guild))
        await message.channel.send(await misc.sendJoke())

    if message.content.startswith( '!google' ):
        logger.info(str(message.author) + " is running !google on " + str(message.guild))
        googleSearchString = await cleanMessage(message.content, 0)
        await message.channel.send(await misc.googleSearch(googleSearchString))

    if message.content.startswith( '!btc' ):
        logger.info(str(message.author) + " is running !btc on " + str(message.guild))
        await message.channel.send(await misc.btc())

if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("-t", "--token", help="discord bot token", type=str)
        args = parser.parse_args()
        # a discord bot token is required for this app to work
        if args.token:
            TOKEN = args.token
            logger.info("discord token gathered from argument -t.")
        elif os.getenv('DISCORD_TOKEN'):
            TOKEN = os.getenv('DISCORD_TOKEN')
            logger.info("discord token gathered from env variable.")
        else:
            print("No token for discord bot was found. Check -h for help")
            logger.error("No token found.")
            exit()
        client.run(TOKEN)
    except KeyboardInterrupt:
        print("Exiting",flush=True)
        sys.exit(0)