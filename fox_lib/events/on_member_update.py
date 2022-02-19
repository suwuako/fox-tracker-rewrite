import discord
import fox_lib.libraries.functions as fox_library

from discord.ext import commands
from datetime import datetime


class MemberUpdate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.json_values = fox_library.read_json()
        self.now_str = fox_library.now_str

        self.ignore_bots = self.json_values["config"]["ignore_bots"]

        self.current_activities = {}

        print("on_member_update loaded")

    @commands.Cog.listener()
    async def on_ready(self):
        self.stat_channel = self.json_values["secret"]["stat_channel"]
        self.stat_channel = await self.bot.fetch_channel(self.stat_channel)

        for guild in self.bot.guilds:
            async for member in guild.fetch_members(limit=None):
                activities = guild.get_member(member.id).activities

                if self.ignore_bots and member.bot:
                    continue

                if activities == ():
                    continue

                self.current_activities[member.id] = dict()
                for i in activities:
                    self.current_activities[member.id][i.type.name] = {"item": i,
                                                                       "time": datetime.now()}

        for uid in self.current_activities:
            member = await self.bot.fetch_user(uid)

            embed = discord.Embed(title=f"`[Event-Init]`",
                                  url="https://github.com/suwuako/fox-tracker",
                                  color=0x87cefa)

            embed.set_author(name=f"{member.name}#{member.discriminator}",
                             icon_url=member.avatar_url)

            for activity in self.current_activities[uid]:
                embed.add_field(name=activity, value=self.current_activities[uid][activity]["item"].name)

            message_info = await self.stat_channel.send(embed=embed)
            self.current_activities[uid]["mid"] = message_info.id

        await self.stat_channel.send("Init concluded")
        print(self.current_activities)


def setup(bot):
    bot.add_cog(MemberUpdate(bot))