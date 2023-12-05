import math

from pico2d import load_image, get_time, clamp, get_canvas_width, get_canvas_height, draw_rectangle
# from sdl2 import SDL_KEYDOWN, SDLK_RIGHT, SDL_KEYUP, SDLK_LEFT, SDLK_SPACE
from sdl2 import *

import game_framework
import server


def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT


def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT


def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT


def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT


def time_out(e):
    return e[0] == 'TIME_OUT'


def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE


def jump_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_c


def jump_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_c


# Player Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class Idle:
    @staticmethod
    def enter(player, e):
        player.action = 4
        player.dir = 0
        player.speed = 0
        player.wait_time = get_time()
        pass

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
        if (SDL_KEYDOWN):
            player.state_machine.handle_event(('RUN', 0))
        if get_time() - player.wait_time >= 2:
            player.action = 3
            player.speed = RUN_SPEED_PPS
            player.dir = math.pi / 2.0
            player.state_machine.handle_event(('RUN', 0))
        pass

    @staticmethod
    def draw(player):
        pass

    # @staticmethod
    # def draw(player):
    #     player.image.clip_draw(int(player.frame) * 150, 720, 150, 160, player.x, get_canvas_height()//2, 80, 80)
    #     # player.image.clip_draw(int(player.frame) * 154, player.action * 178, 154, 178, player.x, 100, 80, 80)


class RunLeft:
    @staticmethod
    def enter(player, e):
        player.action = 3
        player.speed = RUN_SPEED_PPS
        player.dir = math.pi

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
        pass

    @staticmethod
    def draw(player):
        pass

    # @staticmethod
    # def draw(player):
    #     # player.image.clip_draw(player.frame * 154, player.action * 670, player.x, player.y, 100, 100)
    #     player.image.clip_draw(int(player.frame) * 150, player.action * 540, 150, 160, player.x, player.y, 80, 80)


class RunRight:
    @staticmethod
    def enter(player, e):
        player.action = 3
        player.speed = RUN_SPEED_PPS
        player.dir = 0

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
        pass

    @staticmethod
    def draw(player):
        pass

    @staticmethod
    def draw(player):
        pass

    # @staticmethod
    # def draw(player):
    #     # player.image.clip_draw(player.frame * 154, player.action * 670, player.x, player.y, 100, 100)
    #     player.image.clip_draw(int(player.frame) * 150, player.action * 540, 150, 160, player.x, player.y, 80, 80)

class RunUp:
    @staticmethod
    def enter(player, e):
        player.action = 3
        player.speed = RUN_SPEED_PPS
        player.dir = math.pi / 2.0

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
        pass

    @staticmethod
    def draw(player):
        pass

class SideRun:
    @staticmethod
    def enter(player, e):
        player.image = load_image('res/character/c_m_01_02_1.png')
        print('siderun')

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
        # player.x += player.dir * RUN_SPEED_PPS * game_framework.frame_time
        # player.y += RUN_SPEED_PPS * game_framework.frame_time
        player.x += RUN_SPEED_PPS * game_framework.frame_time
        # player.y += player.dir * RUN_SPEED_PPS * game_framework.frame_time
        # player.x = clamp(247, player.x, 357)
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6

    @staticmethod
    def draw(player):
        # player.image.clip_draw(int(player.frame) * 154, player.action * 155, 154, 178, player.x, 100, 80, 80)
        player.image.clip_draw(int(player.frame) * 150, player.action * 540, 143, 160, player.x, 200, 80, 80)


class Jump:

    @staticmethod
    def enter(player, e):
        player.action = 2
        player.frame = 1
        print('Jump')
        player.jump_time = get_time()

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
        if get_time() - player.jump_time > 1.0:
            player.action = 3
            player.state_machine.current_state = RunUp
        pass


class StateMachine:
    def __init__(self, player):
        self.player = player
        self.current_state = Idle
        self.stateTable = {
            Idle: {right_down: RunRight, left_down: RunLeft, left_up: RunRight, right_up: RunLeft, time_out: RunUp},
            RunLeft: {left_up: RunUp, right_down: RunUp, jump_down: Jump, jump_up: RunUp},
            RunRight: {right_up: RunUp, left_down: RunUp, jump_down: Jump, jump_up: RunUp},
            RunUp: {right_down: RunRight, left_down: RunLeft, left_up: RunRight, right_up: RunLeft, jump_down: Jump, jump_up: RunUp},
            # SideRun: {right_down: SideRun, left_down: SideRun, right_up: SideRun, left_up: SideRun, space_down: Run},
            Jump: {jump_up: RunUp, time_out: RunUp}
        }

    def start(self):
        self.current_state.enter(self.player, ('NONE', 0))

    def update(self):
        self.current_state.do(self.player)
        self.player.frame = (self.player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        self.player.x += math.cos(self.player.dir) * self.player.speed * game_framework.frame_time
        self.player.y += math.sin(self.player.dir) * self.player.speed * game_framework.frame_time


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
        self.frame = 0
        self.dir = 0
        self.action = 1
        self.image = load_image('res/character/c_m_01_01_2.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()
        self.x, self.y = server.background.w // 2, server.background.h // 2

    def update(self):
        self.state_machine.update()
        self.x = clamp(240.0, self.x, 360.0)
        # self.y = clamp(50.0, self.y, server.background.h - 50.0)

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        global sx, sy
        sx, sy = get_canvas_width()//2 , get_canvas_height()//2
        # self.state_machine.draw()
        # self.image.clip_draw(int(self.frame) * 150, self.action * 540, 150, 160, sx, sy, 80, 80)

        if self.state_machine.current_state == Jump:
            self.image.clip_draw(150, self.action * 177, 145, 175, sx, sy, 80, 80)
        else:
            self.image.clip_draw(int(self.frame) * 150, self.action * 177, 145, 175, sx, sy, 80, 80)


    def get_p(self):
        return self.x - 20, self.y - 40, self.x + 20, self.y

    def handle_collision(self, group, other):
        if group == 'player:obstacle':
            print('방해물과 충돌!')
        elif group == 'player:fire':
            print('damage')
        elif group == 'player:coin':
            print('Get Coin')
