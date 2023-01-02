import json
from datetime import date
from replit import db
import time

data = {}


def check(num):
	if num % 2 == 0:
		return True
	else:
		return False


def read(file):
	with open(file) as json_file:
		data = json.load(json_file)
	return data


def a(id, towrite):
	id = str(id)
	db[id] = towrite


def b(id, towrite):
	VERSION = '1.' + str(len(read('data.json')))
	id = str(id)
	db[id]['data']['version'] = VERSION


def signup(user, password):
	VERSION = '1.' + str(len(read('data.json')))
	today = str(date.today())
	rn = str(int(time.time()))
	id = len(user) + len(password)
	if check(id):
		id = id + 15
	else:
		id = id - 15
	temp = {
	 'username': user,
	 'password': password,
	 'key': 'PLACEHOLDER_KEY',
	 'id': id,
	 'logincount': 0,
	 'version': VERSION,
	 'data': {
	  'creation_date': today,
	  'creation_time': rn,
	  'last_login': today,
	  'items': data,
	  'dev': 0
	 }
	}
	if user == 'Minejerik':
		temp['data']['dev'] = 1
	a(id, temp)
	return ('success')


def migrate(id):
	id = str(id)
	user = read('user.json')
	items = {}
	items = read('data.json')
	for i in range(0, len(user[id]['data']['items'])):
		i = str(i)
		items[i] = user[id]['data']['items'][i]
	b(id, items)


def login(user, password):
	VERSION = '1.' + str(len(read('data.json')))
	rn = str(int(time.time()))
	user = str(user)
	id = int(len(user)) + int(len(password))
	if check(id):
		id = id + 15
	else:
		id = id - 15
	id = str(id)
	temp = db[id]
	if temp['username'] == user and temp['password'] == password:
		if str(temp['version']) != str(VERSION):
			print('Account made in old version create new account')
			exit()
		global data
		global dev
		dev = int(temp['data']['dev'])
		data = temp['data']['items']
		temp['logincount'] = int(temp['logincount']) + 1
		temp['data']['last_login'] = rn
		a(id, temp)
		return True
	elif temp['username'] == user and temp['password'] != password:
		return False
	else:
		return False


def update(user, password):
	id = len(user) + len(password)
	if check(id):
		id = id + 15
	else:
		id = id - 15
	temp = db[str(id)]
	temp['data']['items'] = data
	a(id, temp)
