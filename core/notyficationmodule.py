import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
KEY_API = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True

client = discord.Client()
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    for i in [703212875271110696, 703212875271110696, 703212875271110696]:
        await notyficationSend(i)


async def notyficationSend(id):
    user = await bot.fetch_user(id)
    print(user)
    await user.send("Your message goes here")

bot.run(KEY_API)
