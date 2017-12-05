__author__ = 'dustinlee'

import json

from pico2d import *


from TileSet import load_tile_set


class TileMap:


    def load(self, name):
        # fill here
        pass



    def clip_draw_to_origin(self, l, b, w, h, dx, dy):
        # fill here
        pass


def load_tile_map(name):
    tile_map = TileMap()
    tile_map.load(name)

    return tile_map



