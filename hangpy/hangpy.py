#!/usr/bin/python3

from random import *

# create variable for then whole game
user_score = 0
pc_score = 0

# simple graphic


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

    print(screen[man])
    return


def start():
    print("Lets start to play hang py")
    while game():
        pass
    score()

# majority of the games function


def game():
    #  Quickly set word for player
    word_dictinary = ["Linux", "magic", "kitty", "playstation"]
    word = choice(word_dictinary)
    word_length = len(word)
    # rules for individual
    clue = word_length * ["_"]
    tries = 6
    letter_tried = ""
    guesses = 0
    letters_correct = 0
    letter_wrong = 0
    global pc_score, user_score
    # loop for player selection
    while (letter_tried != tries) and ("".join(clue) != word):
    	# call the function letters_guess
    	letter = letters_guess()
    	if len(letter) == 1 and letter.isalpha():
    		if letter_tried.find(letter) != -1:
    			print("This letter was used already", letter)
    			

def letters_guess():
    print()
    letter = raw_input("Take a guess at the hidden word:")
    letter.strip()
    letter.lower()
    print()
    return letter


def replay():
	return


def score():
	return