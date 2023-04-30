import pygame, sys
from pygame.locals import *

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((640, 480), pygame.RESIZABLE)
        pygame.display.set_caption('Fireboy and Watergirl')

        CH_SZ = 16
        DISPLAY_SZ = (34 * CH_SZ, 25 * CH_SZ)
        self.display = pygame.Surface(DISPLAY_SZ)

    def display_level_screen(self, level):
        scaled_background_image = pygame.transform.scale(level.screen, (550, 390))
        self.display.blit(scaled_background_image, (0, 0))

        for l in range(3):
            image = level.titles[l + 1]

            title_x = (self.display.get_width() - image.get_width()) / 2
            title_y = 50 * l + 100
            self.display.blit(image, (title_x, title_y))

    def level_select(self, level, cont):
        level_idx = 0

        level_dict = {
            0: "level1",
            1: "level2",
            2: "level3"
        }

        while True:
            self.display_level_screen(level)
            events = pygame.event.get()

            if cont.key_press(K_DOWN, events):
                level_idx += 1

                if level_idx == 3:
                    level_idx = 0

            if cont.key_press(K_UP, events):
                level_idx -= 1

                if level_idx == -1:
                    level_idx = 2

            self.display_level_indicator(level, level_idx)

            if cont.key_press( K_RETURN, events):
                return level_dict[level_idx]

    def display_level_indicator(self, level, level_idx):
            indicator = level.indicator_img

            location_X = (self.display.get_width() - indicator.get_width()) / 2
            location_Y = level_idx * 50 + 95
            indicator_coord = (location_X, location_Y)

            self.display.blit(level.indicator_img, indicator_coord)
            self.new_window()

    def new_window(self):
        new_window_sz, center_coord = self.get_scale()
        new_display = pygame.transform.scale(self.display, new_window_sz)
        self.screen.blit(new_display, center_coord)
        pygame.display.update()

    def get_scale(self):
        window_sz = self.screen.get_size()

        if window_sz[0] / window_sz[1] >= 1.5:
            display_sz = (int(1.5 * window_sz[1]), window_sz[1])
        else:
            display_sz = (window_sz[0], int(0.75 * window_sz[0]))

        coords = ((window_sz[0] - display_sz[0]) / 2,
                 (window_sz[1] - display_sz[1]) / 2)

        return display_sz, coords

    def display_walls(self, walls):
        board_tet = walls.get_board_textures()

        for y, row in enumerate(walls.get_game_map()):
            for x, t in enumerate(row):
                if t != "0":
                    self.display.blit(board_tet[f"{t}"], (x * 16, y * 16))


    def display_level_back(self, walls):
        self.display.blit(walls.get_background(), (0, 0))

    def display_exit(self, doors):
        for door in doors:
            self.display.blit(door.door_background, door.background_location)
            self.display.blit(door.door_image, door.door_location)
            self.display.blit(door.frame_image, door.frame_location)

    def display_landscape(self, landscape):
        for l in landscape:
            self.display.blit(l.gate_image, l.gate_location)

            for location in l.plate_locations:
                self.display.blit(l.plate_image, location)

    def display_player(self, players):
        for player in players:
            if player.moving_right:
                player_img = player.side_image
            elif player.moving_left:
                player_img = pygame.transform.flip(player.side_image, True, False)
            else:
                player_img = player.image

            player_img.set_colorkey((245, 0, 245))
            self.display.blit(player_img, (player.rect.x, player.rect.y))


    def player_moving(self, walls, landscape, players):
        for player in players:
            player.movement_calculation()
            movement = player.get_movement()

            collide_blocks = walls.get_solid_blocks()
            for l in landscape:
                collide_blocks += l.get_solid_blocks()

            collision_types = {
                'top': False,
                'bottom': False,
                'right': False,
                'left': False
            }

            player.rect.x += movement[0]
            hit_list = self.collision_test(player.rect, collide_blocks)
            for tile in hit_list:
                if movement[0] > 0:
                    player.rect.right = tile.left
                    collision_types['right'] = True
                elif movement[0] < 0:
                    player.rect.left = tile.right
                    collision_types['left'] = True

            player.rect.y += movement[1]
            hit_list = self.collision_test(player.rect, collide_blocks)
            for tile in hit_list:
                if movement[1] > 0:
                    player.rect.bottom = tile.top
                    collision_types['bottom'] = True
                elif movement[1] < 0:
                    player.rect.top = tile.bottom
                    collision_types['top'] = True

            if collision_types['bottom']:
                player.y_velocity = 0
                player.air_timer = 0
            else:
                player.air_timer += 1

            if collision_types['top']:
                player.y_velocity = 0



    def player_death(self, walls, players):
        for player in players:
            if player.get_type() == "water":
                is_killed = self.collision_test(
                    player.rect, walls.get_lava())

            if player.get_type() == "fire":
                is_killed = self.collision_test(
                    player.rect, walls.get_water())

            is_killed += self.collision_test(player.rect, walls.get_slize())

            if is_killed:
                player.player_rip()


    def is_gate_press(self, landscape, players):
        for l in landscape:
            plate_collisions = []
            for player in players:
                plates = l.get_plates()
                plate_collisions += self.collision_test(player.rect, plates)
            if plate_collisions:
                l.plate_is_pressed = True
            else:
                l.plate_is_pressed = False

            l.open_gate()

    def is_door_open(self, door, player):
        door_collision = self.collision_test(player.rect, [door.get_door()])
        if door_collision:
            door.player_at_door = True
        else:
            door.player_at_door = False

        door.raise_door()


    @staticmethod
    def collision_test(rect, tiles):
        hit_list = []
        for tile in tiles:
            if rect.colliderect(tile):
                hit_list.append(tile)
        return hit_list

    @staticmethod
    def level_is_done(doors):
        is_win = False
        for door in doors:
            if door.is_door_open():
                is_win = True
        return is_win