import fox_lib.libraries.functions as fox_library

from datetime import datetime
from discord.ext import commands

class DiscordBasicCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = datetime.now()
        self.start_time_str = fox_library.now_str()

        json_values = fox_library.read_json()

    async def latency(self, message, before, after):
        then = datetime.now()
        item = await message.send(before)

        latency = f"[latency: {str(datetime.now() - then)} (ms)]"
        await item.edit(content=f"{after}\n"
                                f"{latency}")


    @commands.command()
    async def ping(self, message):
        then = datetime.now()

        message = await message.send("<a:fox_ears:944222338243780640> Pong!")
        latency = datetime.now() - then
        await message.edit(content=f"<a:fox_ears:944222338243780640> Pong!\n"
                                   f"[latency: {latency}] ")

        edit_latency = datetime.now() - then
        await message.edit(content=f"<a:fox_ears:944222338243780640> Pong!\n"
                                   f"[latency: {latency} (ms)] \n"
                                   f"[edit latency: {edit_latency}] (ms)")

    @commands.command(aliases=["active", "online", "time"])
    async def uptime(self, message):
        uptime = (datetime.now() - self.start_time)

        output = f"[{fox_library.now_str()}]: Kemo has been online for {uptime}, since {self.start_time_str}"
        await self.latency(message, output, output)



def setup(bot):
    bot.add_cog(DiscordBasicCommands(bot))