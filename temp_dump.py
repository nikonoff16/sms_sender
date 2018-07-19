import json

data = {
    'login': 'v.osipov08@gmail.com',
    'myapi': 'ar5usaj8YpyFxXgx1Yj3oRZoxf6W'
}

with open('api.json', 'w') as write_file:
    json.dump(data, write_file)

# Example of deserialization

# with open("api.json", "r") as read_file:
#     data = json.load(read_file)