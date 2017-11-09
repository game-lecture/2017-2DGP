from pico2d import *

import game_framework


from boy import Boy # import Boy class from boy.py
from ball import Ball, BigBall
from grass import Grass



name = "collision"

boy = None
balls = None
big_balls = None
grass = None

def create_world():
    global boy, grass, balls, big_balls

    pass


def destroy_world():
    global boy, grass, balls, big_balls

    del(boy)
    del(balls)
    del(grass)
    del(big_balls)



def enter():
    open_canvas()
    game_framework.reset_time()
    create_world()


def exit():
    destroy_world()
    close_canvas()


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            else:
                boy.handle_event(event)



def collide(a, b):
    # fill here
    pass


def update(frame_time):
    boy.update(frame_time)
    for ball in balls:
        ball.update(frame_time)

    # fill here
    pass



def draw(frame_time):
    clear_canvas()
    grass.draw()
    boy.draw()
    for ball in balls:
        ball.draw()

    # fill here
    pass

    update_canvas()






