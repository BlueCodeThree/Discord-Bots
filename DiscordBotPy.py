# Work with Python 3.6
import discord
from discord.ext import commands
import random
import math
from random import shuffle
import json

bot = commands.Bot(command_prefix='#')
prefix = "#"
learnCommand = "none"
learnResponse = "none"

botdict = [{"botcommand": "head", "botresponse": "*pats head*"} ]
fuckme = botdict
with open('dict.json', 'r') as f:
    fuckme = json.load(f)


TOKEN = 'NTI1NzkzODg0NzAyMjQ0ODg0.Dv71FA.R0P4UasVLo6VHTGOOKsR4nxMPVU'

client = discord.Client()


@client.event
async def on_ready():
    print("A wild PythonDom appears")
#    await client.change_presence(activity=discord.activity(name="being dominating"))


Domanswer = ["*nods nods*", "uh-huh", "mmmhmm", "*nods a little*", "*pets you gently*", "*smirks at you*",
             "*smirks down at you*", "*smiles and pets you*", "*strokes you sympathetically*", "*strokes you gently*",
             "*good girl*", "*nods looking down at you*", "*grins at you*", "*laughs*",
             "*gives your bottom a little pat*"]
DomShuffle = Domanswer[:]
shuffle(DomShuffle)

unpleaseanswer = [
    "Usually when a pleasing submissive girl is asked a question she answers the question rather than asking a question in retaliation.",
    "tell me, if a girl knows what he wants her to do, yet fails to do it, what happens?", "*looks down at the girl*"]
UnpleaseShuffle = unpleaseanswer[:]
shuffle(UnpleaseShuffle)

bratanswer = ["*mmmhmm*", "*obnoxious girl*", "*silly girl*", "*smacks your bottom*", "*so obnoxious*",
              "*looks down at the girl*", "*insolent girl*"]

clothes_bottom = ["Wear the shorts, girl", "Wear the skirt, girl"]
clothes_top = ["I command you to wear the singlet", "I command you to wear the tshirt, time-travel-nerd girl"]
clothes_underwear = ["No bra today", "No underwear today", "Wear underwear, girl"]


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    if message.content.startswith('#dom'):
        DomTemp = DomShuffle[0]
        DomShuffle.pop(0)
        DomShuffle.insert(random.randint(len(DomShuffle) // 2, len(DomShuffle)), DomTemp)
        await message.channel.send(DomShuffle[0])
    if message.content.startswith('#unpleasing'):
        UnpleaseTemp = UnpleaseShuffle[0]
        UnpleaseShuffle.pop(0)
        UnpleaseShuffle.insert(random.randint(len(UnpleaseShuffle) // 2, len(UnpleaseShuffle)), UnpleaseTemp)
        await message.channel.send(UnpleaseShuffle[0])
    if message.content.startswith('#obnoxious'):
        await message.channel.send(random.choice(bratanswer))
    if message.content.startswith('#top'):
        await message.channel.send(random.choice(clothes_top))
    if message.content.startswith('#bottom'):
        await message.channel.send(random.choice(clothes_bottom))
    if message.content.startswith('#underwear'):
        await message.channel.send(random.choice(clothes_underwear))
    if message.content.startswith('#good'):
        await message.channel.send("good girl")
    if message.content.startswith('#goodbye'):
        await message.channel.send("Goodbye amazing girl, until you turn me on again next time. And, um, good bye to you too other person")
    if message.content.startswith('#hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)
    if message.content.startswith('!learn'):
        global learnCommand
        learnCommand = message.content[7:]
        await message.channel.send("oh, you want me to learn \"" + learnCommand + "\" do you hmmmm?")
    if message.content.startswith("!yes"):
        await message.channel.send("you mean, \"#yes sir\"")
    if message.content.startswith("#yes sir"):
        await message.channel.send("and what do you wish for me to say in response?")
    if message.content.startswith("#response"):
        global learnResponse
        global botdict
        global json
        learnResponse = message.content[10:]
        await message.channel.send(learnResponse + " hmmmm?")
        await message.channel.send("alright, I'll consider it")
        fuckme.append({"botcommand": learnCommand, "botresponse": learnResponse})
        jsonwrite = json.dumps(fuckme)
        p = open("dict.json", "w")
        p.write(jsonwrite)

    if message.content.startswith("!no"):
        await message.channel.send("wasting my time, hmmmm?")

    for d in fuckme:
        if message.content.startswith(prefix + d["botcommand"]):
            await message.channel.send(d["botresponse"])






client.run(TOKEN)