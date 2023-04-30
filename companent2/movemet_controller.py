import sys, pygame
from pygame.locals import *

class Movement_Controller:
    def __intit__(self):
        pass

    def controller_for_player(self,  player, events):
        for event in events:
            if event.type == KEYDOWN:
                    if event.key == self._controls["right"]:
                        player.moving_right = True
                    elif event.key == self._controls["left"]:
                        player.moving_left = True
                    elif event.key == self._controls["up"]:
                        if player.air_timer < 6:
                            player.jumping = True

            elif event.type == KEYUP:
                if event.key == self._controls["right"]:
                    player.moving_right = False
                elif event.key == self._controls["left"]:
                    player.moving_left = False
                elif event.key == self._controls["up"]:
                    player.jumping = False


    @staticmethod
    def key_press(key, events):
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == key:
                    return True
        return False


class Main_Controller(Movement_Controller):
    pass

class Left_Player_Controller(Movement_Controller):
    def __init__(self):
        self._controls = {
            "left": K_a,
            "up": K_w,
            "right": K_d,
        }
        super().__init__()


class Right_Player_Controller(Movement_Controller):
    def __init__(self):
        self._controls = {
            "left": K_LEFT,
            "up": K_UP,
            "right": K_RIGHT,
        }
        super().__init__()
