import discord
import re
import logging

client = discord.Client()

logging.basicConfig(filename='discord.log', encoding='utf-8', level=logging.DEBUG)

@client.event
async def on_ready():
    logging.debug('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "https://open.spotify.com" in message.content:
        parsed_uri = re.search("(?P<url>https?://[^\s]+)", message.content).group("url")
        message_send = "Adding to playlist {}".format(message.channel)
        logging.info(parsed_uri)
        await message.channel.send(message_send)

file1 = open('token.txt', 'r')
TOKEN = file1.readline()
file1.close()

client.run(TOKEN)