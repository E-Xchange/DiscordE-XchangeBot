import os
import time
import asyncio
import discord
import schedule
from dotenv import load_dotenv
from discord.ext import commands
from databasemodule import takediscordid

load_dotenv()
KEY_API = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)


def asyncloop():

    async def notyficationSend(id):
        time.sleep(1)
        await bot.wait_until_ready()
        user = await bot.fetch_user(id)
        print(user)
        await user.send("Your message goes here")

    async def loop():
        for i in takediscordid():
            print(takediscordid())
            await notyficationSend(i)

    bot.loop.create_task(loop())


async def whilehehe():
    schedule.every().day.at("21:24").do(asyncloop)
    while True:
        schedule.run_pending()
        await asyncio.sleep(60)


bot.loop.create_task(whilehehe())
bot.run(KEY_API)
