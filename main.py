#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function
from sender import send_sms
import datetime
import time
import json

'''
Здесь будет модуль по переключению сезонов и настройке списков
'''
# TODO: (1) написать модуль настройки программы. В нем будут корректироваться: -kalendar.py -events_base.json -preachers_base.json


with open("preachers_base.json", "r") as read_file:  # ВНИМАНИЕ! ПЕРЕКЛЮЧИ В ТЕСТОВЫЙ РЕЖИМ ПЕРЕД ТЕСТИРОВАНИЕМ ПРИЛОЖЕНИЯ!
    preachers_list = json.load(read_file)


def delta_days(event, first, second, FromTo=False):
    '''
    Функция принимает дату в формате (ГГГГ,ММ,ДД) и два цельночисленных значения,
    которые являются показателями разницы, необходимыми пользователю. В случае
    соответствия разницы между событием event и настоящим числом в любой из
    указанных интервалов, функция возвращает True

    :param event: дата вида (ГГГГ,ММ,ДД)
    :param first: цельночисленный произвольный аргумент
    :param second: цельночисленный произвольный аргумент
    :param FromTo: переключение между точечным и интервальным режимом работы
    :return: булева величина
    '''
    now = datetime.datetime.now()
    year, month, day = (foo for foo in event)
    # этот костыль здесь потому, что ключом в
    # словаре является кортеж с целыми числами.
    # другой формат хранения данных может мне помочь от него
    # избавиться.
    then = datetime.datetime(year, month, day)
    delta = then - now
    # print(delta, now, then)
    if FromTo:
        if delta.days > first and delta.days < second:
            # print('True')
            return True
        else:
            # print('False')
            return False
    else:    
        if delta.days == second or delta.days == first:
            # print('True')
            return True
        else:
            # print('False')
            return False


def phones(day, preachers, events, all=False):
    '''
    Эта функция берет из базы событий events_base имена проповедников и забирает из preachers_base
    номера этих проповедников и помещает их в список.
    :param day: ключ в словаре events, по которому осуществляется поиск
    :param preachers: словарь с телефонами проповедников
    :param events: словарь с информацией о событиях
    :param all: при намеренном включении инициируется альтернативный сценарий 
                работы функции - сбор всех нормеров из базы
    :return: список телефонов в строковом представлении.
    '''
    if all:
        numbers = []
        for preacher in preachers_list.keys():
            numbers.append(preachers_list[preacher][0])
    if not all:
        miniters = events[day]['ministers']
        numbers = []
        for minister in miniters:
            phone = preachers[minister]
            for foo in phone:
                numbers.append(foo)
    return numbers

def dates(church_event, for_script=False, for_message=False):
    ''' 
    Эта проверка корректной даты и времени отправки. Во втором условии проверяется час отправки,
    чтобы не нарушать условия соглашения с смс-шлюзом
    '''
    row_day = [str(foo) for foo in church_event]
    this_day = ','.join(row_day)  # Представление даты в формате словаря events_base
    row_day.reverse()
    correct_day = '.'.join(row_day)  # Представление даты для текста сообщения и поиска в сообщениях по логам.
    if not for_script and not for_message:
        return this_day, correct_day
    if for_script and not for_message:
        return this_day
    if for_message and not for_script:
        return correct_day
    if for_message and for_script:  # На дурака
        return this_day, correct_day


