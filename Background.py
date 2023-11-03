from pico2d import load_image

class Background:
    def __init__(self):
        self.image = load_image('res/background/bg_world.png')

    def draw(self):
        self.image.draw_to_origin(0,0,600,900)

    def update(self):
        pass
