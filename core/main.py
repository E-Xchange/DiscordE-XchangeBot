import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from module import embedAdd
from databasemodule import adddiscordid, removediscordid
from config import help_hint as hint


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
        title="Helper", description=f"!price - {hint.price_comand_help}", color=0x3bbdba)
    embed.set_footer(text="E-Xchange")
    await ctx.author.create_dm()
    await ctx.author.dm_channel.send(embed=embed)


@bot.command(name="price", help=hint.price_comand_help)
async def price(ctx):
    await ctx.author.create_dm()
    await ctx.author.dm_channel.send(hint.price_info)


@bot.command(name="alertON")
async def notyficationON(ctx):
    cl_discord_id = ctx.author.id
    adddiscordid(cl_discord_id)
    await ctx.author.create_dm()
    await ctx.author.dm_channel.send(hint.notification_alert_on)


@bot.command(name="alertOFF")
async def notyficationOFF(ctx):
    cl_discord_id = bot.user.id  # TODO: remove variable
    removediscordid(cl_discord_id)
    await ctx.author.create_dm()
    await ctx.author.dm_channel.send(hint.notification_alert_off)


#
@bot.event()
async def pushNotification(ctx):
    await ctx.author.id.create_dm()
    await ctx.author.dm_channel.send(hint.notification_alert_off)


@bot.command(name="currency")
async def currencyPrice(ctx):
    embed = embedAdd('Currency Price', 0x008000, "currency")
    await ctx.author.create_dm()
    await ctx.author.dm_channel.send(embed=embed)


@bot.command(name="crypto")
async def cryptoPrice(ctx):
    embed = embedAdd('Crypto Price', 0x008ec2, "crypto")
    await ctx.author.create_dm()
    await ctx.author.dm_channel.send(embed=embed)


@bot.command(name="metals")
async def cmetalsPrice(ctx):
    embed = embedAdd('Metals Price', 0x797e80, "metals")
    await ctx.author.create_dm()
    await ctx.author.dm_channel.send(embed=embed)


bot.run(KEY_API)
