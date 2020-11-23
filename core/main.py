import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from config import help_hint as hint
from databasemodule import takeprice


load_dotenv()
KEY_API = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print('E-Xchange Working!')


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hello {member.name}, now I will keep you informed about news from the financial world. Good luck'
    )


bot.remove_command("help")


@bot.command(name="help")
async def helpComand(ctx):
    embed = discord.Embed(
        title="Helper", description=f"!print - {hint.price_comand_help}", color=0x3bbdba)
    embed.set_footer(text="E-Xchange")
    await ctx.author.create_dm()
    await ctx.author.dm_channel.send(embed=embed)


@bot.command(name="price", help=hint.price_comand_help)
async def price(ctx):
    await ctx.author.create_dm()
    await ctx.author.dm_channel.send("``` Check price of currency -> !currency \n\n"
                                     " Check price of crypto -> !crypto \n\n"
                                     " Check price of metals -> !metals ```\n\n")


@bot.command(name="currency")
async def currencyPrice(ctx):
    take_price = takeprice("currency")
    embed = discord.Embed(title="Currency Price", color=0x008000)
    i = 0
    for x in take_price:
        embed.add_field(name=f"{take_price[i][1]}", value=f"{take_price[i][0]}", inline=False)
        i += 1

    await ctx.author.create_dm()
    await ctx.author.dm_channel.send(embed=embed)


bot.run(KEY_API)
