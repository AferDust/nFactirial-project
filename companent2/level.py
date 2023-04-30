import pygame, sys
from pygame.locals import *

class Level_Selected():
    def __init__(self):
        self.load_img()

    def load_img(self):
        self.screen = pygame.image.load('C:/Users/Dias/PycharmProjects/nFactorial-project/resources/screen-pages/select_screen.png')
        self.screen.set_colorkey((0, 0, 0))

        self.titles = {
            1: pygame.image.load('C:/Users/Dias/PycharmProjects/nFactorial-project/resources/screen-pages/l1.png'),
            2: pygame.image.load('C:/Users/Dias/PycharmProjects/nFactorial-project/resources/screen-pages/l2.png'),
            3: pygame.image.load('C:/Users/Dias/PycharmProjects/nFactorial-project/resources/screen-pages/l3.png'),
        }
        for title in self.titles.keys():
            self.titles[title].set_colorkey((245, 0, 245))

        self.indicator_img = pygame.image.load('C:/Users/Dias/PycharmProjects/nFactorial-project/resources/screen-pages/indicator.png')
        self.indicator_img.set_colorkey((245, 0, 245))