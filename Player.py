from pico2d import load_image
from sdl2 import SDL_KEYDOWN, SDLK_RIGHT, SDL_KEYUP, SDLK_LEFT

import game_framework


def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT


def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT


def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT


def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT


def time_out(e):
    return e[0] == 'TIME_OUT' and e[1] == 5.0


#Player Run Speed
PIXEL_PER_METER = (10.0 / 0.3) #10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8



class Run:
    @staticmethod
    def enter(player, e):
        print('enter')
        if right_down(e) or left_up(e): # 오른쪽으로 이동
            player.dir, player.action = 1,1
        elif left_down(e) or right_up(e): # 왼쪽으로 이동
            player.dir, player.action = -1, 1

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
        #player.frame = (player.frame + 1) % 6
        player.x += player.dir * RUN_SPEED_PPS * game_framework.frame_time
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6

        if player.x >= 500:
            player.x = 500
        elif player.x <= 100:
            player.x = 100

        pass

    @staticmethod
    def draw(player):
        #player.image.clip_draw(player.frame * 154, 670, player.x, player.y, 100, 100)
        player.image.clip_draw(int(player.frame) * 154, player.action * 670, 150, 170, player.x, 100)


class StateMachine:
    def __init__(self, player):
        self.player = player
        self.current_state = Run
        self.stateTable = {
            Run: {}
        }

    def start(self):
        self.current_state.enter(self.player, ('START', 0))

    def update(self):
        self.current_state.do(self.player)

    def handle_event(self, e):
        for check_event, next_state in self.stateTable[self.current_state].items():
            if check_event(e):
                self.current_state.exit(self.player, e)
                self.current_state = next_state
                self.current_state.enter(self.player, e)
                return True

        return False

    def draw(self):
        self.current_state.draw(self.player)


class Player:
    def __init__(self):
        self.x, self.y = 300, 300
        self.frame = 0
        self.dir = 0
        self.action = 1
        self.image = load_image('res/character/c_m_01_01.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()
