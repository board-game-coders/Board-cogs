import discord
from redbot.core import commands, Config
from redbot.core.data_manager import bundled_data_path
from redbot.core.data_manager import cog_data_path
from random import randint
import asyncio

class Risk(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.runningin = []
        self.config = Config.get_conf(self, identifier=5849752632)
        self.config.register_guild(

        )

    @commands.guild_only()
    @commands.command()
    async def risk(self, ctx):
        """Plays a game of Risk.  In heavy development, discouraged from use"""
        if ctx.channel.id in self.runningin:
            return await ctx.send('There is already a game running in this channel.')
        self.runningin.append(ctx.channel.id)
        id = [None, ctx.message.author.id]
        name = [None, str(ctx.message.author)[:-5]]
        channel = ctx.channel
        await ctx.send("Welcome!  How many players? (must be between 2 and 5)")
        i = 0
        def check(m):
            canInt = False
            try:
                int(m.content)
                canInt = True
            except:
                pass
            return (m.author.id == ctx.author.id) and (m.channel.id == ctx.channel.id) and (canInt)
        while i == 0:
            try:
                message = await self.bot.wait_for('message', check=check, timeout=60.0)
            except asyncio.TimeoutError:
                await ctx.send("Canceling due to no reply")
                self.runningin.remove(ctx.channel.id)
                return
            num = int(message.content)
            if num < 2 or num > 5:
                await ctx.send("Please select a number between 2 and 5.")
            else:
                numalive = num
                i = 1
        for pnum in range(2, numalive+1):
            await ctx.send('Player '+str(pnum)+', say I')
            try:
                r = await self.bot.wait_for('message', timeout=60, check=lambda m: m.author.id not in id and m.author.bot == False and m.channel == channel and m.content.lower() == 'i')
            except asyncio.TimeoutError:
                self.runningin.remove(ctx.channel.id)
                return await ctx.send('You took too long to respond.')
            name.append(str(r.author)[:-5])
            id.append(r.author.id)
        await ctx.send("There are " + str(len(id)) + " people playing: " + " ".join(name))