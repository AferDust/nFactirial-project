import pygame, sys
from pygame.locals import *

class Doors:
    def __init__(self):
        self.player_at_door = False
        self._height_raised = 0
        self._door_open = False

        self.load_img()
        self.set_rec()

    def load_img(self):
        self.frame_image = pygame.image.load("resources/doors_img/frame.png")
        self.frame_image.set_colorkey((255, 0, 255))
        self.door_background = pygame.image.load("resources/doors_img/background.png")

    def set_rec(self):
        x_cord = self.door_location[0]
        y_cord = self.door_location[1]
        self._rect = pygame.Rect(x_cord, y_cord, self.door_image.get_width(),
                                 self.door_image.get_height())

    def get_door(self):
        return self._rect

    def is_door_open(self):
        return self._door_open

    def raise_door(self):
        DOOR_SPEED = 1.5
        door_x = self.door_location[0]
        door_y = self.door_location[1]
        if self.player_at_door and not self._door_open:
            self.door_location = (door_x, door_y - DOOR_SPEED)
            self._height_raised += DOOR_SPEED
            if self._height_raised >= 31:
                self._door_open = True
        elif not self.player_at_door and self._height_raised > 0:
            self.door_location = (door_x, door_y + DOOR_SPEED)
            self._height_raised -= DOOR_SPEED
            self._door_open = False

class Fire_Door(Doors):
    def __init__(self, door_location):
        CHUNK_SIZE = 16

        self.door_location = door_location
        self.background_location = door_location
        self.frame_location = (door_location[0] - CHUNK_SIZE, door_location[1] - 2 * CHUNK_SIZE)

        self.door_image = pygame.image.load("resources/doors_img/fire_door.png")
        super().__init__()


class Water_Door(Doors):
    def __init__(self, door_location):
        CHUNK_SIZE = 16

        self.door_location = door_location
        self.background_location = door_location
        self.frame_location = (door_location[0] - CHUNK_SIZE, door_location[1] - 2 * CHUNK_SIZE)

        self.door_image = pygame.image.load("resources/doors_img/water_door.png")
        super().__init__()