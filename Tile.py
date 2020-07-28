class Map:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
from collections import namedtuple
Tile = namedtuple("Tile", ("rectangle", "x", "y", "width", "height", "highlighted", "food"))