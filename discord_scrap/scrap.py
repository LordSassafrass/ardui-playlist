import discord
import re
import logging
import spotify_play as ss
import channel_lookup as cl

client = discord.Client()

logging.basicConfig(filename='discord.log')

@client.event
async def on_ready():
    logging.debug('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content == "$status":
        await message.channel.send("Everything seems to be aok.")

    elif message.content == "$refresh":
        await message.channel.send("Refreshing playlist this may take some time.")
        try:
            playlist = cl.channel_lookup[str(message.channel)]
            history = await message.channel.history().flatten()
            songs_uri = []
            for msg in history:
                content = msg.content.strip()
                if "https://open.spotify.com/album" in content or "https://open.spotify.com/track" in content:
                    parsed_uri = re.search("(?P<url>https?://[^\s]+)", content).group("url")
                    songs_uri.append(parsed_uri)
            ss.refresh(playlist, songs_uri)
        except KeyError:
            await message.channel.send("............ mission failed")
            logging.error("playlist not found: {}".format(message.channel))
        await message.channel.send("MISSION COMPLETE!")
        

    elif "https://open.spotify.com/album" in message.content or "https://open.spotify.com/track" in message.content:
        parsed_uri = re.search("(?P<url>https?://[^\s]+)", message.content).group("url")
        message_send = "Adding to playlist {}".format(message.channel)
        try:
            playlist = cl.channel_lookup[str(message.channel)]
            ss.intake(playlist, parsed_uri)
            logging.info(parsed_uri)
            await message.channel.send(message_send)
        except KeyError:
            logging.error("playlist not found: {}".format(message.channel))

file1 = open('token.txt', 'r')
TOKEN = file1.readline()
file1.close()

client.run(TOKEN)