#! python3
# -*- coding: utf-8 -*-

'''
        Реализованные возможности:
            - Все созданные функции при их вызове корректно работают.
            - Краткое перечисление совершаемой работы:
                - Проверяет день на соответствие
                - Определяет тип события, изменяет текст в соотсветствии с событием
                - Находит в базе номера проповедников и производит на них рассылку.
                - Логгирует успешные отправки сообщений
        Дальнейшее развитие:
            - Создание цикла жизни приложения
            - Создание проверок, не допускающих избыточную отправку сообщений.
            - Cобирать информацию о доставке сообщений.
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

with open("test_base.json", "r") as read_file: # ВНИМАНИЕ! ОТКЛЮЧИ ТЕСТОВЫЙ РЕЖИМ ПЕРЕД СТАРТОМ ПРИЛОЖЕНИЯ!
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

        if delta.days == 4 or delta.days == 2:
            row_day = [str(foo) for foo in church_event]
            this_day = ','.join(row_day)  # Представление даты в формате словаря events_base
            row_day.reverse()
            correct_day = '.'.join(row_day)  # Представление даты для текста сообщения и поиска в сообщениях по логам.

            if events_base[this_day]['type'] == 'Preaching':
                print("Someones must prepare for preaching in", correct_day)
                text = correct_day + " Вы читаете проповедь"
                send_sms(phones(this_day, preachers_list, events_base), text)

            if events_base[this_day]['type'] == 'Bible Teaching':
                print("Someones must prepare for Bible Teaching in", correct_day)
                text = correct_day + " Вы ведете разбор Библии"
                send_sms(phones(this_day, preachers_list, events_base), text)
        # else:
        #     print('No events today')

        # time.sleep(86400) # Эта задержка в сутки.

check_kalendar(events_list)