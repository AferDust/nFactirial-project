import pygame, sys

from pygame.locals import *
pygame.init()
pygame.display.set_caption('Fireboy and Watergirl')


WINDOW_SIZE = (900, 600)
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()