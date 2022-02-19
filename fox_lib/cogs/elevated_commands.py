import fox_lib.libraries.functions as fox_library
import discord

from discord.ext import commands


class DiscordElevatedCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.json_values = fox_library.read_json()

        self.ignore_bots = self.json_values["config"]["ignore_bots"]
        self.elevated_users = self.json_values["secret"]["perms"]

        print("elevated_commands loaded")

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

        for guild in self.bot.guilds:
            embed = discord.Embed(title=f" {guild}",
                                  url="https://github.com/suwuako/fox-tracker",
                                  color=0x87cefa)
            embed.set_author(name=guild,
                             icon_url=guild.icon_url)
            embed.set_footer()

            async for member in guild.fetch_members(limit=None):
                activities = guild.get_member(member.id).activities

                if not (self.ignore_bots and member.bot != True) and activities != ():
                    continue
                for i in activities:
                    embed.add_field(name=f"{member.name}#{member.discriminator}",
                                    value=f"`[{i.type.name}]`\n"
                                          f"{i.name}\n",
                                    inline=True)

            await message.send(embed=embed)


def setup(bot):
    bot.add_cog(DiscordElevatedCommands(bot))
