import discord
from databasemodule import takeprice


def embedAdd(title, hexColor):
    embed = discord.Embed(title=title, color=hexColor)
    take_price = takeprice("currency")
    i = 0
    for x in take_price:
        embed.add_field(name=f"{take_price[i][1]}", value=f"{take_price[i][0]}", inline=False)
        i += 1
    return embed
