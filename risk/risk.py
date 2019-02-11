import discord
from redbot.core import commands, Config
from redbot.core.data_manager import bundled_data_path
from redbot.core.data_manager import cog_data_path
from random import randint
import asyncio

class Card():
    def __init__(self, typec, country):
        self.typec = typec
        self.country = country

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
        players = [ctx.message.author.id]
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
                r = await self.bot.wait_for('message', timeout=60, check=lambda m: m.author.id not in [m.id for m in players] and m.author.bot == False and m.channel == channel and m.content.lower() == 'i')
            except asyncio.TimeoutError:
                self.runningin.remove(ctx.channel.id)
                return await ctx.send('You took too long to respond.')
            players.append(r.author)
        # Image set up here
        # Begin play
        cards = {}
        for player in players:
            cards[player.id] = []
        while True:
            for player in players:
                # Print board
                inTurn = True
                while inTurn:
                    await ctx.send(f"{player.mention} it is your now your turn.  Type a to attack, t to trade in cards or d to say you are done.")
                    def check2(m):
                        return (m.author.id == player.id) and (m.channel.id == ctx.channel.id) and (m.content in ['a', 't', 'd'])
                    try:
                        message = await self.bot.wait_for('message', check=check2, timeout=600.0)
                    except asyncio.TimeoutError:
                        # Probably save game here
                        return
                    if message.content == "d":
                        inTurn = False
                        continue
                    elif message.content == "t":
                        pcards = cards[message.author.id]
                        if len(pcards) != 3:
                            await ctx.send("You don't have enough cards!")
                            continue
                        else:
                            scards = []
                            ccards = []
                            hcards = []
                            for card in pcards:
                                if card.typec == "horse":
                                    hcards.append(card)
                                elif card.typec == "cannon":
                                    ccards.append(card)
                                else:
                                    scards.append(card)
                            if (len(scards) >= 3) or (len(ccards) >= 3) or (len(hcards) >= 3):
                                # Ask for which category to trade in, and what cards
                                pass
                            elif (len(scards) >= 1) and (len(ccards) >= 1) and (len(hcards) >= 1):
                                # Trade in three cards, one of each type, ask which cards
                                pass
                            else:
                                await ctx.send("Sorry, it doesn't look like you have the appropriate cards to trade in.")
                                continue
                            continue
                    elif message.content == 'a':
                        # Handle attacking here

                        # Which country are you attacking from
                        # Which country are you attacking?
                        # {Evaluate amount of armies in country}
                        # {Evaluate amount of armies in other country}
                        # Ask how many die
                        # Roll
                        # Cleanup
                        pass