import json
import discord

from datetime import datetime


def now_str():
    now = datetime.now()
    now_string = now.strftime("%H:%M:%S %d/%m/%Y")
    return now_string


def read_json():
    secret = open(r"json/secret.json")
    config = open(r"json/config.json")
    ignore = open(r"json/ignore.json")

    secret = json.load(secret)
    config = json.load(config)
    ignore = json.load(ignore)

    return {"secret": secret, "config": config, "ignore": ignore}

def fetch_misisng_act(before, after):
    """find missing values"""
    b_len = len(before)
    a_len = len(after)

    b_list = list()
    a_list = list()

    for b in before:
        b_list.append(b.type.name)
    for a in after:
        a_list.append(a.type.name)

    if b_len > a_len:
        for b in before:
            if b.type.name not in a_list:
                return {"ab" : "after", "value" : b.type.name, "item" : b}

    elif b_len < a_len:
        for a in after:
            if a.type.name not in b_list:
                return {"ab" : "before", "value" : a.type.name, "item" : a}

    elif b_len == a_len:
        for i in range(b_len):
            if before[i] != after[i]:
                return {"ab" : None, "value" : before[i].type.name, "item" : before[i]}

def time_spent(current, uid, missing):
    try:
        time_then = current[uid][missing["value"]]["time"]
    except KeyError:
        time_then = datetime.now()

    now = datetime.now()
    time_elapsed = now - time_then
    return time_elapsed.total_seconds()

async def log_update(missing, session_time, user, mid, bot, channel):
    missing_value = missing["ab"]
    embed = discord.Embed(url="https://github.com/suwuako/fox-tracker")
    embed.set_author(name=f"{user.name}#{user.discriminator}",
                     icon_url=user.avatar_url)

    try:
        mid = mid[user.id]["mid"]
    except KeyError:
        mid = mid["hook"]

    if missing_value == "after":
        embed.color=0xFF9F7F
        embed.title=("`[end]`")
        if missing["value"] == "listening":
            embed.add_field(name=f"{missing['value']}, {session_time/60}m",value="something spotify")
        else:
            embed.add_field(name=f"{missing['value']}, session: {session_time*60}m", value=missing["item"].name)

    elif missing_value == "before":
        embed.color=0x7FFF7F

    elif missing_value == None:
        embed.color=0x7FFFB2


    a = await channel.fetch_message(mid)
    await a.reply(embed=embed)