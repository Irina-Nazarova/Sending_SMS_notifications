import time

import requests
from twilio.rest import Client


def get_status(user_id):
    params = {
        "user_ids": user_id,
        "v": 5.92,
        "access_token": 'VK_TOKEN',
        "fields": "online"
    }
    users_list = requests.post("https://api.vk.com/method/users.get", params=params)
    return users_list.json()["response"][0]["online"]


def sms_sender(sms_text):
    account_sid = 'TWILIO_ACCOUNT_SID'
    auth_token = 'TWILIO_AUTH_TOKEN'
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                        body="sms_text",
                        from_='NUMBER_FROM',
                        to='NUMBER_TO'
    )
    return message.sid


if __name__ == "__main__":
    vk_id = input("Введите id ")
    while True:
        if get_status(vk_id) == 1:
            sms_sender(f'{vk_id} сейчас онлайн!')
            break
        time.sleep(5)
