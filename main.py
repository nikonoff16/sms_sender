#! python3
# -*- coding: utf-8 -*-

'''
        Программа еще даже не работает.
        Главная проблема - восстановление работоспособности (она уже работала,
        нужно понять причину потери работоспособности и устранить ее).
        План необходимых работ:
            - установить Ubuntu 18.04, накатить все обновления
            - установить gammu
                - настроить модем
                - дать ему нужные разрешения (sudo chmod 777 /dev/TtyXXX)
                - правильно настроить конфигурацию gammu
                - добавить kalendar.py в гитигнор капитально.
            - проверить работоспособность через командную строку
            - допилить отправку сообщений, провести тесты на дурака
            - настроить программу на сервере (пока без собственной настройки сервера для удаленного использования)
        Дальнейшее развитие:
            - Настроить логгирование отправки сообщений, собирать информацию о доставке сообщений.
            - Посылать отчеты администратору и пастору о проповедниках на воскресенье и прочие дни.
            - Обрабатывать типичные ошибки отправки и сообщать о них администратору.
            - Перевести хранение данных программы в JSON. (Использовать и модифицировать C8 приветствуется).
            - Интерфейс редактирования базы данных приложения.
            - Информирование проповедника за месяц до конца сезона о необходимости внесения корректировок
            - Доложить пастору о срыве в подготовке списка если тот не готов за две недели до следующего сезона.
'''

from __future__ import print_function
from  kalendar import *
import gammu
import datetime
import time

import sys
''' Эта функция должна отправлять большие смс, по идее. На самом же деле она спотыкается о 
    utf кодированное сообщение text и выдает ошибку. Попробую переустановить Ubuntu, может 
    зарабоает'''
# def send_sms(phone_number, text):
#     sm = gammu.StateMachine()
#     sm.ReadConfig()
#     sm.Init()
#
#     smsinfo = {
#         'Class': -1,
#         'Unicode': True,
#         'Entries': [
#             {
#                 'ID': 'ConcatenatedTextLong',
#                 'Buffer': text
#             }
#         ]}
#     encoded = gammu.EncodeSMS(smsinfo)
#
#     for message in encoded:
#         message['SMSC'] = {'Location': 1}
#         message['Number'] = phone_number
#         message['Coding'] = 'Unicode_No_Compression'
#         sm.SendSMS(message)
#     # message = {'Text': text,
#     #            'SMSC':{'Location': 1},
#     #            'Coding': 'Unicode_No_Compression',
#     #            'Unicode': True,
#     #            'Number': phone_number}
#     # sm.SendSMS(message)

'''Эта функция собственно и выполняет работу по проверке данных. Из особенностей - 
    выполнение - вечный цикл. При совпадении условий вызывает функцию send_sms. '''
def check_kalendar(events_list, preachers_list, text):
    # Проверяем ключи словаря events_list и высчитываем разницу между ними.
    while True:
        for church_event in events_list:

            now = datetime.datetime.now()
            year, month, day = (foo for foo in church_event) # этот костыль здесь потому, что ключом в
                                                             # словаре является кортеж с целыми числами.
                                                             # другой формат хранения данных может мне помочь от него
                                                             # избавиться.
            then = datetime.datetime(year, month, day)

            delta = then - now

            if delta.days == 6 or delta.days == 2:

                for preacher in events_list[church_event]:

                    for number in preachers_list[preacher]:
                        send_sms(number, text)
            else:
                print('No events today')

            time.sleep(86400) # Эта задержка в сутки.

check_kalendar(events_list, preachers_list, text)