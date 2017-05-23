#!/usr/bin/python3

from random import * 

user_score = 0

pc_score = 0

def hangeman(man):
	screen = [
	"""
	+--------+
	|
	|
	|
	|
	|
	|
	===========
	""",
	"""
	+--------+
	|        |
	|        o
	|
	|
	|
	|
	===========
	""",
	"""
	+--------+
	|        |
	|        o
	|        |
	|
	|
	|
	===========
	""",
	"""
	+--------+
	|        |
	|        o
	|       -|-
	|       / \
	|
	|
	===========
	""",
	]


	print screen[man]
	return