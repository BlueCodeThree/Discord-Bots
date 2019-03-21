# Carlie Hamilton
# https://github.com/BlueCodeThree
# I am trying to make a discord bot that helps you with basic programming thingies,
# in multiple languages, as a simple reference. 
import discord
from discord.ext import commands
import random
import math
from random import shuffle
import json
import js
import rb
import tokenkey
import spotipy
import spotipy.util as util
import apikey
import sys
import webbrowser
import os
from musixmatch import Musixmatch

bot = commands.Bot(command_prefix='!')
prefix = "!"

TOKEN = tokenkey.bot_token

client = discord.Client()

@client.event
async def on_ready():
    print("A wild Bot appears")
#    await client.change_presence(activity=discord.activity(name="being all bot like"))

# STUFF FOR MUSIC STUFF
username = apikey.spotify_username
scope = 'user-read-currently-playing'
musixmatch = Musixmatch(apikey.musixmatch_api)

# getting a token for spotify
try:
    token = util.prompt_for_user_token(username,scope,client_id=apikey.spotify_id,client_secret=apikey.spotify_secret,redirect_uri=apikey.spotify_redirect)
except:
    print("Can't get token for", username)
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username,scope,client_id=apikey.spotify_id,client_secret=apikey.spotify_secret,redirect_uri=apikey.spotify_redirect)


# spotify object
sp = spotipy.Spotify(auth=token)

# Gets the currently playing artist and song name
#current_playing_artist = sp.current_user_playing_track()['item']['album']['artists'][0]['name']
#current_playing_song = sp.current_user_playing_track()['item']['name']

# search for the track id - in order to get the lyrics
#track_id = musixmatch.track_search(current_playing_song, current_playing_artist, page_size=10, page=1, s_track_rating='desc')['message']['body']['track_list'][0]['track']['track_id']

# get the lyrics of a song
def get_lyrics(track_id):
    lyrics = musixmatch.track_lyrics_get(track_id)['message']['body']['lyrics']['lyrics_body']
    return lyrics
 

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    # general conversation
    if message.content.startswith(prefix + 'hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)

    # JAVASCRIPT
    if message.content.startswith(prefix + "js" + ' comment'):
        await message.channel.send(js.comment_answer)
    if message.content.startswith(prefix + "js" + ' if'):
        await message.channel.send(js.if_answer)

    # RUBY
    if message.content.startswith(prefix + "rb" + ' print') or message.content.startswith(prefix + 'rb' + ' puts'):
        await message.channel.send(rb.print_answer)
    if message.content.startswith(prefix + "rb" + ' length'):
        await message.channel.send(rb.length_answer)
    if message.content.startswith(prefix + "rb" + ' time'):
        await message.channel.send(rb.time_answer)
    if message.content.startswith(prefix + "rb" + ' gets') or message.content.startswith(prefix + 'rb' + ' input'):
        await message.channel.send(rb.gets_answer)
    if message.content.startswith(prefix + "rb" + " function"):
        await message.channel.send(rb.function_answer)
    if message.content.startswith(prefix + "rb" + " convert") or message.content.startswith(prefix + 'rb' + ' change type'):
        await message.channel.send(rb.convert_answer)
    if message.content.startswith(prefix + "rb" + " string"):
        await message.channel.send(rb.string_answer)
    if message.content.startswith(prefix + "rb" + " if") or message.content.startswith(prefix + 'rb' + ' unless'):
        await message.channel.send(rb.if_answer)
    if message.content.startswith(prefix + "rb" + " array") or message.content.startswith(prefix + 'rb' + ' list'):
        await message.channel.send(rb.array_answer)
    if message.content.startswith(prefix + "rb" + " loop") or message.content.startswith(prefix + 'rb' + ' while') or message.content.startswith(prefix + 'rb' + ' conditional') or message.content.startswith(prefix + 'rb' + ' until') or message.content.startswith(prefix + 'rb' + ' each') or message.content.startswith(prefix + 'rb' + ' for'):
        await message.channel.send(rb.loop_answer)
    if message.content.startswith(prefix + "rb" + " exception"):
        await message.channel.send(rb.exceptions_answer)

    # MUSIC! 
    # if message.content.startswith(prefix + 'playing'):
    #     await message.channel.send("Artist:  " + current_playing_artist)
    #     await message.channel.send("Song: " + current_playing_song)
    #     await message.channel.send("Lyrics:")
    #     await message.channel.send(get_lyrics(track_id))
    
    # learn new commands
    # if message.content.startswith('!learn'):
    #     global learnCommand
    #     learnCommand = message.content[7:]
    #     await message.channel.send("oh, you want me to learn \"" + learnCommand + "\" do you hmmmm?")
    # if message.content.startswith("!yes"):
    #     await message.channel.send("and what do you wish for me to say in response?")
    # if message.content.startswith("!response"):
    #     global learnResponse
    #     global json
    #     learnResponse = message.content[10:]
    #     await message.channel.send(learnResponse + " hmmmm?")
    #     await message.channel.send("alright, I'll consider it")
        # copybotdict.append({"botcommand": learnCommand, "botresponse": learnResponse})
        # jsonwrite = json.dumps(copybotdict)
        # p = open("dict.json", "w")
        # p.write(jsonwrite)

    # if message.content.startswith("!no"):
    #     await message.channel.send("wasting my time, hmmmm?")

    # for d in copybotdict:
    #     if message.content.startswith(prefix + d["botcommand"]):
    #         await message.channel.send(d["botresponse"])






client.run(TOKEN)