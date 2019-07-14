#!/usr/local/bin/python3

'''Python snake game
Author: Elvin Ramirez


'''

import pygame
import sys

import os

from pygame.locals import *

# class to handle the main function of the game


class SnakeMain:
    # parametar with = passing it as a option
    # default will be 250 x 250

    def __init__(self, in_Width=250, in_Height=250):
        # initial the pygame
        pygame.init()

        # Self Window
        self.width = in_Width
        self.height = in_Height

        # window title

        pygame.display.set_caption("Py Snake")

        # center window

        os.environ["SDL_VIDEO_WINDOW_POS"] = "center"

        # generate screen

        self.screen = pygame.display.set_mode((self.width, self.height))

    def MainLoop(self):
        # main loop for the game
        while True:
            # handle each event
            self.EventsHandler()

            # background = BackGround()
            # background.draw()

            # update screen

            # PySnake.screen.flip()
            
    def EventsHandler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


class BackGround():
        # main methods to BG

    def __init__(self):

        background_file = "background.png"

        self.image = pygame.image.load(background_file).convert()

    def draw(self):
        PySnake.screen.blit(self.image, (0, 0))


if __name__ == '__main__':
    # create an instances of Py Snake

    PySnake = SnakeMain()
    PySnake.MainLoop()
