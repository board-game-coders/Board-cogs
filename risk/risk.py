import discord
from redbot.core import commands, Config
from redbot.core.data_manager import bundled_data_path
from redbot.core.data_manager import cog_data_path
from random import randint

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
