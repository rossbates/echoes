"""
example.py
~~~~~~~~
This module contains an example of how to instantiate and use the EchoAPI
"""


from echoes import EchoAPI
import json

echo = None

with open('config.json') as json_data_file:
	config = json.load(json_data_file)

try:
	echo = EchoAPI(config['email'], config['password'])
except Exception, e:
	print e.message
	exit()

if echo.logged_in:
	# cards are searches, Q&A, etc...
	cards = echo.cards(50)
	for c in cards:
		print c

	# todos have a type of shopping or task
	todos = echo.todos('SHOPPING_ITEM', 10)
	for t in todos:
		print t

	tasks = echo.todos('TASK', 10)
	for t in tasks:
		print t


