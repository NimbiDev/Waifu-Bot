from distutils.log import error
from secrets import choice
import discord
import aiohttp
import TenGiphPy

import random
import json
        

from config import BLUE, PREFIX, RED, PREFIX, TENOR_API
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
    
    @commands.command(name='tenor', description='Display a random gif by tag from tenor.\nSeperate multiple tags with `+`.\n\n**Example**: `{}tenor anime+hug`'.format(PREFIX), command_attrs=command_attrs)
    @commands.has_guild_permissions(send_messages=True, embed_links=True)
    async def _tenor(self, ctx, *, tag):
        tenorUrl = await TENOR.arandom(str(tag))
        e = discord.Embed(colour=BLUE)
        e.set_image(url=tenorUrl)
        await ctx.send(embed=e, mention_author=False)

    @commands.group(name='waifu', breif='Display a waifu image from waifu.im', description='Display a waifu image from waifu.im.\n\n**Usage**: `w.waifu [tag] [filter]`', command_attrs=command_attrs)
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
                    e = discord.Embed(
                        color=BLUE, description='**Direct Link**: [waifu.im]({})'.format(url))
                    e.set_image(url='{}'.format(url))
                    await ctx.send(embed=e)
                else:
                    error = api['detail']
                    e = discord.Embed(color=RED)
                    e.set_description('```js\n{}\n```'.format(error))
                    await ctx.send(embed=e)

    @_waifu.group(name='random', description='Display a random image from waifu.im.', command_attrs=command_attrs)
    @commands.has_guild_permissions(send_messages=True)
    async def _random(self, ctx):
        if ctx.author.id == self.client.user.id:
            return
        url = 'https://api.waifu.im/random/'

        if ctx.invoked_subcommand is None:

            async with self.session.get(url, headers=HEADERS) as resp:
                api = await resp.json()
                if resp.status in {200, 201}:
                    url = api['images'][0]['url']
                    e = discord.Embed(
                        color=BLUE, description='**Direct Link**: [waifu.im]({})'.format(url))
                    e.set_image(url='{}'.format(url))
                    await ctx.send(embed=e)
                else:
                    error = api['detail']
                    e = discord.Embed(color=RED)
                    e.set_description('```js\n{}\n```'.format(error))
                    await ctx.send(embed=e)

    @_waifu.group(name='maid', description='Display a maid image from waifu.im.', command_attrs=command_attrs)
    @commands.has_guild_permissions(send_messages=True)
    async def _maid(self, ctx):
        if ctx.author.id == self.client.user.id:
            return
        url = 'https://api.waifu.im/random/?included_tags=maid'

        if ctx.invoked_subcommand is None:

            async with self.session.get(url, headers=HEADERS) as resp:
                api = await resp.json()
                if resp.status in {200, 201}:
                    url = api['images'][0]['url']
                    e = discord.Embed(
                        color=BLUE, description='**Direct Link**: [waifu.im]({})'.format(url))
                    e.set_image(url='{}'.format(url))
                    await ctx.send(embed=e)
                else:
                    error = api['detail']
                    e = discord.Embed(color=RED)
                    e.set_description('```js\n{}\n```'.format(error))
                    await ctx.send(embed=e)

    @_waifu.group(name='uniform', description='Display a uniformed waifu image from waifu.im.', command_attrs=command_attrs)
    @commands.has_guild_permissions(send_messages=True)
    async def _uniform(self, ctx):
        if ctx.author.id == self.client.user.id:
            return
        url = 'https://api.waifu.im/random/?included_tages=uniform'

        if ctx.invoked_subcommand is None:

            async with self.session.get(url, headers=HEADERS) as resp:
                api = await resp.json()
                if resp.status in {200, 201}:
                    url = api['images'][0]['url']
                    e = discord.Embed(
                        color=BLUE, description='**Direct Link**: [waifu.im]({})'.format(url))
                    e.set_image(url='{}'.format(url))
                    await ctx.send(embed=e)
                else:
                    error = api['detail']
                    e = discord.Embed(color=RED)
                    e.set_description('```js\n{}\n```'.format(error))
                    await ctx.send(embed=e)

    @_waifu.group(name='selfies', description='Display a selfies waifu image from waifu.im.', command_attrs=command_attrs)
    @commands.has_guild_permissions(send_messages=True)
    async def _selfies(self, ctx):
        if ctx.author.id == self.client.user.id:
            return
        url = 'https://api.waifu.im/random/?included_tags=selfies'

        if ctx.invoked_subcommand is None:

            async with self.session.get(url, headers=HEADERS) as resp:
                api = await resp.json()
                if resp.status in {200, 201}:
                    url = api['images'][0]['url']
                    e = discord.Embed(
                        color=BLUE, description='**Direct Link**: [waifu.im]({})'.format(url))
                    e.set_image(url='{}'.format(url))
                    await ctx.send(embed=e)
                else:
                    error = api['detail']
                    e = discord.Embed(color=RED)
                    e.set_description('```js\n{}\n```'.format(error))
                    await ctx.send(embed=e)

    @_waifu.group(name='oppai', description='Display an Oppai image from waifu.im.', command_attrs=command_attrs)
    @commands.has_guild_permissions(send_messages=True)
    async def _oppai(self, ctx):
        if ctx.author.id == self.client.user.id:
            return
        url = 'https://api.waifu.im/random/?included_tags=oppai'

        if ctx.invoked_subcommand is None:

            async with self.session.get(url, headers=HEADERS) as resp:
                api = await resp.json()
                if resp.status in {200, 201}:
                    url = api['images'][0]['url']
                    e = discord.Embed(
                        color=BLUE, description='**Direct Link**: [waifu.im]({})'.format(url))
                    e.set_image(url='{}'.format(url))
                    await ctx.send(embed=e)
                else:
                    error = api['detail']
                    e = discord.Embed(color=RED)
                    e.set_description('```js\n{}\n```'.format(error))
                    await ctx.send(embed=e)

    @_waifu.group(name='gif', description='Display a gif from waifu.im.', command_attrs=command_attrs)
    @commands.has_guild_permissions(send_messages=True)
    async def _gif(self, ctx):
        if ctx.author.id == self.client.user.id:
            return
        url = 'https://api.waifu.im/random/?gif=true'

        if ctx.invoked_subcommand is None:

            async with self.session.get(url, headers=HEADERS) as resp:
                api = await resp.json()
                if resp.status in {200, 201}:
                    url = api['images'][0]['url']
                    e = discord.Embed(
                        color=BLUE, description='**Direct Link**: [waifu.im]({})'.format(url))
                    e.set_image(url='{}'.format(url))
                    await ctx.send(embed=e)
                else:
                    error = api['detail']
                    e = discord.Embed(color=RED)
                    e.set_description('```js\n{}\n```'.format(error))
                    await ctx.send(embed=e)

    @_waifu.group(name='mori-calliope', description='Display a Mori Calliope image from waifu.im.', command_attrs=command_attrs)
    @commands.has_guild_permissions(send_messages=True)
    async def _mori_calliope(self, ctx):
        if ctx.author.id == self.client.user.id:
            return
        url = 'https://api.waifu.im/random/?included_tags=mori-calliope'

        if ctx.invoked_subcommand is None:

            async with self.session.get(url, headers=HEADERS) as resp:
                api = await resp.json()
                if resp.status in {200, 201}:
                    url = api['images'][0]['url']
                    e = discord.Embed(
                        color=BLUE, description='**Direct Link**: [waifu.im]({})'.format(url))
                    e.set_image(url='{}'.format(url))
                    await ctx.send(embed=e)
                else:
                    error = api['detail']
                    e = discord.Embed(color=RED)
                    e.set_description('```js\n{}\n```'.format(error))
                    await ctx.send(embed=e)

    @_waifu.group(name='raiden-shogun', description='Display a Raiden Shogun image from waifu.im.', command_attrs=command_attrs)
    @commands.has_guild_permissions(send_messages=True)
    async def _raiden_shogun(self, ctx):
        if ctx.author.id == self.client.user.id:
            return
        url = 'https://api.waifu.im/random/?included_tags=raiden-shogun'

        if ctx.invoked_subcommand is None:

            async with self.session.get(url, headers=HEADERS) as resp:
                api = await resp.json()
                if resp.status in {200, 201}:
                    url = api['images'][0]['url']
                    e = discord.Embed(
                        color=BLUE, description='**Direct Link**: [waifu.im]({})'.format(url))
                    e.set_image(url='{}'.format(url))
                    await ctx.send(embed=e)
                else:
                    error = api['detail']
                    e = discord.Embed(color=RED)
                    e.set_description('```js\n{}\n```'.format(error))
                    await ctx.send(embed=e)

    @_waifu.group(name='marin-kitgawa', description='Display a Marin Kitagawa image from waifu.im.', command_attrs=command_attrs)
    @commands.has_guild_permissions(send_messages=True)
    async def _marin_kitagawa(self, ctx):
        if ctx.author.id == self.client.user.id:
            return
        url = 'https://api.waifu.im/random/?included_tags=marin-kitagawa'

        if ctx.invoked_subcommand is None:

            async with self.session.get(url, headers=HEADERS) as resp:
                api = await resp.json()
                if resp.status in {200, 201}:
                    url = api['images'][0]['url']
                    e = discord.Embed(
                        color=BLUE, description='**Direct Link**: [waifu.im]({})'.format(url))
                    e.set_image(url='{}'.format(url))
                    await ctx.send(embed=e)
                else:
                    error = api['detail']
                    e = discord.Embed(color=RED)
                    e.set_description('```js\n{}\n```'.format(error))
                    await ctx.send(embed=e)

    @_waifu.group(name='ass', description='Display a NSFW Ass image from waifu.im.', command_attrs=command_attrs)
    @commands.is_nsfw()
    @commands.has_guild_permissions(send_messages=True)
    async def _ass(self, ctx):
        if ctx.author.id == self.client.user.id:
            return
        url = 'https://api.waifu.im/random/?included_tags=ass' \
            '&is_nsfw=true'

        if ctx.invoked_subcommand is None:

            async with self.session.get(url, headers=HEADERS) as resp:
                api = await resp.json()
                if resp.status in {200, 201}:
                    url = api['images'][0]['url']
                    e = discord.Embed(
                        color=BLUE, description='**Direct Link**: [waifu.im]({})'.format(url))
                    e.set_image(url='{}'.format(url))
                    await ctx.send(embed=e)
                else:
                    error = api['detail']
                    e = discord.Embed(color=RED)
                    e.set_description('```js\n{}\n```'.format(error))
                    await ctx.send(embed=e)

    @_waifu.group(name='ero', description='Display a NSFW Ero image from waifu.im.', command_attrs=command_attrs)
    @commands.is_nsfw()
    @commands.has_guild_permissions(send_messages=True)
    async def _ero(self, ctx):
        if ctx.author.id == self.client.user.id:
            return
        url = 'https://api.waifu.im/random/?included_tags=ero' \
            '&is_nsfw=true'

        if ctx.invoked_subcommand is None:

            async with self.session.get(url, headers=HEADERS) as resp:
                api = await resp.json()
                if resp.status in {200, 201}:
                    url = api['images'][0]['url']
                    e = discord.Embed(
                        color=BLUE, description='**Direct Link**: [waifu.im]({})'.format(url))
                    e.set_image(url='{}'.format(url))
                    await ctx.send(embed=e)
                else:
                    error = api['detail']
                    e = discord.Embed(color=RED)
                    e.set_description('```js\n{}\n```'.format(error))
                    await ctx.send(embed=e)

    @_waifu.group(name='ecchi', description='Display a NSFW Evvhi image from waifu.im.', command_attrs=command_attrs)
    @commands.is_nsfw()
    @commands.has_guild_permissions(send_messages=True)
    async def _ecchi(self, ctx):
        if ctx.author.id == self.client.user.id:
            return
        url = 'https://api.waifu.im/random/?included_tags=ecchi' \
            '&is_nsfw=true'

        if ctx.invoked_subcommand is None:

            async with self.session.get(url, headers=HEADERS) as resp:
                api = await resp.json()
                if resp.status in {200, 201}:
                    url = api['images'][0]['url']
                    e = discord.Embed(
                        color=BLUE, description='**Direct Link**: [waifu.im]({})'.format(url))
                    e.set_image(url='{}'.format(url))
                    await ctx.send(embed=e)
                else:
                    error = api['detail']
                    e = discord.Embed(color=RED)
                    e.set_description('```js\n{}\n```'.format(error))
                    await ctx.send(embed=e)

    @_waifu.group(name='hentai', description='Display a NSFW Hentai image from waifu.im.', command_attrs=command_attrs)
    @commands.is_nsfw()
    @commands.has_guild_permissions(send_messages=True)
    async def _hentai(self, ctx, tag, choice):
        if ctx.author.id == self.client.user.id:
            return
        url = f'https://api.waifu.im/random/?included_tags={tag}' \
            f'&is_nsfw={choice}'

        if ctx.invoked_subcommand is None:

            async with self.session.get(url, headers=HEADERS) as resp:
                api = await resp.json()
                if resp.status in {200, 201}:
                    url = api['images'][0]['url']
                    e = discord.Embed(
                        color=BLUE, description='**Direct Link**: [waifu.im]({})'.format(url))
                    e.set_image(url='{}'.format(url))
                    await ctx.send(embed=e)
                else:
                    error = api['detail']
                    e = discord.Embed(color=RED)
                    e.set_description('```js\n{}\n```'.format(error))
                    await ctx.send(embed=e)

    @_waifu.group(name='paizuri', description='Display a NSFW Paizuri image from waifu.im.', command_attrs=command_attrs)
    @commands.is_nsfw()
    @commands.has_guild_permissions(send_messages=True)
    async def _paizuri(self, ctx):
        if ctx.author.id == self.client.user.id:
            return
        url = 'https://api.waifu.im/random/?included_tags=paizuri' \
            '&is_nsfw=true'

        if ctx.invoked_subcommand is None:

            async with self.session.get(url, headers=HEADERS) as resp:
                api = await resp.json()
                if resp.status in {200, 201}:
                    url = api['images'][0]['url']
                    e = discord.Embed(
                        color=BLUE, description='**Direct Link**: [waifu.im]({})'.format(url))
                    e.set_image(url='{}'.format(url))
                    await ctx.send(embed=e)
                else:
                    error = api['detail']
                    e = discord.Embed(color=RED)
                    e.set_description('```js\n{}\n```'.format(error))
                    await ctx.send(embed=e)

    @_waifu.group(name='milf', description='Display a NSFW Milf image from waifu.im.', command_attrs=command_attrs)
    @commands.is_nsfw()
    @commands.has_guild_permissions(send_messages=True)
    async def _milf(self, ctx):
        if ctx.author.id == self.client.user.id:
            return
        url = 'https://api.waifu.im/random/?included_tags=milf' \
            '&is_nsfw=true'

        if ctx.invoked_subcommand is None:

            async with self.session.get(url, headers=HEADERS) as resp:
                api = await resp.json()
                if resp.status in {200, 201}:
                    url = api['images'][0]['url']
                    e = discord.Embed(
                        color=BLUE, description='**Direct Link**: [waifu.im]({})'.format(url))
                    e.set_image(url='{}'.format(url))
                    await ctx.send(embed=e)
                else:
                    error = api['detail']
                    e = discord.Embed(color=RED)
                    e.set_description('```js\n{}\n```'.format(error))
                    await ctx.send(embed=e)

    @_waifu.group(name='oral', description='Display a NSFW Oral image from waifu.im.', command_attrs=command_attrs)
    @commands.is_nsfw()
    @commands.has_guild_permissions(send_messages=True)
    async def _oral(self, ctx):
        if ctx.author.id == self.client.user.id:
            return
        url = 'https://api.waifu.im/random/?included_tags=oral' \
            '&is_nsfw=true'

        if ctx.invoked_subcommand is None:

            async with self.session.get(url, headers=HEADERS) as resp:
                api = await resp.json()
                if resp.status in {200, 201}:
                    url = api['images'][0]['url']
                    e = discord.Embed(
                        color=BLUE, description='**Direct Link**: [waifu.im]({})'.format(url))
                    e.set_image(url='{}'.format(url))
                    await ctx.send(embed=e)
                else:
                    error = api['detail']
                    e = discord.Embed(color=RED)
                    e.set_description('```js\n{}\n```'.format(error))
                    await ctx.send(embed=e)

    @_oral.command(name='gif', description='Return a gif of the selected tag', command_attrs=command_attrs) 
    @commands.is_nsfw()
    @commands.has_guild_permissions(send_messages=True)
    async def _oral_gif(self, ctx):
        if ctx.author.id == self.client.user.id:
            return
        url = 'https://api.waifu.im/random/?included_tags=oral' \
            '&is_nsfw=true' \
            '&gif=true'
        async with self.session.get(url, headers=HEADERS) as resp:
            api = await resp.json()
            if resp.status in {200, 201}:
                url = api['images'][0]['url']
                e = discord.Embed(
                    color=BLUE, description='**Direct Link**: [waifu.im]({})'.format(url))
                e.set_image(url='{}'.format(url))
                await ctx.send(embed=e)
            else:
                error = api['detail']
                e = discord.Embed(color=RED)
                e.set_description('```js\n{}\n```'.format(error))
                await ctx.send(embed=e)

    @_hentai.command(name='gif', description='Return a gif of the selected tag', command_attrs=command_attrs)
    @commands.is_nsfw()
    @commands.has_guild_permissions(send_messages=True)
    async def _hentai_gif(self, ctx):
        if ctx.author.id == self.client.user.id:
            return
        url = 'https://api.waifu.im/random/?included_tags=hentai' \
            '&is_nsfw=true' \
            '&gif=true'
        async with self.session.get(url, headers=HEADERS) as resp:
            api = await resp.json()
            if resp.status in {200, 201}:
                url = api['images'][0]['url']
                e = discord.Embed(
                    color=BLUE, description='**Direct Link**: [waifu.im]({})'.format(url))
                e.set_image(url='{}'.format(url))
                await ctx.send(embed=e)
            else:
                error = api['detail']
                e = discord.Embed(color=RED)
                e.set_description('```js\n{}\n```'.format(error))
                await ctx.send(embed=e)
    
    @_ass.command(name='gif', description='Return a gif of the selected tag', command_attrs=command_attrs)
    @commands.is_nsfw()
    @commands.has_guild_permissions(send_messages=True)
    async def _ass_gif(self, ctx):
        if ctx.author.id == self.client.user.id:
            return
        url = 'https://api.waifu.im/random/?included_tags=ass' \
            '&is_nsfw=true' \
            '&gif=true'
        async with self.session.get(url, headers=HEADERS) as resp:
            api = await resp.json()
            if resp.status in {200, 201}:
                url = api['images'][0]['url']
                e = discord.Embed(
                    color=BLUE, description='**Direct Link**: [waifu.im]({})'.format(url))
                e.set_image(url='{}'.format(url))
                await ctx.send(embed=e)
            else:
                error = api['detail']
                e = discord.Embed(color=RED)
                e.set_description('```js\n{}\n```'.format(error))
                await ctx.send(embed=e)

    @_milf.command(name='gif', description='Return a gif of the selected tag', command_attrs=command_attrs)
    @commands.is_nsfw()
    @commands.has_guild_permissions(send_messages=True)
    async def _milf_gif(self, ctx):
        if ctx.author.id == self.client.user.id:
            return
        url = 'https://api.waifu.im/random/?included_tags=milf' \
            '&is_nsfw=true' \
            '&gif=true'
        async with self.session.get(url, headers=HEADERS) as resp:
            api = await resp.json()
            if resp.status in {200, 201}:
                url = api['images'][0]['url']
                e = discord.Embed(
                    color=BLUE, description='**Direct Link**: [waifu.im]({})'.format(url))
                e.set_image(url='{}'.format(url))
                await ctx.send(embed=e)
            else:
                error = api['detail']
                e = discord.Embed(color=RED)
                e.set_description('```js\n{}\n```'.format(error))
                await ctx.send(embed=e)

    @_ecchi.command(name='gif', description='Return a gif of the selected tag', command_attrs=command_attrs)
    @commands.is_nsfw()
    @commands.has_guild_permissions(send_messages=True)
    async def _ecchi_gif(self, ctx):
        if ctx.author.id == self.client.user.id:
            return
        url = 'https://api.waifu.im/random/?included_tags=ecchi' \
            '&is_nsfw=true' \
            '&gif=true'
        async with self.session.get(url, headers=HEADERS) as resp:
            api = await resp.json()
            if resp.status in {200, 201}:
                url = api['images'][0]['url']
                e = discord.Embed(
                    color=BLUE, description='**Direct Link**: [waifu.im]({})'.format(url))
                e.set_image(url='{}'.format(url))
                await ctx.send(embed=e)
            else:
                error = api['detail']
                e = discord.Embed(color=RED)
                e.set_description('```js\n{}\n```'.format(error))
                await ctx.send(embed=e)

    @_ero.command(name='gif', description='Return a gif of the selected tag', command_attrs=command_attrs)
    @commands.is_nsfw()
    @commands.has_guild_permissions(send_messages=True)
    async def _ero_gif(self, ctx):
        if ctx.author.id == self.client.user.id:
            return
        url = 'https://api.waifu.im/random/?included_tags=ero' \
            '&is_nsfw=true' \
            '&gif=true'
        async with self.session.get(url, headers=HEADERS) as resp:
            api = await resp.json()
            if resp.status in {200, 201}:
                url = api['images'][0]['url']
                e = discord.Embed(
                    color=BLUE, description='**Direct Link**: [waifu.im]({})'.format(url))
                e.set_image(url='{}'.format(url))
                await ctx.send(embed=e)
            else:
                error = api['detail']
                e = discord.Embed(color=RED)
                e.set_description('```js\n{}\n```'.format(error))
                await ctx.send(embed=e)

    @_paizuri.command(name='gif', description='Return a gif of the selected tag', command_attrs=command_attrs)
    @commands.is_nsfw()
    @commands.has_guild_permissions(send_messages=True)
    async def _paizuri_gif(self, ctx):
        if ctx.author.id == self.client.user.id:
            return
        url = 'https://api.waifu.im/random/?included_tags=paizuri' \
            '&is_nsfw=true' \
            '&gif=true'
        async with self.session.get(url, headers=HEADERS) as resp:
            api = await resp.json()
            if resp.status in {200, 201}:
                url = api['images'][0]['url']
                e = discord.Embed(
                    color=BLUE, description='**Direct Link**: [waifu.im]({})'.format(url))
                e.set_image(url='{}'.format(url))
                await ctx.send(embed=e)
            else:
                error = api['detail']
                e = discord.Embed(color=RED)
                e.set_description('```js\n{}\n```'.format(error))
                await ctx.send(embed=e)

    @_random.command(name='gif', description='Return a gif of the selected tag', command_attrs=command_attrs)
    @commands.has_guild_permissions(send_messages=True)
    async def _random_gif(self, ctx):
        if ctx.author.id == self.client.user.id:
            return
        url = 'https://api.waifu.im/random/?gif=true'
        async with self.session.get(url, headers=HEADERS) as resp:
            api = await resp.json()
            if resp.status in {200, 201}:
                url = api['images'][0]['url']
                e = discord.Embed(
                    color=BLUE, description='**Direct Link**: [waifu.im]({})'.format(url))
                e.set_image(url='{}'.format(url))
                await ctx.send(embed=e)
            else:
                error = api['detail']
                e = discord.Embed(color=RED)
                e.set_description('```js\n{}\n```'.format(error))
                await ctx.send(embed=e)

    @_maid.command(name='gif', description='Return a gif of the selected tag', command_attrs=command_attrs)
    @commands.has_guild_permissions(send_messages=True)
    async def _maid_gif(self, ctx):
        if ctx.author.id == self.client.user.id:
            return
        url = 'https://api.waifu.im/random/?included_tags=maid' \
            '&gif=true'
        async with self.session.get(url, headers=HEADERS) as resp:
            api = await resp.json()
            if resp.status in {200, 201}:
                url = api['images'][0]['url']
                e = discord.Embed(
                    color=BLUE, description='**Direct Link**: [waifu.im]({})'.format(url))
                e.set_image(url='{}'.format(url))
                await ctx.send(embed=e)
            else:
                error = api['detail']
                e = discord.Embed(color=RED)
                e.set_description('```js\n{}\n```'.format(error))
                await ctx.send(embed=e)

    @_oppai.command(name='gif', description='Return a gif of the selected tag', command_attrs=command_attrs)
    @commands.has_guild_permissions(send_messages=True)
    async def _oppai_gif(self, ctx):
        if ctx.author.id == self.client.user.id:
            return
        url = 'https://api.waifu.im/random/?included_tags=oppai' \
            '&gif=true'
        async with self.session.get(url, headers=HEADERS) as resp:
            api = await resp.json()
            if resp.status in {200, 201}:
                url = api['images'][0]['url']
                e = discord.Embed(
                    color=BLUE, description='**Direct Link**: [waifu.im]({})'.format(url))
                e.set_image(url='{}'.format(url))
                await ctx.send(embed=e)
            else:
                error = api['detail']
                e = discord.Embed(color=RED)
                e.set_description('```js\n{}\n```'.format(error))
                await ctx.send(embed=e)

    @_uniform.command(name='gif', description='Return a gif of the selected tag', command_attrs=command_attrs)
    @commands.has_guild_permissions(send_messages=True)
    async def _unifoirm_gif(self, ctx):
        if ctx.author.id == self.client.user.id:
            return
        url = 'https://api.waifu.im/random/?included_tags=uniform' \
            '&gif=true'
        async with self.session.get(url, headers=HEADERS) as resp:
            api = await resp.json()
            if resp.status in {200, 201}:
                url = api['images'][0]['url']
                e = discord.Embed(
                    color=BLUE, description='**Direct Link**: [waifu.im]({})'.format(url))
                e.set_image(url='{}'.format(url))
                await ctx.send(embed=e)
            else:
                error = api['detail']
                e = discord.Embed(color=RED)
                e.set_description('```js\n{}\n```'.format(error))
                await ctx.send(embed=e)

    @_selfies.command(name='gif', description='Return a gif of the selected tag', command_attrs=command_attrs)
    @commands.has_guild_permissions(send_messages=True)
    async def _selfies_gif(self, ctx):
        if ctx.author.id == self.client.user.id:
            return
        url = 'https://api.waifu.im/random/?included_tags=selfies' \
            '&gif=true'
        async with self.session.get(url, headers=HEADERS) as resp:
            api = await resp.json()
            if resp.status in {200, 201}:
                url = api['images'][0]['url']
                e = discord.Embed(
                    color=BLUE, description='**Direct Link**: [waifu.im]({})'.format(url))
                e.set_image(url='{}'.format(url))
                await ctx.send(embed=e)
            else:
                error = api['detail']
                e = discord.Embed(color=RED)
                e.set_description('```js\n{}\n```'.format(error))
                await ctx.send(embed=e)

    @_raiden_shogun.command(name='gif', description='Return a gif of the selected tag', command_attrs=command_attrs)
    @commands.has_guild_permissions(send_messages=True)
    async def _raiden_shogun_gif(self, ctx):
        if ctx.author.id == self.client.user.id:
            return
        url = 'https://api.waifu.im/random/?included_tags=raiden-shogun' \
            '&gif=true'
        async with self.session.get(url, headers=HEADERS) as resp:
            api = await resp.json()
            if resp.status in {200, 201}:
                url = api['images'][0]['url']
                e = discord.Embed(
                    color=BLUE, description='**Direct Link**: [waifu.im]({})'.format(url))
                e.set_image(url='{}'.format(url))
                await ctx.send(embed=e)
            else:
                error = api['detail']
                e = discord.Embed(color=RED)
                e.set_description('```js\n{}\n```'.format(error))
                await ctx.send(embed=e)

    @_mori_calliope.command(name='gif', description='Return a gif of the selected tag', command_attrs=command_attrs)
    @commands.has_guild_permissions(send_messages=True)
    async def _mori_calliope_gif(self, ctx):
        if ctx.author.id == self.client.user.id:
            return
        url = 'https://api.waifu.im/random/?included_tags=mori-calliope' \
            '&gif=true'
        async with self.session.get(url, headers=HEADERS) as resp:
            api = await resp.json()
            if resp.status in {200, 201}:
                url = api['images'][0]['url']
                e = discord.Embed(
                    color=BLUE, description='**Direct Link**: [waifu.im]({})'.format(url))
                e.set_image(url='{}'.format(url))
                await ctx.send(embed=e)
            else:
                error = api['detail']
                e = discord.Embed(color=RED)
                e.set_description('```js\n{}\n```'.format(error))
                await ctx.send(embed=e)

    @_marin_kitagawa.command(name='gif', description='Return a gif of the selected tag', command_attrs=command_attrs)
    @commands.has_guild_permissions(send_messages=True)
    async def _marin_kitagawa_gif(self, ctx):
        if ctx.author.id == self.client.user.id:
            return
        url = 'https://api.waifu.im/random/?included_tags=marin-kitagawa' \
            '&gif=true'
        async with self.session.get(url, headers=HEADERS) as resp:
            api = await resp.json()
            if resp.status in {200, 201}:
                url = api['images'][0]['url']
                e = discord.Embed(
                    color=BLUE, description='**Direct Link**: [waifu.im]({})'.format(url))
                e.set_image(url='{}'.format(url))
                await ctx.send(embed=e)
            else:
                error = api['detail']
                e = discord.Embed(color=RED)
                e.set_description('```js\n{}\n```'.format(error))
                await ctx.send(embed=e)



def setup(client):
    client.add_cog(Images(client))