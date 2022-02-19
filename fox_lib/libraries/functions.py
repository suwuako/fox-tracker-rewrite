import json

from datetime import datetime


def now_str():
    now = datetime.now()
    now_string = now.strftime("%H:%M:%S %d/%m/%Y")
    return now_string


def read_json():
    secret = open(r"json/secret.json")
    config = open(r"json/config.json")

    secret = json.load(secret)
    config = json.load(config)

    return {"secret" : secret, "config" : config}

async def sort_activity(before, after):
    activity_dict = {}
    activity_dict["before"] = {}
    activity_dict["after"] = {}

    for i in before:
        activity_dict["before"][i.type.name] = i

    for i in after:
        activity_dict["after"][i.type.name] = i

    return activity_dict

#purpose is to find before and after if they have differences and returns before and after values with Nonetype if not assigned
async def find_diff(before, after):
    a_keys = []
    b_keys = []

    a_keys_missing = []
    b_keys_missing = []

    for a in after:
        a_keys.append(a)

    for b in before:
        b_keys.append(b)

    for a in a_keys:
        if a not in b_keys:
            a_keys_missing.append(a)

    for b in b_keys:
        if b not in a_keys:
            b_keys_missing.append(b)

    return({"after" : a_keys_missing, "before": b_keys_missing})

async def missing(missing, sort):
    print(missing)
    if len(missing["after"]) == len(missing["before"]):
        sort["status"] = 0
        return sort

    elif len(missing["after"]) >= len(missing["before"]):
        sort["before"][missing["after"][0]] = None
        sort["status"] = 1
        return sort

    elif len(missing["after"]) <= len(missing["before"]):
        sort["after"][missing["before"][0]] = None
        sort["status"] = 2
        return sort

