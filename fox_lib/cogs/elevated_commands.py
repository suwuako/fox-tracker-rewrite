import fox_lib.libraries.functions as fox_library

from datetime import datetime
from discord.ext import commands


class DiscordElevatedCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.json_values = fox_library.read_json()

        self.elevated_users = self.json_values["secret"]["perms"]

    @commands.command(aliases=["poweroff", "shutdown"])
    async def quit(self, message):
        if message.author.id not in self.elevated_users:
            return

        log_channel = await self.bot.fetch_channel(self.json_values["secret"]["log_channel"])

        await message.send("shutting down...")
        await log_channel.send(f"<@{message.author.id}> used !quit. Shutting down...")
        quit()

    @commands.command(aliases=["status"])
    async def stat(self, message):
        if message.author.id not in self.elevated_users:
            return





def setup(bot):
    bot.add_cog(DiscordElevatedCommands(bot))
