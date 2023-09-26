from random import randint

with open("lines.txt") as file:
	lines = file.readlines()
	if len(lines) > 1:
		print(lines[randint(0, len(lines) - 1)])
	elif len(lines) == 1:
		print(lines[0])