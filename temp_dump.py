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
                    'sended': 0
    },
    '2018,7,22': {
                    'day': 'sunday',
                    'ministers': ["Горбаль Василий", "Крыгин Юрий"],
                    'type': 'Preaching',
                    'theme': '',
                    'sended': 0
    },
    '2018,7,28': {
                    'day': 'saturday',
                    'ministers': ["Николай Новиков"],
                    'type': 'Bible Teaching',
                    'theme': '',
                    'sended': 0
    },
    '2018,7,29': {
                    'day': 'sunday',
                    'ministers': ["Лобанов Алексей", "Юровских Андрей"],
                    'type': 'Preaching',
                    'theme': '',
                    'sended': 0
    },
    '2018,8,4': {
                    'day': 'saturday',
                    'ministers': ["Агафонов Борис"],
                    'type': 'Preaching',
                    'theme': '',
                    'sended': 0
    },
    '2018,8,5': {
                    'day': 'sunday',
                    'ministers': ["Горлов Андрей", "Крыгин Юрий"],
                    'type': 'Preaching',
                    'theme': '',
                    'sended': 0
    },
    '2018,8,6': {
        'day': 'sunday',
        'ministers': ["Горлов Андрей", "Крыгин Юрий", "Новиков Николай", "Юровских Андрей", "Тропин Владимир",
                      "Горбаль Василий", "Новиков Эдуард", "Новиков Павел", "Осипов Виктор"],
        'type': 'Preaching',
        'theme': '',
        'sended': 0
    },
    '2018,8,11': {
                    'day': 'saturday',
                    'ministers': ["Новиков Николай"],
                    'type': 'Bible Teaching',
                    'theme': '',
                    'sended': 1
    },
    '2018,8,12': {
                    'day': 'sunday',
                    'ministers': ["Лобанов Алексей", "Мальцев Максим"],
                    'type': 'Preaching',
                    'theme': '',
                    'sended': 0
    },
    '2018,8,18': {
                    'day': 'saturday',
                    'ministers': ["Новиков Николай"],
                    'type': 'Bible Teaching',
                    'theme': '',
                    'sended': 0
    },
    '2018,8,19': {
                    'day': 'sunday',
                    'ministers': ["Новиков Эдуард", "Юровских Андрей"],
                    'type': 'Preaching',
                    'theme': '',
                    'sended': 0
    },
    '2018,8,25': {
                    'day': 'saturday',
                    'ministers': ["Новиков Николай"],
                    'type': 'Bible Teaching',
                    'theme': '',
                    'sended': 0
    },
    "2018,8,26": {
                    'day': 'sunday',
                    'ministers': ["Осипов Виктор", "Соболев Виктор"],
                    'type': 'Preaching',
                    'theme': '',
                    'sended': 0
    }
}

with open('events_base.json', 'w') as write_file:
    json.dump(events_list, write_file)

preachers_base = {
  "Агафонов Борис": [""],
  "Горбаль Василий": ["79058505447"],
  "Горлов Андрей": ["79058517750"],
  "Гуляк Виктор": ["79828043024"],
  "Крыгин Юрий": ["79125232003"],
  "Лобанов Алексей": ["79068838045"],
  "Мальцев Максим": ["79136809349"],
  "Мельников Олег": ["79025910204"],
  "Новиков Николай": ["79128326978"],
  "Новиков Павел": ["79125744404"],
  "Новиков Эдуард": ["79128374707"],
  "Осипов Виктор": ["79129760922", "79965574689"],
  "Соловьев Виктор": ["79634381021"],
  "Тропин Владимир": ["79088329661", "79292292612"],
  "Юровских Андрей": ["79630101443"]
}
test_base = {
  "Агафонов Борис": ["79195628785"],
  "Горбаль Василий": ["79195628785"],
  "Горлов Андрей": ["79195628785"],
  "Гуляк Виктор": ["79195628785"],
  "Крыгин Юрий": ["79195628785"],
  "Лобанов Алексей": ["79195628785"],
  "Мельников Олег": ["79195628785"],
  "Мальцев Максим": ["79136809349"],
  "Новиков Николай": ["79195628785"],
  "Новиков Павел": ["79195628785"],
  "Новиков Эдуард": ["79195628785"],
  "Осипов Виктор": ["79129760922"],
  "Соловьев Виктор": ["79195628785"],
  "Тропин Владимир": ["79195628785"],
  "Юровских Андрей": ["79195628785"]
}
#
with open('preachers_base.json', 'w') as write_file:
    json.dump(preachers_base, write_file)

with open('test_base.json', 'w') as write_file:
    json.dump(test_base, write_file)

tech_counters = {
    'cycle_counter': 28,
    'sms_counter': 9,
    'total_cost': 27.28,
    'season': 'summer'
}
#
with open('tech_counters.json', 'w') as write_file:
    json.dump(tech_counters, write_file)

days = {}

# with open('days_script_was_working.json', 'w') as write_file:
#     json.dump(days, write_file)
