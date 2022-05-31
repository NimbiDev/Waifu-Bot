from distutils.log import error
import discord
import aiohttp

import random
import json

from config import BLUE, PREFIX, RED, PREFIX
from discord.ext import commands


HEADERS = {'User-Agent': f'aiohttp/{aiohttp.__version__}; Waifu-Bot'}

command_attrs = {'hidden': False}


class Waifu(commands.Cog, name='Waifu Commands'):
    def __init__(self, client):
        self.client = client
        self.session = aiohttp.ClientSession()

    def cog_unload(self):
        self.client.loop.create_task(self.session.close())

    @commands.group(name='waifu', description='Get a waifu image from waifu.im.\n\n**Usage**: `w.waifu [subcommand]`', command_attrs=command_attrs)
    @commands.has_guild_permissions(send_messages=True)
    async def _waifu(self, ctx):
        if ctx.author.id == self.client.user.id:
            return

        if ctx.invoked_subcommand is None:

            url = 'https://api.waifu.im/random/?included_tags=waifu'
            async with self.session.get(url, headers=HEADERS) as resp:
                api = await resp.json()
                if resp.status in {200, 201}:
                    url = api['images'][0]['url']
                    e = discord.Embed(color=BLUE)
                    e.set_image(url='{}'.format(url))
                    await ctx.send(embed=e)
                else:
                    error = api['detail']
                    e = discord.Embed(color=RED)
                    e.set_description('```js\n{}\n```'.format(error))
                    await ctx.send(embed=e)

    @_waifu.command(name='random', description='Get a random image from waifu.im.', command_attrs=command_attrs)
    @commands.has_guild_permissions(send_messages=True)
    async def _random(self, ctx):
        if ctx.author.id == self.client.user.id:
            return
        url = 'https://api.waifu.im/random/'
        async with self.session.get(url, headers=HEADERS) as resp:
            api = await resp.json()
            if resp.status in {200, 201}:
                url = api['images'][0]['url']
                e = discord.Embed(color=BLUE)
                e.set_image(url='{}'.format(url))
                await ctx.send(embed=e)
            else:
                error = api['detail']
                e = discord.Embed(color=RED)
                e.set_description('```js\n{}\n```'.format(error))
                await ctx.send(embed=e)

    @_waifu.command(name='maid', description='Get a maid image from waifu.im.', command_attrs=command_attrs)
    @commands.has_guild_permissions(send_messages=True)
    async def _maid(self, ctx):
        if ctx.author.id == self.client.user.id:
            return
        url = 'https://api.waifu.im/random/?included_tags=maid'
        async with self.session.get(url, headers=HEADERS) as resp:
            api = await resp.json()
            if resp.status in {200, 201}:
                url = api['images'][0]['url']
                e = discord.Embed(color=BLUE)
                e.set_image(url='{}'.format(url))
                await ctx.send(embed=e)
            else:
                error = api['detail']
                e = discord.Embed(color=RED)
                e.set_description('```js\n{}\n```'.format(error))
                await ctx.send(embed=e)

    @_waifu.command(name='uniform', description='Get a uniformed waifu image from waifu.im.', command_attrs=command_attrs)
    @commands.has_guild_permissions(send_messages=True)
    async def _uniform(self, ctx):
        if ctx.author.id == self.client.user.id:
            return
        url = 'https://api.waifu.im/random/?included_tages=uniform'
        async with self.session.get(url, headers=HEADERS) as resp:
            api = await resp.json()
            if resp.status in {200, 201}:
                url = api['images'][0]['url']
                e = discord.Embed(color=BLUE)
                e.set_image(url='{}'.format(url))
                await ctx.send(embed=e)
            else:
                error = api['detail']
                e = discord.Embed(color=RED)
                e.set_description('```js\n{}\n```'.format(error))
                await ctx.send(embed=e)

    @_waifu.command(name='selfies', description='Get a selfies waifu image from waifu.im.', command_attrs=command_attrs)
    @commands.has_guild_permissions(send_messages=True)
    async def _selfies(self, ctx):
        if ctx.author.id == self.client.user.id:
            return
        url = 'https://api.waifu.im/random/?included_tags=selfies'
        async with self.session.get(url, headers=HEADERS) as resp:
            api = await resp.json()
            if resp.status in {200, 201}:
                url = api['images'][0]['url']
                e = discord.Embed(color=BLUE)
                e.set_image(url='{}'.format(url))
                await ctx.send(embed=e)
            else:
                error = api['detail']
                e = discord.Embed(color=RED)
                e.set_description('```js\n{}\n```'.format(error))
                await ctx.send(embed=e)

    @_waifu.command(name='oppai', description='Get an Oppai image from waifu.im.', command_attrs=command_attrs)
    @commands.has_guild_permissions(send_messages=True)
    async def _oppai(self, ctx):
        if ctx.author.id == self.client.user.id:
            return
        url = 'https://api.waifu.im/random/?included_tags=oppai'
        async with self.session.get(url, headers=HEADERS) as resp:
            api = await resp.json()
            if resp.status in {200, 201}:
                url = api['images'][0]['url']
                e = discord.Embed(color=BLUE)
                e.set_image(url='{}'.format(url))
                await ctx.send(embed=e)
            else:
                error = api['detail']
                e = discord.Embed(color=RED)
                e.set_description('```js\n{}\n```'.format(error))
                await ctx.send(embed=e)

    @_waifu.command(name='gif', description='Get a gif from waifu.im.', command_attrs=command_attrs)
    @commands.has_guild_permissions(send_messages=True)
    async def _gif(self, ctx):
        if ctx.author.id == self.client.user.id:
            return
        url = 'https://api.waifu.im/random/?gif=true'
        async with self.session.get(url, headers=HEADERS) as resp:
            api = await resp.json()
            if resp.status in {200, 201}:
                url = api['images'][0]['url']
                e = discord.Embed(color=BLUE)
                e.set_image(url='{}'.format(url))
                await ctx.send(embed=e)
            else:
                error = api['detail']
                e = discord.Embed(color=RED)
                e.set_description('```js\n{}\n```'.format(error))
                await ctx.send(embed=e)

    @_waifu.command(name='mori-calliope', description='Get a Mori Calliope image from waifu.im.', command_attrs=command_attrs)
    @commands.has_guild_permissions(send_messages=True)
    async def _mori_calliope(self, ctx):
        if ctx.author.id == self.client.user.id:
            return
        url = 'https://api.waifu.im/random/?included_tags=mori-calliope'
        async with self.session.get(url, headers=HEADERS) as resp:
            api = await resp.json()
            if resp.status in {200, 201}:
                url = api['images'][0]['url']
                e = discord.Embed(color=BLUE)
                e.set_image(url='{}'.format(url))
                await ctx.send(embed=e)
            else:
                error = api['detail']
                e = discord.Embed(color=RED)
                e.set_description('```js\n{}\n```'.format(error))
                await ctx.send(embed=e)

    @_waifu.command(name='raiden-shogun', description='Get a Raiden Shogun image from waifu.im.', command_attrs=command_attrs)
    @commands.has_guild_permissions(send_messages=True)
    async def _raiden_shogun(self, ctx):
        if ctx.author.id == self.client.user.id:
            return
        url = 'https://api.waifu.im/random/?included_tags=raiden-shogun'
        async with self.session.get(url, headers=HEADERS) as resp:
            api = await resp.json()
            if resp.status in {200, 201}:
                url = api['images'][0]['url']
                e = discord.Embed(color=BLUE)
                e.set_image(url='{}'.format(url))
                await ctx.send(embed=e)
            else:
                error = api['detail']
                e = discord.Embed(color=RED)
                e.set_description('```js\n{}\n```'.format(error))
                await ctx.send(embed=e)

    @_waifu.command(name='marin-kitgawa', description='Get a Marin Kitagawa image from waifu.im.', command_attrs=command_attrs)
    @commands.has_guild_permissions(send_messages=True)
    async def _marin_kitagawa(self, ctx):
        if ctx.author.id == self.client.user.id:
            return
        url = 'https://api.waifu.im/random/?included_tags=marin-kitagawa'
        async with self.session.get(url, headers=HEADERS) as resp:
            api = await resp.json()
            if resp.status in {200, 201}:
                url = api['images'][0]['url']
                e = discord.Embed(color=BLUE)
                e.set_image(url='{}'.format(url))
                await ctx.send(embed=e)
            else:
                error = api['detail']
                e = discord.Embed(color=RED)
                e.set_description('```js\n{}\n```'.format(error))
                await ctx.send(embed=e)

    @_waifu.command(name='ass', description='Get a NSFW Ass image from waifu.im.', command_attrs=command_attrs)
    @commands.has_guild_permissions(send_messages=True)
    async def _ass(self, ctx):
        if ctx.author.id == self.client.user.id:
            return
        url = 'https://api.waifu.im/random/?included_tags=ass' \
            '&is_nsfw=true'
        async with self.session.get(url, headers=HEADERS) as resp:
            api = await resp.json()
            if resp.status in {200, 201}:
                url = api['images'][0]['url']
                e = discord.Embed(color=BLUE)
                e.set_image(url='{}'.format(url))
                await ctx.send(embed=e)
            else:
                error = api['detail']
                e = discord.Embed(color=RED)
                e.set_description('```js\n{}\n```'.format(error))
                await ctx.send(embed=e)

    @_waifu.command(name='ero', description='Get a NSFW Ero image from waifu.im.', command_attrs=command_attrs)
    @commands.has_guild_permissions(send_messages=True)
    async def _ero(self, ctx):
        if ctx.author.id == self.client.user.id:
            return
        url = 'https://api.waifu.im/random/?included_tags=ero' \
            '&is_nsfw=true'
        async with self.session.get(url, headers=HEADERS) as resp:
            api = await resp.json()
            if resp.status in {200, 201}:
                url = api['images'][0]['url']
                e = discord.Embed(color=BLUE)
                e.set_image(url='{}'.format(url))
                await ctx.send(embed=e)
            else:
                error = api['detail']
                e = discord.Embed(color=RED)
                e.set_description('```js\n{}\n```'.format(error))
                await ctx.send(embed=e)

    @_waifu.command(name='ecchi', description='Get a NSFW Evvhi image from waifu.im.', command_attrs=command_attrs)
    @commands.has_guild_permissions(send_messages=True)
    async def _ecchi(self, ctx):
        if ctx.author.id == self.client.user.id:
            return
        url = 'https://api.waifu.im/random/?included_tags=ecchi' \
            '&is_nsfw=true'
        async with self.session.get(url, headers=HEADERS) as resp:
            api = await resp.json()
            if resp.status in {200, 201}:
                url = api['images'][0]['url']
                e = discord.Embed(color=BLUE)
                e.set_image(url='{}'.format(url))
                await ctx.send(embed=e)
            else:
                error = api['detail']
                e = discord.Embed(color=RED)
                e.set_description('```js\n{}\n```'.format(error))
                await ctx.send(embed=e)

    @_waifu.command(name='hentai', description='Get a NSFW Hentai image from waifu.im.', command_attrs=command_attrs)
    @commands.has_guild_permissions(send_messages=True)
    async def _hentai(self, ctx):
        if ctx.author.id == self.client.user.id:
            return
        url = 'https://api.waifu.im/random/?included_tags=hentai' \
            '&is_nsfw=true'
        async with self.session.get(url, headers=HEADERS) as resp:
            api = await resp.json()
            if resp.status in {200, 201}:
                url = api['images'][0]['url']
                e = discord.Embed(color=BLUE)
                e.set_image(url='{}'.format(url))
                await ctx.send(embed=e)
            else:
                error = api['detail']
                e = discord.Embed(color=RED)
                e.set_description('```js\n{}\n```'.format(error))
                await ctx.send(embed=e)

    @_waifu.command(name='paizuri', description='Get a NSFW Paizuri image from waifu.im.', command_attrs=command_attrs)
    @commands.has_guild_permissions(send_messages=True)
    async def _paizuri(self, ctx):
        if ctx.author.id == self.client.user.id:
            return
        url = 'https://api.waifu.im/random/?included_tags=paizuri' \
            '&is_nsfw=true'
        async with self.session.get(url, headers=HEADERS) as resp:
            api = await resp.json()
            if resp.status in {200, 201}:
                url = api['images'][0]['url']
                e = discord.Embed(color=BLUE)
                e.set_image(url='{}'.format(url))
                await ctx.send(embed=e)
            else:
                error = api['detail']
                e = discord.Embed(color=RED)
                e.set_description('```js\n{}\n```'.format(error))
                await ctx.send(embed=e)

    @_waifu.command(name='milf', description='Get a NSFW Milf image from waifu.im.', command_attrs=command_attrs)
    @commands.has_guild_permissions(send_messages=True)
    async def _milf(self, ctx):
        if ctx.author.id == self.client.user.id:
            return
        url = 'https://api.waifu.im/random/?included_tags=milf' \
            '&is_nsfw=true'
        async with self.session.get(url, headers=HEADERS) as resp:
            api = await resp.json()
            if resp.status in {200, 201}:
                url = api['images'][0]['url']
                e = discord.Embed(color=BLUE)
                e.set_image(url='{}'.format(url))
                await ctx.send(embed=e)
            else:
                error = api['detail']
                e = discord.Embed(color=RED)
                e.set_description('```js\n{}\n```'.format(error))
                await ctx.send(embed=e)

    @_waifu.command(name='oral', description='Get a NSFW Oral image from waifu.im.', command_attrs=command_attrs)
    @commands.has_guild_permissions(send_messages=True)
    async def _oral(self, ctx):
        if ctx.author.id == self.client.user.id:
            return
        url = 'https://api.waifu.im/random/?included_tags=oral' \
            '&is_nsfw=true'
        async with self.session.get(url, headers=HEADERS) as resp:
            api = await resp.json()
            if resp.status in {200, 201}:
                url = api['images'][0]['url']
                e = discord.Embed(color=BLUE)
                e.set_image(url='{}'.format(url))
                await ctx.send(embed=e)
            else:
                error = api['detail']
                e = discord.Embed(color=RED)
                e.set_description('```js\n{}\n```'.format(error))
                await ctx.send(embed=e)


def setup(client):
    client.add_cog(Waifu(client))
