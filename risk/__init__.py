from .risk import Risk

def setup(bot):
    bot.add_cog(Risk(bot))