import random
import game_world
import game_framework

from pico2d import *


class Obstacle:

    def __init__(self):
        self.x, self,y = random.randint(230,370), random.randint(300, 800)
        self.image = None
