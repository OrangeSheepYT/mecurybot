import discord
from discord.ext import commands
import asyncio
import os
import sys
import time
import json
import random
import datetime as dt
import datetime
import json, asyncio
import copy
import logging
import traceback
import aiohttp
import urllib.parse
from collections                import Counter


class Commands():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        e = discord.Embed(title="Help - Commands [2]", inline=False,color=0xFF0000)
        e.add_field(name="Bot Related - [1]", value = "`ping`", inline=False)
        e.add_field(name="Fun - [6]", value="`pfp` `poll`  `kill` `hug` `roblox` `minecraft` `cat` `dog`", inline=False)
        e.add_field(name="Developer - [3]", value= "`load`, `unload`, `todo`", inline=False)
        e.set_footer(text="More commands will be added soon.")
        await ctx.send(embed=e)

    @commands.command()
    async def ping(self, ctx):
        e = discord.Embed(title="Pong! :ping_pong:",color=0xFF0000)
        await ctx.send(embed=e)

    @commands.command(aliases=['av', 'pfp'])
    async def avatar(self, ctx, *, member: discord.Member = None):
        '''Gets someones pfp'''
        member = member or ctx.author
        av = member.avatar_url
        if ".gif" in av:
            av += "&f=.gif"
        em = discord.Embed(url=av, color=0xffffff)
        em.set_author(name=str(member), icon_url=av)
        em.set_image(url=av)
        await ctx.send(embed=em)

    @commands.command(pass_context=True)
    async def dog(self, ctx):
        api = "https://api.thedogapi.co.uk/v2/dog.php"
        async with aiohttp.ClientSession() as session:
            async with session.get(api) as r:
                if r.status == 200:
                    response = await r.json()
                    embed = discord.Embed(color = 0x00ff44)
                    embed.set_author(name = "{} here is your random dog".format(ctx.message.author.name))
                    embed.set_image(url = response['data'][0]["url"])
                    await ctx.send(embed = embed)


    @commands.command()
    async def cat(self, ctx):
        """Random cat images. Awww, so cute! Powered by random.cat"""
        api = "https://random.cat/meow"
        async with aiohttp.ClientSession() as session:
            async with session.get(api) as r:
                if r.status == 200:
                    js = await r.json()
                    em = discord.Embed(name='random.cat', colour=0x690E8)
                    em.set_image(url=js['file'])
                    await ctx.send(embed=em)
                else:
                    raise utils.errors.ServiceError(f'could not fetch cute cat :( (http {r.status})')

    @commands.command()
    async def roblox(self, ctx):
        embed = discord.Embed(title="Roblox", description="is a meme")
        embed.set_thumbnail(url="https://microsoft.such-a-me.me/vsCyOhkCU.png")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Commands(bot))
