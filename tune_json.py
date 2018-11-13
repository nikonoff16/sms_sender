#! python3
#! -*- coding: utf-8 -*-

'''
Module manifest
The module should interact with *.json files in the program and provide for that human-frendly 
interface. 
The core functionality: change or create events_base and preachers_base files through one console window. 

Bussiness logic:
- Show current state of events_base and preachers_base
- Ask is it right that user wants to setup the program
- If user acsepts the request, ask him what time period he is going to setup (by default it shall be 92 days 
  and starts from last date in event_base)
- The scrit starts for cycle and parses every date in that period. 
- The processors - the big il-elif-else construction - shall manage different event rules.
- The rules may relate to the weekday, day of the month (25.12, 07.01) or any other calculated church event, like Pascha.
	- Every rule shall have its own theme marker.
- Every rule shall use create_event() function. 
- Every event shall have following points:
	- Preachers
	- Leaders
	- Proposal text
- When an iteration ends, script shall update json-file with new data.
- When the cycle ends, script shall
	- create a copy of json-file and place it in designated directory
	- delete all the events, that is older then current date
'''
import json 
import datetime
import time
import requests

# Creating global variables
try:
	with open("preachers_base.json", "r") as read_file:
		preachers_list = json.load(read_file)
except FileNotFoundError:
	preachers_list = {}

try:
	with open("events_base.json", "r") as read_file:
		events_base = json.load(read_file)
except FileNotFoundError:
	events_base = {}
api_keys = {}
try:
	with open("api.json", "r") as api_file:
		api_keys = json.load(api_file)
except FileNotFoundError:
	api_keys = {"login": 0, "myapi": 0}



# Creating date-variables 
# I don't know for sure what date standard I would use in the main cycle, so let it be both there.s	

date_cur_date = datetime.datetime.now()
str_cur_date = str(date_cur_date)[:10]  # I need only YYYY-MM-DD date format, so by slicing to 10 I make it

###########################################################################################################
################################## STATE SCRIPT CONSOLE PRESENTATION ###################################### 
###########################################################################################################

#  API-status
def auth_check(api: dict, eml=0, pswrd=0) -> 'bool':
	if eml == 0 and pswrd == 0:
		api['login'] = input('Введите корректный логин от ресурса smsaero.ru (как правило это email-адрес): ')
		api['myapi'] = input('Введите корректный ключ доступа к API: ')
		auth = "https://" + api_keys['login'] + ":" + api_keys['myapi'] + "@gate.smsaero.ru/v2"
	else:
		auth = "https://" + eml + ":" + pswrd + "@gate.smsaero.ru/v2"
	response = requests.get(auth + '/auth')
	todos = response.json()
	return todos['success']  # Here we receive a boolean, response from sms-server.

print('Проверка ключей доступа к API smsaero.ru')
if api_keys['login'] == 0 and api_keys['myapi'] == 0:
	print('\nДанные не обнаружены, переходим к процедуре добавления ключей.\n')
	count = 3
	while count != 0:
		if auth_check(api_keys):
			with open('api.json', 'w') as write_file:
				json.dump(api_keys, write_file, indent=4, ensure_ascii=False,)
			print('\nАвторизация прошла успешно, даные сохранены в api.json в корне приложения.')
			break
		count -= 1
		print('Авторизация не удалась, проверьте корректность введенных данных и попробуйте снова.')
		print('Количество оставшихся попыток:', count)

elif not auth_check(api_keys, eml=api_keys['login'], pswrd=api_keys['myapi']):
	print('\nАвторизация не удалась, проверьте корректность учетных данных, наличие интернет-соединения, доступность сервера смс-рассылки.')
	users_will = input('Желаете ли Вы ввести заново учетные данные от своего смс-шлюза? \nОтветьте Да/Нет: ')
	if users_will in ["Да", "Да ", "да", "да ","ДА", "ДА ", "д", "д ", "Д", "Д ","Yes", "Y", "yes", "y"]:
		count = 3
		while count != 0:
			if auth_check(api_keys):
				with open('api.json', 'w') as write_file:
					json.dump(api_keys, write_file, indent=4, ensure_ascii=False,)
				print('\nАвторизация прошла успешно, даные сохранены в api.json в корне приложения.')
				break
			count -= 1
			print('Авторизация не удалась, проверьте корректность введенных данных и попробуйте снова.')
			print('Количество оставшихся попыток:', count)

# Дописать ситуации, когда:
# 	- файл есть, его нужно скорректировать (пусть он и рабочий)
