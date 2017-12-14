__author__ = 'dustinlee'

import json

from pico2d import *


from TileSet import load_tile_set


class TileMap:


    def load(self, name):
        f = open(name)
        info = json.load(f)
        f.close()
        self.__dict__.update(info)
        self.tile_set = load_tile_set(self.tilesets[0]['source'])
        self.firstgid = self.tilesets[0]['firstgid']
        self.data = self.layers[0]['data']
        new_data = []
        for row in reversed(range(self.height)):
            new_data.append(self.data[row * self.width: row * self.width + self.width])
        self.data = new_data
        pass



    def clip_draw_to_origin(self, l, b, w, h, dx, dy):
        tl = l // self.tilewidth
        tb = b // self.tileheight
        tw = (l + w) // self.tilewidth - tl + 1
        th = (b + h) // self.tileheight - tb + 1
        lo = l % self.tilewidth
        bo = b % self.tileheight
        for x in range(tl, min(tl + tw, self.width)):
            for y in range(tb, min(tb + th, self.height)):
                self.tile_set.tile_images[self.data[y][x] - self.firstgid].draw_to_origin((x - tl) * self.tilewidth - lo, (y - tb) * self.tileheight - bo)
        pass


def load_tile_map(name):
    tile_map = TileMap()
    tile_map.load(name)

    return tile_map



