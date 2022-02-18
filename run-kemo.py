import asyncio
import discord
import fox_lib.libraries.functions as fox_library

from discord.ext import tasks, commands

class kemo():
    def __init__(self):
        self.now_str = fox_library.now_str

        json_values = fox_library.read_json()


        self.token = json_values["secret"]["token"]


        @bot.event
        async def on_ready():
            self.log_channel = await bot.fetch_channel(json_values["secret"]["log_channel"])
            self.stat_channel = await bot.fetch_channel(json_values["secret"]["stat_channel"])

            await bot.change_presence(activity=discord.Streaming(name='with Foxes 🦊', url='https://www.youtube.com/watch?v=c6VhcpwFZJM'))
            await self.log_channel.send("=== Start Log ===")
            await self.log_channel.send(f"`[{self.now_str()}]` Bot logged in as {bot.user}")

    def load_cogs(self):
        pass

    def run(self):
        self.load_cogs()
        bot.run(self.token)

if __name__ == "__main__":
    intents = discord.Intents.all()

    bot = commands.Bot(command_prefix='!', intents=intents)
    bot.remove_command('help')

    discord_bot = kemo()
    discord_bot.run()