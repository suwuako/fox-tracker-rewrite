import discord
import fox_lib.libraries.functions as fox_library

from discord.ext import commands
from datetime import datetime


class MemberUpdate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.json_values = fox_library.read_json()
        self.sort_activity = fox_library.sort_activity
        self.find_diff = fox_library.find_diff
        self.now_str = fox_library.now_str
        self.missing = fox_library.missing

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

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        cid = after.guild.id
        mgid = self.json_values["secret"]["main_guild"]

        # check if info is being taken from main_guild
        if str(cid) == mgid:
            return

        if self.ignore_bots and after.bot:
            return

        if before.activities != after.activities:
            before_act = before.activities
            after_act = after.activities

            sort = await self.sort_activity(before_act, after_act)
            missing = await self.find_diff(sort["before"], sort["after"])
            sorted = await self.missing(missing, sort)



def setup(bot):
    bot.add_cog(MemberUpdate(bot))