import os
import discord
from dotenv import load_dotenv

load_dotenv()
KEY_API = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member, message):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi Nice to meet you'
    )
    await message.channel.send(f"Dolaczyl do nas {client.user.name}")
    print("dolaczyl ")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    text = "bot test"

    if message.content == "99!":
        await message.channel.send(text)

client.run(KEY_API)
