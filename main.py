#! python3
# -*- coding: utf-8 -*-

'''
        Ура, программа работает!
            - В базовом режиме, конечно, не прикручен еще механизм автоматизации - нужно запускать скрипт в ручную,
            - Но при ручном запуске прога без ошибок отрабатывает логику программы:
                - Проверяет день на соответствие
                - Определяет тип события, изменяет текст в соотсветствии с событием
                - Находит в базе номера проповедников и производит на них рассылку.
                - Логгирует успешные отправки сообщений (хоть и очень кратко)
        Дальнейшее развитие:
            - Настроить нормальное логгирование отправки сообщений, собирать информацию о доставке сообщений.
            - Посылать отчеты администратору и пастору о проповедниках на воскресенье и прочие дни.
            - Обрабатывать типичные ошибки отправки и сообщать о них администратору.
            - Интерфейс редактирования базы данных приложения.
            - Информирование проповедника за месяц до конца сезона о необходимости внесения корректировок
            - Доложить пастору о срыве в подготовке списка если тот не готов за две недели до следующего сезона.
'''

from __future__ import print_function
from kalendar import events_2018_summer as events_list
from sender import *
import datetime
import time
import json

with open("preachers_base.json", "r") as read_file:
    preachers_list = json.load(read_file)

with open("events_base.json", "r") as read_file:
    events_base = json.load(read_file)

def phones(day, preachers, events):
    miniters = events[day]['ministers']
    numbers = []
    for minister in miniters:
        phone = preachers[minister]
        for foo in phone:
            numbers.append(foo)
    return numbers

def check_kalendar(events_list):
    # Проверяем ключи словаря events_list и высчитываем разницу между ними.

    for church_event in events_list:

        now = datetime.datetime.now()
        year, month, day = (foo for foo in church_event) # этот костыль здесь потому, что ключом в
                                                         # словаре является кортеж с целыми числами.
                                                         # другой формат хранения данных может мне помочь от него
                                                         # избавиться.
        then = datetime.datetime(year, month, day)

        delta = then - now

        if delta.days == 6 or delta.days == 2:
            this_day = ','.join([str(foo) for foo in church_event])  # Представление даты в формате словаря events_base
            if events_base[this_day]['type'] == 'Preaching':
                print("Someones must prepare for preaching in", this_day)
                text = "Напоминаю, что " + this_day + " Вы читаете проповедь в церкви 'Слово Жизни'"
                send_sms(phones(this_day, preachers_list, events_base), text)

            if events_base[this_day]['type'] == 'Bible Teaching':
                print("Someones must prepare for Bible Teaching in", this_day)
                text = "Напоминаю, что " + this_day + " Вы ведете разбор Библии в церкви 'Слово Жизни'"
                send_sms(phones(this_day, preachers_list, events_base), text)
        # else:
        #     print('No events today')

        # time.sleep(86400) # Эта задержка в сутки.

check_kalendar(events_list)