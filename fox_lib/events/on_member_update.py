import discord
import pprint
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
        self.stat_channel = await self.bot.fetch_channel(self.json_values["secret"]["stat_channel"])

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

        mid = await self.stat_channel.send("Init concluded")
        self.current_activities["hook"] = mid

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        cid = after.guild.id
        mgid = self.json_values["secret"]["main_guild"]

        # check if info is being taken from main_guild
        if str(cid) == mgid:
            return

        if self.ignore_bots and after.bot:
            return

        if after.id not in self.json_values["ignore"]:
            return

        if before.activities != after.activities:
            before_act = before.activities
            after_act = after.activities

            missing = fox_library.fetch_misisng_act(before_act, after_act)
            session_time = fox_library.time_spent(self.current_activities, after.id, missing)

            await fox_library.log_update(missing, session_time, after, self.current_activities, self.bot, self.stat_channel)







def setup(bot):
    bot.add_cog(MemberUpdate(bot))
