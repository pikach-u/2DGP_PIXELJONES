from pico2d import *



def init():
    global world, character, running, frame, dir, x
    open_canvas(600, 800)
    world = load_image('res/background/bg_world.png')
    character = load_image('res/character/c_m_01_01.png')
    x = 300
    dir = 0
    running = True
    frame = 0


def handle_events():
    global running, dir

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_a:
            dir -= 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_d:
            dir += 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_a:
                dir += 1
            elif event.key == SDLK_d:
                dir -= 1

def drawing():
    global frame
    clear_canvas()
    world.draw(300,400)
    character.clip_draw(frame * 154, 670, 170, 170, x, 300, 100, 100)
    frame = (frame + 1) % 6


init()

while running:
    handle_events()
    update_canvas()
    drawing()
    x += dir * 10
    delay(0.1)

close_canvas()