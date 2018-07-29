# from main import tech_counters
import json
import time
import requests


def send_sms(numbers, text):
    # # Создаем словарь для сбора статистической информации
    # with open("tech_counters.json", "r") as read_file:
    #     tech_counters = json.load(read_file)

    # Проходим авторизацию
    with open("api.json", "r") as read_file:
        data = json.load(read_file)
    auth = "https://" + data['login'] + ":" + data['myapi'] + "@gate.smsaero.ru/v2"
    response = requests.get(auth + '/auth')
    todos = response.json()
    if todos['success']:
        print(todos['message'])

    sms_count = 0
    total_cost = 0

    for number in numbers:

        # Собираем переменную с параметрами
        params = {
        'number': number,
        'sign': ['SLOVO'],
        'text': text,
        'channel': 'DIRECT'
    }
        # Отправляем сообщения
        send = requests.get(auth + '/sms/send', params=params)
        track = send.json()

        # Обрабатываем ответ для сбора статистической информации
        di = track['data']['id']
        message = track['data']['text']
        phone = track['data']['number']
        cost = track['data']['cost']
        # Создаем строку для удобной записи в лог
        log_string = '  id: ' + str(di) + ', text: "' + message + '", number: ' + phone + '", cost: ' + str(cost) + '\n'

        if track['success']:
            sms_count += 1
            total_cost +=  cost
            with open("success_log.txt", "a") as log:
                log.write(time.ctime(time.time()))
                log.write(log_string)
        else:
            with open("success_log.txt", "a") as log:
                log.write(time.ctime(time.time()))
                log.write(' Sending failed\n')
    return sms_count, total_cost