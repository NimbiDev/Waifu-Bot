from distutils.log import error
import discord
import aiohttp
import TenGiphPy

import random
import json
        

from config import BLUE, EMBED_THUMBNAIL, PREFIX, RED, GREEN, PREFIX, RANDOM, TENOR_API
from discord.ext import commands

TOKENS = {'TENOR_API': TENOR_API}
TENOR = TenGiphPy.Tenor(token=TOKENS['TENOR_API'])

command_attrs = {'hidden': False}


class Images(commands.Cog, name='Image Commands'):
    def __init__(self, client):
        self.client = client
        self.session = aiohttp.ClientSession()

    def cog_unload(self):
        self.client.loop.create_task(self.session.close())
    
    @commands.command(name='tenor', description='Return a random gif by tag from tenor.\nSeperate multiple tags with `+`.\n\n**Example**: `{}tenor anime+hug`'.format(PREFIX), command_attrs=command_attrs)
    @commands.has_guild_permissions(send_messages=True, embed_links=True)
    async def _tenor(self, ctx, *, tag):
        tenorUrl = await TENOR.arandom(str(tag))
        e = discord.Embed(colour=BLUE)
        e.set_image(url=tenorUrl)
        await ctx.send(embed=e, mention_author=False)



def setup(client):
    client.add_cog(Images(client))