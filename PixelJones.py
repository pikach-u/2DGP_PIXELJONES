from pico2d import *

from Background import Background
from player import Player

def reset_world():
    global world, running, world

    running = True

    world = []
    bg = Background()
    world.append(bg)
    player = Player()
    world.append(player)


def handle_events():
    global running, dir

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            player.handle_event(event)


def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()

def update_world():
    for o in world:
        o.update()
    pass

open_canvas()
reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.1)

close_canvas()