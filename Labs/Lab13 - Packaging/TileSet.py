__author__ = 'dustinlee'

import json

from pico2d import *

class TileSet:

    def __init__(self):
        self.firstgid = 0

    def load(self, file_name):
        f = open(file_name)
        data = json.load(f)
        f.close()
        self.__dict__.update(data)
        print(self.__dict__)
        self.base_image = load_image(self.image)
        self.tile_images = []
        for i in range(self.tilecount):
            col, row = i % self.columns, i // self.columns
            left = col * self.tilewidth
            bottom = self.base_image.h - (row + 1) * self.tileheight
            image = self.base_image.clip_image(left, bottom, self.tilewidth, self.tileheight)
            self.tile_images.append(image)
        pass


def load_tile_set(file_name):
    tile_set = TileSet()
    tile_set.load(file_name)
    return tile_set

if __name__ =='__main__':
    # fill here
    pass
