#!/bin/python3
from collections import nametuple
import pygame
import sys
import time

W = 804

H = 600

RED_COLOR = 200, 0, 0

WHITE_COLOR = 200, 200, 200

GOLD_COLOR = 205, 145, 0

'''
make the ball object for the game

using math, and tuples 
'''

ball = Rect((W/2, H/2), (30, 30))
Direction = namedtuple('Direction', 'x y')
ball_dir = Direction(5, -5)

bat = Rect((W/2, 0.96 * H), (120, 15))


class Block(Rect):

    def __init__(self, colour, rect):
        Rect.__init__(self, rect)
        self.colour = colour
