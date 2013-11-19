import random
from helpers.colors import *
from helpers.constants import Constants


class Creature(object):
    def __init__(self):
        self.color = WHITE
        self.character = ' '
        self.x = 0
        self.y = 0

    def draw(self, window):
        window.write(
            self.character,
            fgcolor=self.color,
            bgcolor=Constants.BG_COLOR,
            x=self.x,
            y=self.y,
        )
