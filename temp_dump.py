import json

# data = {
#     'login': 'fuck',
#     'myapi': 'fuck'
# }
#
# with open('api.json', 'w') as write_file:
#     json.dump(data, write_file)

# Example of deserialization

# with open("api.json", "r") as read_file:
#     data = json.load(read_file)

events_list = {
    '2018,7,21': {
                    'day': 'saturday',
                    'ministers': ['Осипов Виктор'],
                    'type': 'Bible Teaching',
                    'theme': '2 Коринфянам 12',
                    'sended': False
    },
    '2018,7,22': {
                    'day': 'sunday',
                    'ministers': ["Горбаль Василий", "Крыгин Юрий"],
                    'type': 'Preaching',
                    'theme': '',
                    'sended': False
    },
    '2018,7,28': {
                    'day': 'saturday',
                    'ministers': ["Николай Новиков"],
                    'type': 'Bible Teaching',
                    'theme': '',
                    'sended': False
    },
    '2018,7,29': {
                    'day': 'sunday',
                    'ministers': ["Лобанов Алексей", "Юровских Андрей"],
                    'type': 'Preaching',
                    'theme': '',
                    'sended': False
    },
    '2018,8,4': {
                    'day': 'saturday',
                    'ministers': ["Агафонов Борис"],
                    'type': 'Preaching',
                    'theme': '',
                    'sended': False
    },
    '2018,8,5': {
                    'day': 'sunday',
                    'ministers': ["Горлов Андрей", "Крыгин Юрий"],
                    'type': 'Preaching',
                    'theme': '',
                    'sended': False
    },
    '2018,8,11': {
                    'day': 'saturday',
                    'ministers': ["Новиков Николай"],
                    'type': 'Bible Teaching',
                    'theme': '',
                    'sended': False
    },
    '2018,8,12': {
                    'day': 'sunday',
                    'ministers': ["Лобанов Алексей", "Новиков Павел"],
                    'type': 'Preaching',
                    'theme': '',
                    'sended': False
    },
    '2018,8,18': {
                    'day': 'saturday',
                    'ministers': ["Новиков Николай"],
                    'type': 'Bible Teaching',
                    'theme': '',
                    'sended': False
    },
    '2018,8,19': {
                    'day': 'sunday',
                    'ministers': ["Новиков Эдуард", "Юровских Андрей"],
                    'type': 'Preaching',
                    'theme': '',
                    'sended': False
    },
    '2018,8,25': {
                    'day': 'saturday',
                    'ministers': ["Новиков Николай"],
                    'type': 'Bible Teaching',
                    'theme': '',
                    'sended': False
    },
    "2018,8,26": {
                    'day': 'sunday',
                    'ministers': ["Осипов Виктор", "Соболев Виктор"],
                    'type': 'Preaching',
                    'theme': '',
                    'sended': False
    }
}

with open('events_base.json', 'w') as write_file:
    json.dump(events_list, write_file)


}
#
# with open('preachers_base.json', 'w') as write_file:
#     json.dump(preachers_base, write_file)
#
# with open('test_base.json', 'w') as write_file:
#     json.dump(test_base, write_file)

tech_counters = {
    'cycle_counter': 0,
    'sms_counter': 0,
    'total_cost': 0
}
#
# with open('tech_counters.json', 'w') as write_file:
#     json.dump(tech_counters, write_file)
