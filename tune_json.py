#! python3
#! -*- coding: utf-8 -*-

import json 
import datetime
import time
import requests

# Создаем глобальные переменные скрипта
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

# Отметка об успешном прохождении авторизации
succesful_id = True



# Создаю переменные даты в разных форматах, т.к. не уверен, который мне будет нужен. 

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

# Login-password input cycle
def logpss_cycle(count=3):
	# print(status_message)
	while count != 0:
		if auth_check(api_keys):
			with open('api.json', 'w') as write_file:
				json.dump(api_keys, write_file, indent=4, ensure_ascii=False,)
			print('\nАвторизация прошла успешно, даные сохранены в api.json в корне приложения.')
			return True	
		count -= 1
		print('Авторизация не удалась, проверьте корректность введенных данных и попробуйте снова.')
		print('Количество оставшихся попыток:', count)

print('Проверка ключей доступа к API smsaero.ru')
if api_keys['login'] == 0 and api_keys['myapi'] == 0:
	print('\nДанные не обнаружены, переходим к процедуре добавления ключей.\n')
	succesful_id = logpss_cycle()	

elif not auth_check(api_keys, eml=api_keys['login'], pswrd=api_keys['myapi']):
	print('\nАвторизация не удалась, проверьте следующие параметры: ',
			'\n - корректность учетных данных', 
			'\n - наличие интернет-соединения', 
			'\n - доступность сервера смс-рассылки.')
	users_will = input('Желаете ли Вы ввести заново учетные данные от своего смс-шлюза? \nОтветьте Да/Нет: ')
	if users_will in ["Да", "Да ", "да", "да ","ДА", "ДА ", "д", "д ", "Д", "Д ","Yes", "Y", "yes", "y"]:
		succesful_id = logpss_cycle()	

else:
	print("Логин", api_keys['login'], "успешно авторизован в системе smsaero.ru")
	users_will = input('Желаете ли Вы изменить логин и парль от своего смс-шлюза? \nОтветьте Да/Нет: ')
	if users_will in ["Да", "Да ", "да", "да ","ДА", "ДА ", "д", "д ", "Д", "Д ","Yes", "Y", "yes", "y"]:
		succesful_id = logpss_cycle()

if succesful_id:
	print("All is working!")

# если будет время - сделать ввод пароля как в терминале.
# если будет время - сделать цикл ввода пароля отдельной функцией
# дальше - следуй намеченному плану разработки
