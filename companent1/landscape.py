import pygame, sys
from pygame.locals import *

class Landscape:
    def __init__(self, gate_l, plate_l):
        self.gate_location = gate_l
        self.plate_locations = plate_l
        self.plate_is_pressed = False
        self._gate_is_open = False

        self.load_img()
        self.set_rec()

    def load_img(self):
        self.gate_image = pygame.image.load('C:/Users/Dias/PycharmProjects/nFactorial-project/resources/gate_and_plate/gate.png')
        self.gate_image.set_colorkey((245, 0, 245))

        self.plate_image = pygame.image.load('C:/Users/Dias/PycharmProjects/nFactorial-project/resources/gate_and_plate/plate.png')
        self.plate_image.set_colorkey((245, 0, 245))

    def set_rec(self):
        x_cord = self.gate_location[0]
        y_cord = self.gate_location[1]
        self._gate = pygame.Rect(x_cord, y_cord, self.gate_image.get_width(),
                                 self.gate_image.get_height())

        self._plates = []
        for location in self.plate_locations:
            self._plates.append(
                pygame.Rect(location[0], location[1],
                            self.plate_image.get_width(),
                            self.plate_image.get_height()))

    def get_solid_blocks(self):
        return [self._gate]

    def get_plates(self):
        return self._plates

    def open_gate(self):
        CHUNK_SIZE = 16
        gate_x = self.gate_location[0]
        gate_y = self.gate_location[1]

        if self.plate_is_pressed and not self._gate_is_open:
            self.gate_location = (gate_x, gate_y - 2 * CHUNK_SIZE)
            self._gate.y -= 2 * CHUNK_SIZE
            self._gate_is_open = True
        if not self.plate_is_pressed and self._gate_is_open:
            self.gate_location = (gate_x, gate_y + 2 * CHUNK_SIZE)
            self._gate.y += 2 * CHUNK_SIZE
            self._gate_is_open = False