import random
import game_world
import game_framework
import server

from pico2d import *


class Coin:
    coinImg = None

    def __init__(self, x = 400, y = 400):
        # self.x, self,y = random.randint(230,370), random.randint(300, 800)
        if Coin.coinImg == None:
            self.coinImg = load_image('res/item/coin_sheet.png')
        # self.font = load_font('ENCR10B.TTF', 16)
        self.x = x if x else random.randint(240, 360)
        self.y = y if y else random.randint(400, 1000)
        self.coin_count = 0
        self.frame = 0

    def draw(self):
        global sx, sy
        sx = self.x - server.background.window_left
        sy = self.y - server.background.window_bottom
        self.coinImg.clip_draw(int(self.frame) * 100, 10, 100, 100, sx, sy, 40, 40)
        # self.font.draw(self.x - 10, self.y + 50, f'{self.coin_count:02d}', (255, 255, 0))
        draw_rectangle(*self.get_p())
        pass

    def update(self):
        # self.x += game_framework.frame_time
        if self.x < 240.0 or self.x > 360.0:
            game_world.remove_object(self)
        self.frame = (self.frame + game_framework.frame_time * 5) % 3
        pass

    def get_p(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self,  group, other):
        if group == 'player:coin':
            game_world.remove_object(self)
            # print('Get Coin')
