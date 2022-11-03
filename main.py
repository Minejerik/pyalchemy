import os
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
	pa = input('Password?\n')
	my_secret = os.environ['pass']
	if pa != my_secret:
		clear()
		print('WRONG\n')
		start()
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

def clearquest():
	temp = input('Do you want to clear your progress?\n')
	if temp == 'y':
		print('clearing!')
		for i in range(1,len(login.data)+1):
			login.data[str(i)] = 0
		login.data['1'] = 1
		login.data['2'] = 1
		login.data['3'] = 1
		login.data['4'] = 1
		login.update(user,pas)
	else:
		clear()
		print('stopping!')
		main()

def main():
	temp = read()
	data = login.data
	for i in range(1, len(data) + 1):
		if data[str(i)] == 1 or login.dev == 1:
			print( '{}			{}'.format(temp[str(i)]['name'],i))
	rep = input('Recipe 1,2\n')
	if rep == 'reset':
		clear()
		clearquest()
	if len(rep) < 3:
		clear()
		print('Invalid recipe!\n')
	tempk = rep.split(',')
	if data[str(tempk[0])] == 1 and data[str(tempk[1])] == 1: 
		for i in range(1, len(data) + 1):
			tt = temp[str(i)]['recipe']
			tedata = str(tt)
			if rep == tedata:
				data[str(i)] = 1
				login.update(user, pas)
				clear()
				print(temp[str(i)]['name'] + ' unlocked\n')
				main()
	clear()
	print('Invalid recipe!\n')
	main()


def start():
	login.data = login.read('data.json')
	temp = input('[1] Login [2] Sign up\n')
	if temp == 'admin':
		clear()
		print('adding console')
		write()
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