import discord
import os
import time

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

async def get_history_of_channel(channel):
    messages = await channel.history(limit=None) # adding None lets us retrieve every message
    for message in messages:
        # do something with that message
        print(message.content)


file1 = open('token.txt', 'r')
client.run(file1.readline())
file1.close()

sleep(5000)

for guild in client.guilds:
    for chan in client.get_all_channels():
        print(chan)
        get_history_of_channel(chan)