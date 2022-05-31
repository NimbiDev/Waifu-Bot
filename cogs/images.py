from distutils.log import error
import discord
import aiohttp
import TenGiphPy

import random
import json
        

from config import DARKPINK, EMBED_THUMBNAIL, PREFIX, RED, GREEN, PREFIX, RANDOM, TENOR_API
from discord.ext import commands

TOKENS = {'TENOR_API': TENOR_API}
TENOR = TenGiphPy.Tenor(token=TOKENS['TENOR_API'])

HEADERS = {'User-Agent': f'aiohttp/{aiohttp.__version__}; Waifu-Bot'}

command_attrs = {'hidden': False}


class Images(commands.Cog, name='Image Commands'):
    def __init__(self, client):
        self.client = client
        self.session = aiohttp.ClientSession()

    def cog_unload(self):
        self.client.loop.create_task(self.session.close())

    @commands.command(name='waifu', description='Get a random waifu by tag from waifu.im.\n\n**Example**: {}waifu maid'.format(PREFIX), command_attrs=command_attrs)
    @commands.has_guild_permissions(send_messages=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def _waifu(self, ctx, *, args):
        if ctx.author.id == self.client.user.id:
            return
        url = 'https://api.waifu.im/random/?{}=true'.format(args)
        async with self.session.get(url, headers=HEADERS) as resp:
            api = await resp.json()
            if resp.status in {200, 201}:
                url = api['images'][0]['url']
                e = discord.Embed(color=str(DARKPINK))
                e.set_image(url='{}'.format(url))
                await ctx.send(embed=e)
            else:
                error = api['detail']
                e = discord.Embed(color=RED)
                e.set_description('```js\n{}\n```'.format(error))
                await ctx.send(embed=e)
    
    @commands.command(aliases=['gif'], description='Return a random gif by tag from tenor.\nSeperate multiple tags with `+`.\n\n**Example**: `{}tenor anime+hug`'.format(PREFIX), command_attrs=command_attrs)
    @commands.has_guild_permissions(send_messages=True, embed_links=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def tenor(self, ctx, *, query):
        tenorUrl = await TENOR.arandom(str(query))
        e = discord.Embed(colour=RANDOM)
        e.set_image(url=tenorUrl)
        await ctx.send(embed=e, mention_author=False)



def setup(client):
    client.add_cog(Images(client))