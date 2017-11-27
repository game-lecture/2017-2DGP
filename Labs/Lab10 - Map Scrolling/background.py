import random

from pico2d import *


class FixedBackground:

    def __init__(self):
        self.image = load_image('futsal_court.png')
        self.speed = 0
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h

    def set_center_object(self, boy):
        # fill here
        self.center_object = boy


    def draw(self):
        # fill here
        self.image.clip_draw_to_origin(self.window_left, self.window_bottom, self.canvas_width, self.canvas_height, 0, 0)


    def update(self, frame_time):
        # fill here
        self.window_left = clamp(0, int(self.center_object.x) - self.canvas_width//2, self.w - self.canvas_width)
        self.window_bottom = clamp(0, int(self.center_object.y) - self.canvas_height//2, self.h - self.canvas_height)

    def handle_event(self, event):
        pass


class InfiniteBackground:


    def __init__(self):
        self.image = load_image('futsal_court.png')
        self.speed = 0
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h

    def set_center_object(self, boy):
        # fill here
        self.center_object = boy


    def draw(self):
        # fill here
        self.image.clip_draw_to_origin(self.quadrant3_left, self.quadrant3_bottom, self.quadrant3_width, self.quadrant3_height, 0, 0)
        self.image.clip_draw_to_origin(self.quadrant2_left, self.quadrant2_bottom, self.quadrant2_width, self.quadrant2_height, 0, self.quadrant3_height)
        self.image.clip_draw_to_origin(self.quadrant4_left, self.quadrant4_bottom, self.quadrant4_width, self.quadrant4_height, self.quadrant3_width, 0)
        self.image.clip_draw_to_origin(self.quadrant1_left, self.quadrant1_bottom, self.quadrant1_width, self.quadrant1_height, self.quadrant3_width, self.quadrant3_height)


    def update(self, frame_time):

        # quadrant 3
        self.quadrant3_left = (int(self.center_object.x) - self.canvas_width // 2) % self.w
        self.quadrant3_bottom = (int(self.center_object.y) - self.canvas_height // 2) % self.h
        self.quadrant3_width = clamp(0, self.w - self.quadrant3_left, self.w)
        self.quadrant3_height = clamp(0, self.h - self.quadrant3_bottom, self.h)


        # quadrant 2
        self.quadrant2_left = self.quadrant3_left
        self.quadrant2_bottom = 0
        self.quadrant2_width = self.quadrant3_width
        self.quadrant2_height = self.canvas_height - self.quadrant3_height


        # quadrand 4
        self.quadrant4_left = 0
        self.quadrant4_bottom = self.quadrant3_bottom
        self.quadrant4_width = self.canvas_width - self.quadrant3_width
        self.quadrant4_height = self.quadrant3_height


        # quadrand 1
        self.quadrant1_left = 0
        self.quadrant1_bottom = 0
        self.quadrant1_width = self.quadrant4_width
        self.quadrant1_height = self.quadrant2_height


    def handle_event(self, event):
        pass




