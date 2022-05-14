import os
import discord
import re
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")


client = discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    
    print(
    f'{client.user} has connected to Discord!'
    f'{guild.name} (id: {guild.id})'
    )

#the fun shit
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    slimshady = """> Hi, my name is
> *what?*
> My name is
> *who?*
> My name is
> *chicka **chicka***
> %s""" %re.sub("(?i)^i'?m ", "" ,message.content, 1)
    
    havesomecake = """> Have some cake!
> :cake:
>  ¯¯¯\\\_(ツ)
"""
    sorryhavesomecake = """> I'm sorry, I don't have %s...
> Would some cake be okay instead?
> :cake:
>  ¯¯¯\\\_(ツ)


""" %re.sub("(?i)i want\s", "", message.content)
    
    feellike = "> I also feel " + re.sub("(?i)I feel ", "", message.content)
    
    if re.search("(?i)^I'?m",message.content):
        await message.channel.send(slimshady)
    elif message.content.lower().startswith("i want"):
        if re.search("(?i).*?I want (this|some|that|your|a|)? ?cake",message.content):
            await message.channel.send(havesomecake)
        else:
            await message.channel.send(sorryhavesomecake)
            
    elif message.content.lower().startswith("i don't want cake") or message.content.lower().startswith("i dont want cake"):
        await message.channel.send("> :(")
        
    elif message.content.lower().startswith("i feel"):
        await message.channel.send(feellike)
        
    elif message.content.lower().startswith("!vote"):
        msg = await message.channel.send(setup_vote(message.content))
        await msg.add_reaction("1️⃣")
        await msg.add_reaction("2️⃣")
    

def setup_vote(message): # !vote Cats or dogs? ~cats,dogs 
    try:
        mess = re.sub("!vote", "", message)
        m = mess.split("~")
        v = m.pop(1).split(",")
        
        m = m[0]
        
        s = "***VOTE***" + "\n> Question: " + m.strip() + "\n> :one: " + str(v[0]).strip() + "\n> \n> :two: " + str(v[1]).strip()
        return s
    except:
        return "Error: invalid vote"
        

client.run(TOKEN)
