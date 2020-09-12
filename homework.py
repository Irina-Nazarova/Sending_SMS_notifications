import time
import os
import requests

from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

vk_access_token = os.getenv("VK_TOKEN")
vk_v = 5.92
tw_account_sid = os.getenv("TWILIO_ACCOUNT_SID")
tw_auth_token = os.getenv("TWILIO_AUTH_TOKEN")
tw_from = os.getenv("NUMBER_FROM")
tw_to = os.getenv("NUMBER_TO")

client = Client(tw_account_sid, tw_auth_token)


def get_status(user_id):
    params = {
        "user_ids": user_id,
        "v": vk_v,
        "access_token": vk_access_token,
        "fields": "online",
    }
    users_list = requests.post(
        "https://api.vk.com/method/users.get", params=params
    )
    try:
        return users_list.json()["response"][0]["online"]
    except Exception as e:
        return e


def sms_sender(sms_text):
    message = client.messages.create(
        body=sms_text,
        from_=tw_from,
        to=tw_to
    )
    return message.sid


if __name__ == "__main__":
    vk_id = input("Введите id ")
    while True:
        if get_status(vk_id) == 1:
            sms_sender(f"{vk_id} сейчас онлайн!")
            break
        time.sleep(5)
