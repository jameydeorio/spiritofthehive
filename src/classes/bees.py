from classes.base import Creature
from helpers.colors import *
from helpers.constants import Constants


class Queen(Creature):
    def __init__(self):
        super(Queen, self).__init__()

        self.color = QUEEN_YELLOW
        self.character = 'b'
        self.x = Constants.SCREEN_WIDTH / 2
        self.y = Constants.SCREEN_HEIGHT / 2