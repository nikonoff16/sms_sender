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
                    'ministers': ['Osipov Viktor'],
                    'type': 'Bible Teaching',
                    'theme': '2 Коринфянам 12'
    },
    '2018,7,22': {
                    'day': 'sunday',
                    'ministers': ["Gorbal Vasiliy", "Krygin Yuriy"],
                    'type': 'Preaching',
                    'theme': ''
    },
    '2018,7,28': {
                    'day': 'saturday',
                    'ministers': ["Novikov Nikolay"],
                    'type': 'Bible Teaching',
                    'theme': ''
    },
    '2018,7,29': {
                    'day': 'sunday',
                    'ministers': ["Lobanov Alexey", "Yurovskich Andrey"],
                    'type': 'Preaching',
                    'theme': ''
    },
    '2018,8,4': {
                    'day': 'saturday',
                    'ministers': ["Agafonov Boris"],
                    'type': 'Preaching',
                    'theme': ''
    },
    '2018,8,5': {
                    'day': 'sunday',
                    'ministers': ["Gorlov Andrey", "Krygin Yuriy"],
                    'type': 'Preaching',
                    'theme': ''
    },
    '2018,8,11': {
                    'day': 'saturday',
                    'ministers': ["Novikov Nikolay"],
                    'type': 'Bible Teaching',
                    'theme': ''
    },
    '2018,8,12': {
                    'day': 'sunday',
                    'ministers': ["Lobanov Alexey", "Novikov Pavel"],
                    'type': 'Preaching',
                    'theme': ''
    },
    '2018,8,18': {
                    'day': 'saturday',
                    'ministers': ["Novikov Nikolay"],
                    'type': 'Bible Teaching',
                    'theme': ''
    },
    '2018,8,19': {
                    'day': 'sunday',
                    'ministers': ["Novikov Edward", "Yurovskich Andrey"],
                    'type': 'Preaching',
                    'theme': ''
    },
    '2018,8,25': {
                    'day': 'saturday',
                    'ministers': ["Novikov Nikolay"],
                    'type': 'Bible Teaching',
                    'theme': ''
    },
    "2018,8,26": {
                    'day': 'sunday',
                    'ministers': ["Osipov Viktor", "Solovev Viktor"],
                    'type': 'Preaching',
                    'theme': ''
    }
}

with open('events_base.json', 'w') as write_file:
    json.dump(events_list, write_file)