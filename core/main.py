import os
import discord
from dotenv import load_dotenv

load_dotenv()
KEY_API = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)


@client.event
async def on_ready(): print(f'E-Xchange Working!')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hello {member.name}, now I will keep you informed about news from the financial world. Good luck'
    )


client.run(KEY_API)
