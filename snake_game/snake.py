#/usr/bin/python

'''Python snake game

Author: Elvin Ramirez


'''

import pygame
import sys

from pygame.locals import *

# class to handle the main function of the game


class SnakeMain:
    # parametar with = passing it as a option
    # default will be 250 x 250

    def __init__(self, width=250, height=250):
        # initial the pygame
        pygame.init()

        # Self Window
        self.width = in_Width
        self.height = in_Height

        # window title

        pygame.display.set_caption("Py Snake")

        # center window

        os.environ["SDL_VIDEO_WINDOW_POS"] = "center"

        " generate screen"

        self.screen = pygame.display.set_mode((self.width, self.height))

if __name__ == '__main__':
    main = SnakeMain()
