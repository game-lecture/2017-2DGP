import sys
sys.path.append('../LabsAll/Labs')

import random
from pico2d import *

running = None

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    image = None

    def __init__(self):
        #fill here
        pass

    def update(self):
        # fill here
        pass

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def main():

    open_canvas()
    boy = Boy()
    grass = Grass()

    global running
    running = True
    while running:
        handle_events()

        boy.update()

        clear_canvas()
        grass.draw()
        boy.draw()
        update_canvas()

        delay(0.05)

    close_canvas()


if __name__ == '__main__':
    main()