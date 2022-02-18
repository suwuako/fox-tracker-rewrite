import json

from datetime import datetime


def now_str():
    now = datetime.now()
    now_string = now.strftime("%H:%M:%S %d/%m/%Y")
    return now_string


def read_json():
    secret = open("json/secret.json")
    config = open("json/config.json")

    secret = json.load(secret)
    config = json.load(config)

    return {"secret" : secret, "config" : config}
