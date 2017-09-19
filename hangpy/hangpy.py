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


	print (screen[man])
	return

def start():
    print ("Lets start to play hang py")
    while game():
        pass
    score()

def game():
	


def letters_guess():
	print()
	letter = raw_input("Take a guess at the hidden word:")
	letter.strip()
	letter.lower()
	print()
	return letter
	
def replay():

def score():


