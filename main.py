import random

import requests
import json
import time
from datetime import datetime

keys_api = [["YjRlYzYzOTAtNTg1OC00Yzg5LTlhYzktMTRlYjdkYzE1MDcz", "ef936a33-36ad-4068-929b-96425a4b33f1"],
            ["MjQ0NDZhMTgtYWEwMC00NmFkLWI1M2YtNmZhZjg3MzhlYTc2", "dbfe723c-eb57-4d87-aa03-d7482565a141"],
            ["NDllZWRiNGItNzJmMy00M2QwLThiZTMtMWM3NWY1YzNmNWMy", "ee772290-d0fd-4580-a13f-6686eaf1fe07"],
            ["M2I1MjYwNmItMzMyYi00OWE5LWJkOWQtNGE3NTljN2JiMzVj", "03eefc42-1f1b-4e12-a828-646967832b8a"]]

titles = ["ДЕНЬГИ ЖДУТ !!!", "Денег на всех не хватит.", "Специальное предложение", "Только для Вас",
          "Займы без процентов", "Денег нет? Мы поможем", "Под 0%", "Ваш займ одобрен", "Деньги под 0%",
          "Здравствйуте, деньги почти у вас✅"]
messages = ["Вам одобрен БЕЗПРОЦЕНТНЫЙ заем до 50 000р.😱", "Успей получить заем до 50 000р. под 0%😱",
            "Одобрен займ до 50 000", "Дадим в долг под 0%", "Один клик и деньги у вас", "Даем в долг без процентов",
            "Подтвердите отправку денег"]


def sendPush(rest_api_key, app_id, title, text):
    header = {"Content-Type": "application/json; charset=utf-8",
              "Authorization": f"Basic {rest_api_key}"}

    payload = {"app_id": f"{app_id}",
               "included_segments": ["Subscribed Users"],
               "headings": {"en": f"{title}"},
               "contents": {
                   "en": f"{text}"
               }}

    req = requests.post("https://onesignal.com/api/v1/notifications", headers=header, data=json.dumps(payload))

    print(req.status_code, req.reason)


def sendMessagesToAll(title, message):
    for i in range(len(keys_api)):
        api_key = keys_api[i][0]
        app_id = keys_api[i][1]
        print(api_key, app_id)
        sendPush(api_key, app_id, title, message)


# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    while (True):
        time.sleep(60)
        date_now = datetime.now()
        hour = date_now.hour
        minute = date_now.minute
        print(hour,minute)
        if ((hour == 9 or hour == 12) and minute == 00):
            title_random = random.randint(0, len(titles) - 1)
            message_random = random.randint(0, len(messages) - 1)
            sendMessagesToAll(title=titles[title_random], message=messages[message_random])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
