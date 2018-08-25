#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function
from kalendar import *
# from sender import send_sms
import datetime
import time
import json

'''
Здесь будет модуль по переключению сезонов и настройке списков
'''
# TODO: (1) написать модуль настройки программы. В нем будут корректироваться: -kalendar.py -events_base.json -preachers_base.json
events_list = summer


with open("preachers_base.json", "r") as read_file:  # ВНИМАНИЕ! ПЕРЕКЛЮЧИ В ТЕСТОВЫЙ РЕЖИМ ПЕРЕД ТЕСТИРОВАНИЕМ ПРИЛОЖЕНИЯ!
    preachers_list = json.load(read_file)


def delta_days(event, first, second):
    '''
    Функция принимает дату в формате (ГГГГ,ММ,ДД) и два цельночисленных значения,
    которые являются показателями разницы, необходимыми пользователю. В случае
    соответствия разницы между событием event и настоящим числом в любой из
    указанных интервалов, функция возвращает True

    :param event: дата вида (ГГГГ,ММ,ДД)
    :param first: цельночисленный произвольный аргумент
    :param second: цельночисленный произвольный аргумент
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

with open("events_base.json", "r") as read_file:
    events_base = json.load(read_file)

fuck = phones('2018,8,2', preachers_list, events_base)
print(fuck)