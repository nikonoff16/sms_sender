import json
import requests

with open("api.json", "r") as read_file:
    data = json.load(read_file)
auth = "https://"+ data['login'] + ":" + data['myapi'] + "@gate.smsaero.ru/v2"

response = requests.get(auth + '/auth')
todos = response.json()

params = {
    'number': '',
    'sign': ['SMS aero'],
    'text': 'Это Осипов))',
    'channel': 'INFO'
}

send = requests.get(auth + '/sms/send', params=params)
print(send)
track = send.json()
print(track)