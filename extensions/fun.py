import discord
from random import randint

from discord.ext import commands


class Fun(commands.Cog, name='Fun'):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(aliases=['keks'], hidden=True)
    async def cookie(self, ctx, member: discord.Member):
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send('{0.mention} hier ist ein Keks für dich 🍪'.format(member))
        else:
            await ctx.send('Ach {0.mention}, der {1.name} bekam zuletzt einen Keks. Du darfst ihm nicht noch einen geben.'.format(ctx.author, member))
        self._last_member = member

    @commands.command(hidden=True)
    async def ping(self, ctx):
        await ctx.send('{0.mention} pong!'.format(ctx.author))

    @commands.command(hidden=True)
    async def pong(self, ctx):
        await ctx.send('{0.mention} ping'.format(ctx.author))

    @commands.command(aliases=['kuchen'], hidden=True)
    async def cake(self, ctx):
        await ctx.send('{0.mention} The Cake Is A Lie'.format(ctx.author))

    @commands.command(hidden=True)
    async def alive(self, ctx):
        await ctx.send('{0.mention} https://www.youtube.com/watch?v=Y6ljFaKRTrI'.format(ctx.author))

    @commands.command(aliases=['münzwurf', 'münze', 'kopf', 'zahl', 'coin'], hidden=True)
    async def coinflip(self, ctx):
        coin = randint(0, 1)
        if coin == 0:
            await ctx.send('{0.mention} Kopf'.format(ctx.author))
        else:
            await ctx.send('{0.mention} Zahl'.format(ctx.author))

    @commands.command(aliases=['tableflip'], hidden=True)
    async def flip(self, ctx):
        await ctx.send('{0.mention} (╯°□°）╯︵ ┻━┻'.format(ctx.author))

    @commands.command(aliases=['mayo'], hidden=True)
    async def mayonaise(self, ctx):
        await ctx.send('{0.mention} https://www.youtube.com/watch?v=hVtSkF-hBXE'.format(ctx.author))

    @commands.command(aliases=['carlo'], hidden=True)
    async def caro(self, ctx):
        await ctx.send('{0.mention} https://youtu.be/NFAjjdM0HaU?t=27'.format(ctx.author))


def setup(bot):
    bot.add_cog(Fun(bot))