#! python3
#! -*- coding: utf-8 -*-

'''
Module manifest
The module should interact with *.json files in the program and provide for that human-frendly 
interface. 
The core functionality: change or create events_base and preachers_base files through one console window. 

Bussiness logic:
- Show current state of events_base and preachers_base
- Ask is it right that user wants to setup the program
- If user acsepts the request, ask him what time period he is going to setup (by default it shall be 92 days 
  and starts from last date in event_base)
- The scrit starts for cycle and parses every date in that period. 
- The processors - the big il-elif-else construction - shall manage different event rules.
- The rules may relate to the weekday, day of the month (25.12, 07.01) or any other calculated church event, like Pascha.
	- Every rule shall have its own theme marker.
- Every rule shall use create_event() function. 
- Every event shall have following points:
	- Preachers
	- Leaders
	- Proposal text
- When an iteration ends, script shall update json-file with new data.
- When the cycle ends, script shall
	- create a copy of json-file and place it in designated directory
	- delete all the events, that is older then current date
'''
import json 
import datetime
import time

# Creating global variables
try:
	with open("preachers_base.json", "r") as read_file:
		preachers_list = json.load(read_file)
except FileNotFoundError:
	preachers_list = {}

try:
	with open("events_base.json", "r") as read_file:
		events_base = json.load(read_file)
except FileNotFoundError:
	events_base = {}

try:
	with open("api.json", "r") as api_file:
		api = json.load(api_file)
except FileNotFoundError:
	api = {"login": 0, "myapi": 0}

# Creating date-variables 
# I don't know for sure what date standard I would use in the main cycle, so let it be both there.s	

date_cur_date = datetime.datetime.now()
str_cur_date = str(date_cur_date)[:10]  # I need only YYYY-MM-DD date format, so by slicing to 10 I make it



print(date_cur_date, str_cur_date)