''' 
*******************************************************************************************************
**************************************** ЦИКЛ ЖИЗНИ ПРИЛОЖЕНИЯ ****************************************
******************************************************************************************************* 
'''
while True:
    # Создаем словарь для сбора статистической информации
    with open("tech_counters.json", "r") as count_file:
        tech_counters = json.load(count_file)
    # Создаем пустые переменные для исключения ошибок
    cost = 0
    count = 0

    # Подгружаем базу отработаных дней
    with open('days_script_was_working.json', "r") as days_checked:
        checked_days = json.load(days_checked)
        check_day = datetime.date.__str__(datetime.date.today())

    # Логгируем начало цикла
    with open("success_log.txt", "a") as log:
        log.write(time.ctime(time.time()))
        cycle_number = tech_counters['cycle_counter']
        log.write(' Cycle #' + str(cycle_number) + ' started\n')

    # Создаем в памяти объект базы событий из json-объекта
    with open("events_base.json", "r") as read_file:
        events_base = json.load(read_file)

    # Замена старого kalendar.py (Одна ошибка с этим файлом помешала мне запустить скрипт вовремя.)
    events_row = [(foo.split(',')) for foo in events_base.keys()]
    events_list = []
    for ev in events_row:
        fuck = []
        for string in ev:
            fuck.append(int(string))
        fuck = tuple(fuck)
        events_list.append(fuck)

    # Функция Дайджест проповедника ОНА НАСТРОЕНА ИСКЛЮЧИТЕЛНО НА РАБОТУ С ТРЕХЧАСОВЫМИ ПЕРИОДАМИ БЕЗДЕЙСТВИЯ!!!
    # if (time.strftime("%a") == "Thu") and (6 <= int(time.strftime('%H', time.localtime())) < 21):
    if (time.strftime("%a") == "Fri") and (18 <= int(time.strftime('%H', time.localtime())) < 21):
        weekly_events = []
        messages = ["Новости служения"]
        for church_event in events_list:
            if delta_days(church_event, 1, 7, FromTo=True):
                weekly_events.append(church_event)
        for ev in weekly_events:
            text = dates(ev, for_message=True)
            den = dates(ev, for_script=True)
            if events_base[den]["type"] == "Bible Teaching":
                text += " Разбор"
            if events_base[den]["type"] == "Preaching":
                text += " Служение"
            text += " ведут "
            text += ', '.join(events_base[den]['ministers'])
            if events_base[den]['theme']:
                text += '. Тема: ' + events_base[den]['theme']
            # print(text, len(text))
            messages.append(text)
        messages = ' '.join(messages)
        print(messages, weekly_events)
        count, cost = send_sms(phones("This dosen't matter", preachers_list, events_base, all=True), messages)

    # Отправка предупреждений о братском молитвенном ОНА НАСТРОЕНА ИСКЛЮЧИТЕЛНО НА РАБОТУ С ТРЕХЧАСОВЫМИ ПЕРИОДАМИ БЕЗДЕЙСТВИЯ!!!
    if (time.strftime("%a") == "Wed") and (9 <= int(time.strftime('%H', time.localtime())) < 12):
        msg = 'Сегодня молитва в 20:00 у пастора'
        count, cost = send_sms(phones("This dosen't matter", preachers_list, events_base, all=True), msg)

        


    # Проверяем ключи словаря events_list и высчитываем разницу между ними.
    for church_event in events_list:
        
        # Отправка сообщений непосредственным участникам служений
        if delta_days(church_event, 2, 5) and (9 <= int(time.strftime('%H', time.localtime())) < 22):       

            this_day, correct_day = dates(church_event)

            if events_base[this_day]['sended'] < 2 and not checked_days.get(
                    check_day):  # Проверка предыдущей отправки смс.

                if events_base[this_day]['type'] == 'Preaching':
                    text = correct_day + " Вы проповедуете в церкви Слово Жизни. Тема: " + events_base[this_day]['theme']
                    admin_text = ', '.join(events_base[this_day]['ministers']) + ' проповедуют ' + correct_day + '. Тема: ' + events_base[this_day]['theme']
                    print(text, '\n', admin_text)
                    count, cost = send_sms(phones(this_day, preachers_list, events_base), text)
                    count, cost = send_sms([
                        preachers_list['Осипов Виктор'], 
                        preachers_list['Новиков Николай'], 
                        preachers_list['Новиков Павел']
                        ], admin_text)

                if events_base[this_day]['type'] == 'Bible Teaching':
                    text = correct_day + " Вы ведете разбор Библии; Текст: " + events_base[this_day]['theme']
                    # TODO: (3) прикрутить функцию send_email для отправки сообщений по почте (ее можно вызывать и в send_sms)
                    admin_text = ', '.join(events_base[this_day]['ministers']) + ' ведет разбор ' + correct_day  + '. Текст: ' + events_base[this_day]['theme']
                    print(text, '\n', admin_text)
                    count, cost = send_sms(phones(this_day, preachers_list, events_base), text)
                    count, cost = send_sms([
                        preachers_list['Осипов Виктор'], 
                        preachers_list['Новиков Николай'], 
                        preachers_list['Новиков Павел']
                        ], admin_text)

                events_base[this_day]['sended'] += 1  # Перезапись таблицы после отправки (не факт что успешной)
                checked_days[check_day] = True  # Отметка об отправке в этот день

                with open('days_script_was_working.json', "w") as days_checked:
                    checked_days = json.dump(checked_days, days_checked, indent=4, ensure_ascii=False,)
    # Контроль работы программы (отправка сообщения админу о работе)
    # TODO: (4) написать код, отправляющий на емайл админу оповещение о работе с отчетом из логов.
    # https://habr.com/company/pechkin/blog/281915/

    # Напоминание о необходимости создавать новый список
    # TODO: (2) создать проверку наличия списка на следущий сезон.

    # Перезаписываем файл базы событий
    with open("events_base.json", "w") as write_file:
        events_base = json.dump(events_base, write_file, indent=4, ensure_ascii=False,)

    # Логгируем завершение цикла
    with open("success_log.txt", "a") as log:
        log.write(time.ctime(time.time()))
        log.write(' Cycle #' + str(cycle_number) + ' finised\n')

    # Перезаписываем статистические данные
    tech_counters['cycle_counter'] += 1
    tech_counters['sms_counter'] += count
    tech_counters['total_cost'] += cost
    # Итерируем счетчик циклов
    with open("tech_counters.json", "w") as write_file:
        tech_counters = json.dump(tech_counters, write_file, indent=4, ensure_ascii=False,)

    print("Sleeping for 3 hours")
    time.sleep(10800)  # Это задержка на 3 часа.
