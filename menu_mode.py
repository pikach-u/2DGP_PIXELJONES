import random
from pico2d import *
import game_framework

import game_world
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
            if event.x >= 245 and event.x <= 475 and event.y >=370 and event.y <= 435:
                game_framework.change_mode(play_mode)
        elif event.type == SDL_MOUSEMOTION:
            print(event.x) #245~475
            print(event.y) #370~435


def init():
    global menuBg, stageButton1, stageButton2, stageButton3
    global selectImg,coinImg, playButton, ClickedplayButton, clearButton, boxImg, homeButton
    menuBg = load_image('res/background/bg_world.png')
    stageButton1 = load_image('res/gui/menu/lv_icon_01.png')
    stageButton2 = load_image('res/gui/menu/lv_icon_02.png')
    stageButton3 = load_image('res/gui/menu/lv_icon_03.png')
    selectImg = load_image('res/gui/menu/text_select.png')
    boxImg = load_image('res/gui/menu/box_select.png')
    homeButton = load_image('res/gui/menu/btn_home.png')
    playButton = load_image('res/gui/menu/btn_play.png')
    ClickedplayButton = load_image('res/gui/menu/btn_play_clicked.png')
    coinImg = load_image('res/gui/menu/icon_coin.png')

def finish():
    pass

def update():
    pass

def draw():
    clear_canvas()
    menuBg.draw_to_origin(0,0,600,900)
    boxImg.draw(300, 500)
    boxImg.draw(300, 350)
    boxImg.draw(300, 200)
    homeButton.draw_to_origin(100, 700, 60,60)
    coinImg.draw_to_origin(440,700,60,60)
    selectImg.draw(300,600,137,29)
    stageButton1.draw_to_origin(110,445,113,107)
    stageButton2.draw_to_origin(110, 295, 113, 107)
    stageButton3.draw_to_origin(110, 145, 113, 107)
    # 다음 스테이지 비활성화
    boxImg.draw(300, 350)
    boxImg.draw(300, 200)
    playButton.draw(362, 495, 230, 69)

    update_canvas()