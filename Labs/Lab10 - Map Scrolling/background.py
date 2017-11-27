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
        self.image.clip_draw_to_origin(self.window_left, self.window_bottom, self.canvas_width, self.canvas_height, 0, 0)






    def update(self, frame_time):
        # fill here
        self.window_left = clamp(0, int(self.center_object.x) - self.canvas_width//2, self.w - self.canvas_width)
        self.window_bottom = clamp(0, int(self.center_object.y) - self.canvas_height//2, self.h - self.canvas_height)


        # 3
        self.left3 = (int(self.center_object.x) - self.canvas_width // 2) % self.w
        self.bottom3 = (int(self.center_object.x) - self.canvas_height // 2) % self.h
        self.width3 = clamp(0, self.w - self.left3, self.w)
        self.height3 = clamp(0, self.h - self.bottom3, self.h)

        self.left1 = 0
        self.bottom1 = 0
        self.width1 = clamp(0, )





        self.sx = self.window_left % self.w
        self.sy = self.window_bottom % self.h
        self.rect3 = int(self.window_left) % self.w, int(self.window_bottom) % self.h, clamp(0, )




    def handle_event(self, event):
        pass




