import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from config import help_hint as hint
import asyncio

load_dotenv()
KEY_API = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)
bot.remove_command("help")

@bot.event
async def on_ready():
    print(f'E-Xchange Working!')


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hello {member.name}, now I will keep you informed about news from the financial world. Good luck'
    )

@bot.command(name="help")
async def helpComand(ctx):
    await ctx.author.create_dm()
    await ctx.author.dm_channel.send(f"```!price -> {hint.price_comand_help} \n```")



@bot.command(name="price", help=hint.price_comand_help)
async def price(ctx):
    await ctx.author.create_dm()
    await ctx.author.dm_channel.send("``` Check price of currency -> !currency \n\n"
                   " Check price of crypto -> !crypto \n\n"
                   " Check price of metals -> !metals ```\n\n")








bot.run(KEY_API)
