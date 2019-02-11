import discord
from redbot.core import commands
from random import randint

class Risk(commands.Cog):
    def __init__(self, bot):
        self.bot = bot