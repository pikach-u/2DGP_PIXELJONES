from pico2d import load_image
from sdl2 import SDL_KEYDOWN, SDLK_RIGHT, SDL_KEYUP, SDLK_LEFT


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


class Player:
    def __init__(self):
        self.x, self.y = 300, 300
        self.image = load_image('res/Player/c_m_01_01.png')
        self.frame = 0
        self.action = 1
        self.state_machine = StateMachine(self)
        self.state_machine.start()

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()


class Run:
    @staticmethod
    def enter(player, e):
        if right_down(e) or left_up(e):
            player.dir, player.action = 1,1
        elif left_down(e) or right_up(e):
            player.dir, player.action = -1, 1

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + 1) % 6
        player.x += player.dir * 5

        if player.x >= 500:
            player.x = 500
        elif player.x <= 100:
            player.x = 100

        pass

    @staticmethod
    def draw(player):
        player.image.clip_draw(player.frame * 154, player.action * 670, player.x, player.y, 100, 100)


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
