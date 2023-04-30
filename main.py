import pygame, sys
from pygame.locals import *

from game import Game
from companent1.walls import Walls
from companent2.sprite import Fire_Boy, Water_Girl
from companent2.movemet_controller import Main_Controller, Left_Player_Controller, Right_Player_Controller
from companent1.landscape import Landscape
from companent1.exit import Fire_Door, Water_Door
from companent2.level import Level_Selected


def main():
    pygame.init()
    cont = Main_Controller()
    game = Game()
    display_main_page(game, cont)

def display_main_page(game, cont):
    intro = pygame.image.load('resources/screen-pages/main_page.png')
    game.display.blit(intro, (-50, 0))
    while True:
        game.new_window()
        if cont.key_press(K_RETURN, pygame.event.get()):
            display_level_page(game, cont)


def dispaly_win_page(game, cont):
    win_page = pygame.image.load('resources/screen-pages/win_screen.png')
    scaled_background_image = pygame.transform.scale(win_page, (550, 400))
    win_page.set_colorkey((255, 0, 255))
    game.display.blit(scaled_background_image, (0, 0))

    while True:
        game.new_window()
        if cont.key_press(K_RETURN, pygame.event.get()):
            display_level_page(game, cont)

def display_lose_page(game, controller, level):
    lose_page = pygame.image.load('resources/screen-pages/lose_screen.png')
    lose_page.set_colorkey((255, 0, 255))
    scaled_background_image = pygame.transform.scale(lose_page, (550, 400))
    game.display.blit(scaled_background_image, (0, 0))
    while True:
        game.new_window()
        events = pygame.event.get()
        if controller.key_press(K_RETURN, events):
            run_game(game, controller, level)
        if controller.key_press(K_ESCAPE, events):
            display_level_page(game, controller)


def display_level_page(game, cont):
    level_select = Level_Selected()
    level = game.level_select(level_select, cont)
    run_game(game, cont, level)



def run_game(game, cont, level="level1"):
    if level == "level1":
        walls = Walls('resources/level_1')
        gate_location = (285, 128)
        plate_locations = [(190, 168), (390, 168)]
        land = Landscape(gate_location, plate_locations)
        lands = [land]

        fire_door_location = (64, 48)
        fire_door = Fire_Door(fire_door_location)
        water_door_location = (128, 48)
        water_door = Water_Door(water_door_location)
        doors = [fire_door, water_door]

        fire_boy_location = (16, 336)
        fire_boy = Fire_Boy(fire_boy_location)
        water_girl_location = (35, 336)
        water_girl = Water_Girl(water_girl_location)

    if level == "level2":
        walls = Walls('resources/level_2')
        lands = []

        fire_door_location = (5 * 16, 4 * 16)
        fire_door = Fire_Door(fire_door_location)
        water_door_location = (28 * 16, 4 * 16)
        water_door = Water_Door(water_door_location)
        doors = [fire_door, water_door]

        fire_boy_location = (28 * 16, 4 * 16)
        fire_boy = Fire_Boy(fire_boy_location)
        water_girl_location = (5 * 16, 4 * 16)
        water_girl = Water_Girl(water_girl_location)


    left_controller = Left_Player_Controller()
    right_controller = Right_Player_Controller()

    clock = pygame.time.Clock()

    while True:
        clock.tick(60)
        events = pygame.event.get()

        game.display_level_back(walls)
        game.display_walls(walls)
        if lands:
            game.display_landscape(lands)
        game.display_exit(doors)

        game.display_player([fire_boy, water_girl])

        right_controller.controller_for_player(fire_boy, events)
        left_controller.controller_for_player(water_girl, events)

        game.player_moving(walls, lands, [fire_boy, water_girl])

        game.player_death(walls, [fire_boy, water_girl])
        game.is_gate_press(lands, [fire_boy, water_girl])

        game.is_door_open(fire_door, fire_boy)
        game.is_door_open(water_door, water_girl)

        game.new_window()

        if cont.key_press(K_ESCAPE, events):
            display_level_page(game, cont)

        if water_girl.is_dead() or fire_boy.is_dead():
            display_lose_page(game, cont, level)

        if game.level_is_done(doors):
            dispaly_win_page(game, cont)

        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


if __name__ == '__main__':
    main()