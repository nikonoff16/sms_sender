# #! python3
# # -*- coding: utf-8 -*-
#
# from __future__ import print_function
# from kalendar import summer as events_list
# from sender import send_sms
# import datetime
# import time
# import json
#
# with open("preachers_base.json", "r") as read_file:  # ВНИМАНИЕ! ПЕРЕКЛЮЧИ В ТЕСТОВЫЙ РЕЖИМ ПЕРЕД ТЕСТИРОВАНИЕМ ПРИЛОЖЕНИЯ!
#     preachers_list = json.load(read_file)
#
#
# def delta_days(event, first, second):
#     '''
#     Функция принимает дату в формате (ГГГГ,ММ,ДД) и два цельночисленных значения,
#     которые являются показателями разницы, необходимыми пользователю. В случае
#     соответствия разницы между событием event и настоящим числом в любой из
#     указанных интервалов, функция возвращает True
#
#     :param event: дата вида (ГГГГ,ММ,ДД)
#     :param first: цельночисленный произвольный аргумент
#     :param second: цельночисленный произвольный аргумент
#     :return: булева величина
#     '''
#     now = datetime.datetime.now()
#     year, month, day = (foo for foo in event)
#     # этот костыль здесь потому, что ключом в
#     # словаре является кортеж с целыми числами.
#     # другой формат хранения данных может мне помочь от него
#     # избавиться.
#     then = datetime.datetime(year, month, day)
#     delta = then - now
#     # print(delta, now, then)
#     if delta.days == second or delta.days == first:
#         # print('True')
#         return True
#     else:
#         # print('False')
#         return False
#
#
# def phones(day, preachers, events):
#     '''
#     Эта функция берет из базы событий events_base имена проповедников и забирает из preachers_base
#     номера этих проповедников и помещает их в список.
#     :param day: ключ в словаре events, по которому осуществляется поиск
#     :param preachers: словарь с телефонами проповедников
#     :param events: словарь с информацией о событиях
#     :return: список телефонов в строковом представлении.
#     '''
#     miniters = events[day]['ministers']
#     numbers = []
#     for minister in miniters:
#         phone = preachers[minister]
#         for foo in phone:
#             numbers.append(foo)
#     return numbers
#
#
# '''
# *******************************************************************************************************
# **************************************** ЦИКЛ ЖИЗНИ ПРИЛОЖЕНИЯ ****************************************
# *******************************************************************************************************
# '''
# while True:
#     # Создаем словарь для сбора статистической информации
#     with open("tech_counters.json", "r") as count_file:
#         tech_counters = json.load(count_file)
#     # Создаем пустые переменные для исключения ошибок
#     cost = 0
#     count = 0
#
#     # Подгружаем базу отработаных дней
#     with open('days_script_was_working.json', "r") as days_checked:
#         checked_days = json.load(days_checked)
#         check_day = datetime.date.__str__(datetime.date.today())
#
#     # Логгируем начало цикла
#     with open("success_log.txt", "a") as log:
#         log.write(time.ctime(time.time()))
#         cycle_number = tech_counters['cycle_counter']
#         log.write(' Cycle #' + str(cycle_number) + ' started\n')
#
#     # Создаем в памяти объект базы событий из json-объекта
#     with open("events_base.json", "r") as read_file:
#         events_base = json.load(read_file)
#
#     # Проверяем ключи словаря events_list и высчитываем разницу между ними.
#     for church_event in events_list:
#
#         if delta_days(church_event, 0, 1) and (18 <= int(time.strftime('%H', time.localtime())) < 19):
#             '''
#             Эта проверка корректной даты и времени отправки. Во втором условии проверяется час отправки,
#             чтобы не нарушать условия соглашения с смс-шлюзом
#             '''
#             row_day = [str(foo) for foo in church_event]
#             this_day = ','.join(row_day)  # Представление даты в формате словаря events_base
#             row_day.reverse()
#             correct_day = '.'.join(row_day)  # Представление даты для текста сообщения и поиска в сообщениях по логам.
#
#             if events_base[this_day]['sended'] < 2 and not checked_days.get(
#                     check_day):  # Проверка предыдущей отправки смс.
#
#                 print("Отправляю смс всем братьям", correct_day)
#                 text = "Это Витя О. С этого номера будут приходить СМС, если согласимся на это."
#                 print(text)
#                 admin_text = ', '.join(events_base[this_day]['ministers']) + ' должны получить смс о ' + correct_day
#                 count, cost = send_sms(phones(this_day, preachers_list, events_base), text)
#                 count, cost = send_sms([preachers_list['Осипов Виктор']], admin_text)
#
#
#     # Перезаписываем файл базы событий
#     with open("events_base.json", "w") as write_file:
#         events_base = json.dump(events_base, write_file)
#
#     with open("success_log.txt", "a") as log:
#         log.write(time.ctime(time.time()))
#         log.write(' Cycle #' + str(cycle_number) + ' finised\n')
#
#     # Перезаписываем статистические данные
#     tech_counters['cycle_counter'] += 1
#     tech_counters['sms_counter'] += count
#     tech_counters['total_cost'] += cost
#     # Итерируем счетчик циклов
#     with open("tech_counters.json", "w") as write_file:
#         tech_counters = json.dump(tech_counters, write_file)
#
#     print("Sleeping for an hour")
#     time.sleep(3600)  # Это задержка на 3 часа.
#
# # check_kalendar(events_list, events_base)
