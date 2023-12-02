import random
import game_world
import game_framework
import server

from pico2d import *


class Obstacle:
    obs1 = None

    def __init__(self, x = 400, y = 400):
        # self.x, self,y = random.randint(230,370), random.randint(300, 800)
        if Obstacle.obs1 == None:
            self.obs1 = load_image('res/obstacle/obstacle_01_01.png')
            self.obs2 = load_image('res/obstacle/obstacle_01_02.png')
        # self.obs3 = load_image('res/obstacle/obstacle_bonus.png')
        # self.obs4 = load_image('res/obstacle/obstacle_common.png')
        self.x = x
        self.y = y

    def draw(self):
        sx = self.x - server.background.window_left
        sy = self.y - server.background.window_bottom
        self.obs1.draw(sx, sy)
        pass

    def update(self):

        pass

    def get_p(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self,  group, other):
        pass
