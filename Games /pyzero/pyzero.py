#!/usr/bin/python3

import collections
import pygame
import sys
import time

W = 804

H = 600

RED_COLOR = 200, 0, 0

WHITE_COLOR = 200, 200, 200

GOLD_COLOR = 205, 145, 0

"""
make the ball object for the game

using math, and tuples 
"""

ball = Rect((W / 2, H / 2), (30, 30))

Direction = namedtuple("Direction", "x y")

ball_dir = Direction(5, -5)

bat = Rect((W / 2, 0.96 * H), (120, 15))


class Block(Rect):
    def __init__(self, colour, rect):

        Rect.__init__(self, rect)

        self.colour = colour


block = []


for n_block in range(24):
    block = Block(
        GOLD_COLOR, ((((n_block % 8) * 100) + 2, ((n_block // 8) * 25) + 2), (96, 23))
    )
    block.append(block)


def draw_block():
    for block in blocks:
        screen.draw.filled_rect(block, block.colour)
