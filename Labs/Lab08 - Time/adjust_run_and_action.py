# adjust_run_and_action.py : regulate run speed and action speed as well

import random
import json
from pico2d import *

running = None

class Field:
    def __init__(self):
        self.image = load_image('background30M.bmp')

    def draw(self):
        self.image.draw(480, 136)


class Boy:

    # fill here

    image = None

    LEFT_RUN, RIGHT_RUN = 0, 1

    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = random.randint(0, 7)
        self.total_frames = 0.0
        self.dir = 1
        self.state = self.RIGHT_RUN
        if Boy.image == None:
            Boy.image = load_image('animation_sheet.png')
        # fill here


    def update(self, frame_time):
        # fill here
        pass


    def draw(self):
        # fill here
        self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)


def handle_events(frame_time):
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False



current_time = 0.0


def get_frame_time():

    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time


def main():

    open_canvas(960, 272)

    global running
    global current_time


    hero = Boy()
    field = Field()

    running = True
    current_time = get_time()

    while running:

        # Game Logic
        # fill here


        # Game Rendering
        clear_canvas()
        field.draw()
        hero.draw()
        update_canvas()


    close_canvas()


if __name__ == '__main__':
    main()