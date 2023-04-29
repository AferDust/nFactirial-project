import pygame, sys
from pygame.locals import *

class Sprite:
    def __init__(self, location):
        _location = location
        self.rect = pygame.Rect(
            location[0], location[1], self.image.get_width(),
            self.image.get_height())

        self.moving_left = False
        self.moving_right = False

        self.y_velocity = 0
        self.air_timer = 0
        self.jumping = False

        self._alive = True

    def movement_calculation(self):
        JUMP_SPEED = -4
        GRAVITY = 0.3
        LATERAL_SPEED = 4
        TERMINAL_VELOCITY = 3

        self._movement = [0, 0]

        if self.moving_left:
            self._movement[0] -= LATERAL_SPEED
        if self.moving_right:
            self._movement[0] += LATERAL_SPEED

        if self.jumping:
            self.y_velocity = JUMP_SPEED
            self.jumping = False
        self._movement[1] += self.y_velocity
        self.y_velocity += GRAVITY

        if self.y_velocity > TERMINAL_VELOCITY:
            self.y_velocity = TERMINAL_VELOCITY

    def get_movement(self):
        return self._movement

    def get_type(self):
        return self._type

    def player_rip(self):
        self._alive = False

    def is_dead(self):
        return self._alive is False

class Water_Girl:
    def __init__(self, location):
        self.image = pygame.image.load('resources/sprites_img/watergirl.png')
        self.side_image = pygame.image.load('resources/sprites_img/watergirl-side.png')
        self._type = "water"
        super().__init__(location)

class Fire_Boy:
    def __init__(self, location):
        self.image = pygame.image.load('resources/sprites_img/fireboy.png.png')
        self.side_image = pygame.image.load('resources/sprites_img/fireboy-side.png')
        self._type = "fire"
        super().__init__(location)