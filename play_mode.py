import random
from pico2d import *
import game_framework

import game_world
import menu_mode
from Background import Background
from Player import Player

def handle_events():

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(menu_mode)
        elif event.type == SDL_MOUSEMOTION:
            print(event.x)  # road: 237~364
            print(event.y)
        else:
            player.handle_event(event)


def init():
    global bg
    global player

    running = True

    bg = Background()
    game_world.add_object(bg, 0)

    player = Player()
    game_world.add_object(player, 3)



def finish():
    game_world.clear()
    pass

def update():
    game_world.update()

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()