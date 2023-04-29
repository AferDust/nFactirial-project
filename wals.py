import pygame, sys
from pygame.locals import *

class Walls:
    def __init__(self, path):
        self.CHUNK_SIZE = 16
        self.load_map(path)
        self.load_img()
        self.set_water()
        self.set_lava()
        self.set_slize()
        self.set_solid_blocks()

    def load_img(self):
        self._background = pygame.image.load('resources/walls-and-liquid_img/background-wall.png')
        self._board_textures = {
            "100": pygame.image.load('resources/walls-and-liquid_img/wall.png'),
            "2": pygame.image.load('resources/walls-and-liquid_img/lava.png'),
            "3": pygame.image.load('resources/walls-and-liquid_img/water.png'),
            "4": pygame.image.load('resources/walls-and-liquid_img/slize.png')
        }
        for texture in self._board_textures.keys():
            self._board_textures[texture].set_colorkey((255, 0, 255))


    def load_map(self, path):
        self._game_map = []

        with open(path) as f:
            for line in f:
                line = line.strip().split(',')
                self._game_map.append(line)

    def set_solid_blocks(self):
        CHUNKS_SIZE = 16
        self._solid_blocks = []
        for y, row in enumerate(self._game_map):
            for x, tile in enumerate(row):
                if tile not in ['0', '2', '3', '4']:
                    self._solid_blocks.append(
                        pygame.Rect(x * self.CHUNK_SIZE, y * self.CHUNK_SIZE,
                                    self.CHUNK_SIZE, self.CHUNK_SIZE))

    def get_background(self):
        return self._background

    def get_board_textures(self):
          return self._board_textures

    def get_game_map(self):
        return self._game_map

    def get_solid_blocks(self):
        return self._solid_blocks

    def get_lava(self):
        return self._lava_pools

    def get_water(self):
        return self._water_pools

    def get_slize(self):
        return self._goo_pools

    def set_lava(self):
        self._lava_pools = []
        for y, row in enumerate(self._game_map):
            for x, tile in enumerate(row):
                 if tile == "2":
                        self._lava_pools.append(
                        pygame.Rect(x * self.CHUNK_SIZE, y * self.CHUNK_SIZE
                                + self.CHUNK_SIZE / 2, self.CHUNK_SIZE,
                                    self.CHUNK_SIZE / 2))

    def set_water(self):
        self._water_pools = []
        for y, row in enumerate(self._game_map):
            for x, tile in enumerate(row):
                if tile == "3":
                    self._water_pools.append(
                        pygame.Rect(x * self.CHUNK_SIZE, y * self.CHUNK_SIZE
                                + self.CHUNK_SIZE / 2, self.CHUNK_SIZE,
                                    self.CHUNK_SIZE / 2))

    def set_slize(self):
        self._goo_pools = []
        for y, row in enumerate(self._game_map):
            for x, tile in enumerate(row):
                if tile == "4":
                    self._goo_pools.append(
                        pygame.Rect(x * self.CHUNK_SIZE, y * self.CHUNK_SIZE
                                + self.CHUNK_SIZE / 2, self.CHUNK_SIZE,
                                    self.CHUNK_SIZE / 2))