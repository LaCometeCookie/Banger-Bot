import discord
from discord.ext import commands

# On récupère le token
with open("Token.txt", "r", encoding="utf-8") as fichier:
    token= fichier.readline()


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'Le bot est en ligne !')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'banger' in message.content.lower():
        await message.add_reaction('🐸')
        await message.channel.send('BANGER !')


client.run(token)