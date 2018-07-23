import json
import time
import requests


def send_sms(numbers, text):
    # Проходим авторизацию
    with open("api.json", "r") as read_file:
        data = json.load(read_file)
    auth = "https://" + data['login'] + ":" + data['myapi'] + "@gate.smsaero.ru/v2"
    response = requests.get(auth + '/auth')
    todos = response.json()
    if todos['success']:
        print(todos['message'])

    for number in numbers:

        # Собираем переменную с параметрами
        params = {
        'number': number,
        'sign': ['SLOVO'],
        'text': text,
        'channel': 'INFO'
    }
        # Отправляем сообщения
        send = requests.get(auth + '/sms/send', params=params)
        track = send.json()
        di = track['data']['id']
        message = track['data']['text']
        phone = track['data']['number']
        cost = track['data']['cost']
        log_string = '  id: ' + str(di) + ', text: "' + message + '", number: ' + phone + '", cost: ' + str(cost) + '\n'
        if track['success']:
            with open("success_log.txt", "a") as log:
                log.write(time.ctime(time.time()))
                log.write(log_string)
        else:
            with open("success_log.txt", "a") as log:
                log.write(time.ctime(time.time()))
                log.write(' Sending failed\n')