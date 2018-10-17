#! python3
#! -*- coding: utf-8 -*-

'''
Module manifest
The module should interact with *.json files in the program and provide for that humanreadable 
interface. 
The core functionality is to change or create events base and preachers base (events_base and
preachers_base accordingly in the code) through one console window. 

Bussiness logic:
- Show current state of events_base and preachers_base
- Ask is it right that user wants to setup the program
- If user acsepts the request, ask him what time period he going to setup (by default it shall be 92 days 
  and starts from last date in event_base)
- The scrit starts for cycle and parses every date in that period. 
- Translate it next time you will be here: 	• Обработчики - большая конструкция из if-elif-…-else, которая отрабатывает различные правила событий.
	• Правила могут относиться ко дню недели (сб, вс), дню месяца (25.12, 07.01), или конкретному календарному событию (прописать список таковых на лет 50 вперед, или формулу их вписать в правило). 
		○ С каждом правиле есть указатель темы. 
	• В правиле для создания события нужно использовать функцию create_event()
	• Если правило события, то открывается форма создания события, в которой пользователь заполняет: 
		○ Проповедники
		○ Ведущие собрания
		○ Рекомендуемый текст
	• По завершению в итерации - создание json-файла из словаря, в который аугментируются созданные события. (Чтобы не потерять результаты в случае сбоя программы на очередном этапе.)
По завершении цикла создать копию списка в отдельную папку и удалить те значения в списке, которые стоят высше текущей даты. 
'''