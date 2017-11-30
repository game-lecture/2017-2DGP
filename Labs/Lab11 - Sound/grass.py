import random

from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
        # fill here


    def draw(self):
        self.image.draw(400, 30)

    def draw_bb(self):
        #draw_rectangle(*self.get_bb())
        pass

    def get_bb(self):
        return 0,0,799,50

    def __del__(self):
        del self.image
        del self.bgm

