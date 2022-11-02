import json
import login
from os import system, name

filename = 'items.json'


def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')


def read():
	with open(filename) as json_file:
		data = json.load(json_file)
	return data


def write():
	data = read()
	h = login.read('data.json')
	id = input('id?\n')
	recipe = input('recipe?\n')
	name = input('name?\n')
	data[id] = {
	 'recipe': recipe,
	 'name': name,
	}
	h[id] = 0
	f = open(filename, 'w')
	temp = json.dumps(data, indent=3, sort_keys=False)
	f.write(temp + '\n')
	f.close()
	f = open('data.json', 'w')
	temp = json.dumps(h, indent=3, sort_keys=False)
	f.write(temp + '\n')
	f.close()


def main():
	temp = read()
	data = login.data
	for i in range(1, len(data) + 1):
		if data[str(i)] == 1:
			print(temp[str(i)]['name'], '		', i)
	rep = input('Recipe 1/2\n')
	if len(rep) < 3:
		clear()
		print('Invalid recipe!\n')
	for i in range(1, len(data) + 1):
		print(temp[str(i)])
		tt = temp[str(i)]['recipe']
		tedata = str(tt)
		if rep == tedata:
			data[str(i)] = 1
			login.update(user, pas)
			clear()
			print(temp[str(i)]['name'] + ' unlocked\n')
			main()
	clear()
	print('not recipe\n')
	main()


def start():
	login.data = login.read('data.json')
	temp = input('[1] Login [2] Sign up\n')
	clear()
	if temp == '1':
		global user
		global pas
		user = input('Username?\n')
		pas = input('Password?\n')
		temp = login.login(user, pas)
		if temp == True:
			main()
		elif temp == False:
			print('Wrong Password')
	elif temp == '2':
		login.signup(input('Username?\n'), input('Password?\n'))
		clear()
		start()


start()
#write()
