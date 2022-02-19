from discord.ext import commands

class member_update(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(member_update(bot))