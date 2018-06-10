#! python3
# -*- coding: utf-8 -*-

from __future__ import print_function
from  kalendar import *
import gammu
import datetime
import time

import sys

def send_sms(phone_number, text):
    sm = gammu.StateMachine()
    sm.ReadConfig()
    sm.Init()

    smsinfo = {
        'Class': -1,
        'Unicode': True,
        'Entries': [
            {
                'ID': 'ConcatenatedTextLong',
                'Buffer': text
            }
        ]}
    encoded = gammu.EncodeSMS(smsinfo)

    for message in encoded:
        message['SMSC'] = {'Location': 1}
        message['Number'] = phone_number
        message['Coding'] = 'Unicode_No_Compression'
        sm.SendSMS(message)
    # message = {'Text': text,
    #            'SMSC':{'Location': 1},
    #            'Coding': 'Unicode_No_Compression',
    #            'Unicode': True,
    #            'Number': phone_number}
    # sm.SendSMS(message)

def check_kalendar(events_list, preachers_list, text):
    # Проверяем ключи словаря events_list и высчитываем разницу между ними.
    while True:
        for church_event in events_list:

            now = datetime.datetime.now()
            year, month, day = (foo for foo in church_event)
            then = datetime.datetime(year, month, day)

            delta = then - now

            if delta.days == 6 or delta.days == 2:

                for preacher in events_list[church_event]:

                    for number in preachers_list[preacher]:
                        send_sms(number, text)
            else:
                print('No events today')

            time.sleep(10)

check_kalendar(events_list, preachers_list, text)