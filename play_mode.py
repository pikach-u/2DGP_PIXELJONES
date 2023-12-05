import random
from pico2d import *
import game_framework

import game_world
import menu_mode
import server
from Background import InfiniteBackground as Background
from Player import Player
from obstacle import Obstacle

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
            server.player.handle_event(event)


def init():
    global player

    running = True

    server.background = Background()
    game_world.add_object(server.background, 0)

    server.player = Player()
    game_world.add_object(server.player, 3)

    global obstacles
    obstacles = [Obstacle(random.randint(200,400), random.randint(300,1000)) for _ in range(10)]
    game_world.add_objects(obstacles, 3)

    game_world.add_collision_pair('player:obstacle', server.player, None)
    for obs in obstacles:
        game_world.add_collision_pair('player:obstacle', None, obs)



def finish():
    game_world.clear()
    pass

def update():
    game_world.update()
    game_world.handle_collisions()

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()