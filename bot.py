import discord
from discord.ext import commands
import asyncio
import os
import sys
import time
import json
import random
import urbandict
import datetime as dt
import datetime
import json, asyncio
import copy
import logging
import traceback
import aiohttp
import urllib.parse
from collections                import Counter

verison = "0.1"
command_prefix = ['m!', '<@411609402911490049> ', '<@!411609402911490049> ' ] #CHANGE IT TO WHAT YOU WANT
description = "DatBot" #ALSO CHANGE THIS
bot = commands.Bot(command_prefix, description = description, owner_id = 282088833082720256)
bot.remove_command('help')
tu = datetime.datetime.now()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print(verison)


startup_extensions = ["cogs.commands"]


@bot.command()
@commands.is_owner()
async def load(ctx, extension_name : str):
    """Loads an extension."""
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        ctx.send("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
        ctx.send("{} loaded.".format(extension_name))

@bot.command()
@commands.is_owner()
async def todo(ctx):
    if commands.is_owner is False:
        await ctx.send("Your not my owner!")
    else:
        e = discord.Embed(title="Do this by the date given(DEV ONLY)",color=0xFF0000)
        e.add_field(name="Help Command", value="Do me by tomorrow plz")
        await ctx.send(embed=e)

@bot.command()
async def poll(ctx, *, message):
    author = ctx.message.author
    embed = discord.Embed(color=author.color, timestamp=datetime.datetime.utcnow())
    embed.set_author(name="Poll", icon_url=author.avatar_url)
    embed.description = message
    embed.set_footer(text=author.name)
    x = await ctx.send(embed=embed)
    await x.add_reaction("👍")
    await x.add_reaction("\U0001f937")
    await x.add_reaction("👎")

@bot.command()
async def minecraft(ctx):
    await ctx.send('cancer')



@bot.command()
async def hug(ctx, *, member: discord.Member = None):
    if member is None:
        embed=discord.Embed(title="Mention someone to hug!", description="{} You must mention someone to hug!".format(ctx.message.author.mention), color=0xff0000)
        embed.set_thumbnail(url="https://assets-auto.rbl.ms/c0f5fa68ff7c7a92e99330629790efee24cc9d02c3af953e3535e39ea842a21e")
        embed.set_footer(text="Developed by Jupiter#0001")
        await ctx.send(embed=embed)
    elif member.id == ctx.message.author.id:
        embed=discord.Embed(title="Well ok go ahead and hug yourself", description="{} tryed to hug themselves!".format(ctx.message.author.mention), color=0xff0000)
        embed.set_thumbnail(url="https://m.popkey.co/ac8118/v0kR5.gif")
        embed.set_footer(text="Developed By Jupiter#0001")
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="Hugged", description="{} Hugged {} CUTE!".format(ctx.message.author.mention, member.mention), color=0xff0000)
        embed.set_image(url="https://media.giphy.com/media/k6SMGojsRMMpy/giphy.gif")
        embed.set_footer(text="Developed by Jupiter#0001")
        await ctx.send(embed=embed)

@bot.command()
async def urban(ctx, *, word: str):
    """Browse Urban Dictionary."""
    defi = urbandict.define(word)

    definition = defi[0]['def'] #definition of the word
    example = defi[0]['example'] #example of usage (if available)

    #make an embedded message colored blue
    embed = discord.Embed(title=word, description=definition, color=0x0062f4)
    embed.add_field(name = "Example", value = example, inline = False)
    embed.set_footer(text="Urban Dictionary", icon_url='https://vignette.wikia.nocookie.net/logopedia/images/a/a7/UDAppIcon.jpg/revision/latest?cb=20170422211150')
    embed.set_thumbnail(url='https://s3.amazonaws.com/pushbullet-uploads/ujxPklLhvyK-RGDsDKNxGPDh29VWVd5iJOh8hkiBTRyC/urban_dictionary.jpg?w=188&h=188&fit=crop')
    await ctx.send(embed=embed)

@bot.command()
async def kill(ctx, *, member: discord.Member = None):
    if member is None:
        embed=discord.Embed(title="No one to kill!", description="You havent mentioned anyone to kill!", color=0xff0000)
        embed.set_thumbnail(url="http://i.imgur.com/6YToyEF.png")
        embed.set_footer(text="Developed by Jupiter#0001")
        await ctx.send(embed=embed)
    elif member.id == ctx.message.author.id:
        embed=discord.Embed(title="Call this number", description="1-800-784-2433", color=0xff0000)
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/NHS-Logo.svg/1200px-NHS-Logo.svg.png")
        embed.set_image(url="http://4.bp.blogspot.com/-FL6mKTZOk94/UBb_9EuAYNI/AAAAAAAAOco/JWsTlyInMeQ/s400/Jean+Reno.gif")
        embed.set_footer(text="Developed by Jupiter#0001")
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="Killed!", description="{} Was killed by {} OOF ".format(member.mention, ctx.message.author.name),color=0xff0000)
        embed.set_image(url="https://media.giphy.com/media/kOA5F569qO4RG/giphy.gif")
        embed.set_footer(text="Developed by Jupiter#0001")
        await ctx.send(embed=embed)


@bot.command()
@commands.is_owner()
async def unload(ctx, extension_name : str):
    """Unloads an extension."""
    bot.unload_extension(extension_name)
    ctx.send("{} unloaded.".format(extension_name))


if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n'.format(extension))

bot.run('')
