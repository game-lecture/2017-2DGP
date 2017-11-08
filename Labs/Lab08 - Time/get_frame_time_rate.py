# get_frame_time_rate : measure frame time and frame rate

import random
import json
from pico2d import *

running = None

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    image = None

    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND = 0, 1, 2, 3

    def handle_left_run(self):
        self.x -= 5
        self.run_frames += 1
        if self.x < 0:
            self.state = self.RIGHT_RUN
            self.x = 0
        if self.run_frames == 100:
            self.state = self.LEFT_STAND
            self.stand_frames = 0

    def handle_left_stand(self):
        self.stand_frames += 1
        if self.stand_frames == 50:
            self.state = self.LEFT_RUN
            self.run_frames = 0

    def handle_right_run(self):
        self.x += 5
        self.run_frames += 1
        if self.x > 800:
            self.state = self.LEFT_RUN
            self.x = 800
        if self.run_frames == 100:
            self.state = self.RIGHT_STAND
            self.stand_frames = 0

    def handle_right_stand(self):
        self.stand_frames += 1
        if self.stand_frames == 50:
            self.state = self.RIGHT_RUN
            self.run_frames = 0


    handle_state = {
                LEFT_RUN: handle_left_run,
                RIGHT_RUN: handle_right_run,
                LEFT_STAND: handle_left_stand,
                RIGHT_STAND: handle_right_stand
    }

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.handle_state[self.state](self)


    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.run_frames = 0
        self.stand_frames = 0
        self.state = self.RIGHT_RUN
        self.name = 'noname'
        if Boy.image == None:
            Boy.image = load_image('animation_sheet.png')

    def draw(self):
        self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False



# team FACTORY

def create_team():
    team_data_text = '                                                   \
        {                                                                \
            "Tiffany" : {"StartState":"LEFT_RUN", "x":100, "y":100},     \
    	    "Yuna"    : {"StartState":"RIGHT_RUN", "x":200, "y":200},    \
    	    "Sunny"   : {"StartState":"LEFT_STAND", "x":300, "y":300},   \
    	    "Yuri"    : {"StartState":"RIGHT_STAND", "x":400, "y":400},  \
    	    "Jessica" : {"StartState":"LEFT_RUN", "x":500, "y":500}      \
        }                                                                \
    '
    player_state_table = {
        "LEFT_RUN" : Boy.LEFT_RUN,
        "RIGHT_RUN" : Boy.RIGHT_RUN,
        "LEFT_STAND" : Boy.LEFT_STAND,
        "RIGHT_STAND" : Boy.RIGHT_STAND
    }

    team_data = json.loads(team_data_text)

    team = []
    for name in team_data:
        player = Boy()
        player.name = name
        player.x = team_data[name]['x']
        player.y = team_data[name]['y']
        player.state = player_state_table[team_data[name]['StartState']]
        team.append(player)

    return team


TARGET_FPS = 60.0
TARGET_FRAME_TIME = 1.0 / TARGET_FPS

def main():

    open_canvas()

    global boy
    global running

    team = create_team()

    grass = Grass()

    running = True

    # fill here

    while running:
        # Game Logic
        handle_events()
        for player in team:
            player.update()

        # Game Rendering
        clear_canvas()
        grass.draw()
        for player in team:
            player.draw()
        update_canvas()

        #fill here


    close_canvas()


if __name__ == '__main__':
    main()