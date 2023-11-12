import random
from pico2d import *
import game_framework

import menu_mode
import play_mode
from Background import Background
from Player import Player

def handle_events():

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            game_framework.change_mode(menu_mode)
            #game_framework.change_mode(play_mode)




def init():
    global titleBg, titleTop, titleButton,titleCh, title2
    titleBg = load_image('res/title/title_bg.png')
    titleTop = load_image('res/title/title.png')
    # titleButton = load_image()
    titleCh = load_image('res/title/title_ch.png')



def finish():
    pass

def update():
    pass

def draw():
    clear_canvas()

    titleBg.draw_to_origin(0,0,600,900)
    titleTop.draw_to_origin(0, 0, 600, 900)
    titleCh.draw_to_origin(0, 0, 600, 900)
    update_canvas()