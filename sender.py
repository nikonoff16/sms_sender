#! python3
# -*- coding: utf-8 -*-

import kalendar
import gammu


def send_sms(preacher, phone_number, text):
    sm = gammu.StateMachine()
    sm.ReadConfin()
    sm.Init()

    message = {'Text': text,
               'SMSC':{'Location': 1},
               'Number': phone_number}

def check_kalendar(kalendar):
    # some code here
    # Нужно разобраться с тем, как работает время отправки.


