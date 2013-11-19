import random
from classes.base import Creature
from helpers.colors import *
from helpers.constants import Constants


class Bee(Creature):
    def move(self):
        direction = random.choice(((0, -1), (0, 1), (-1, 0), (1, 0)))
        newx = self.x + direction[0]
        newy = self.y + direction[1]
        if (0 <= newx < Constants.SCREEN_WIDTH) and (0 <= newy < Constants.SCREEN_HEIGHT - 1):
            # If the move is within the screen boundaries...
            self.x = newx
            self.y = newy


class Queen(Bee):
    def __init__(self):
        super(Queen, self).__init__()

        self.color = QUEEN_WHITE
        self.character = 'Q'
        self.x = Constants.SCREEN_WIDTH / 2
        self.y = Constants.SCREEN_HEIGHT / 2

    def lay(self):
        """
        Lay eggs in cell. A healthy queen will lay 2,000 eggs per day.
        """
        pass


class Worker(Bee):
    def __init__(self):
        super(Worker, self).__init__()

        self.color = WORKER_YELLOW
        self.character = 'w'
        self.x = random.randrange(Constants.SCREEN_WIDTH)
        self.y = random.randrange(Constants.SCREEN_HEIGHT - 1)


class Drone(Bee):
    def __init__(self):
        super(Drone, self).__init__()

        self.color = DRONE_YELLOW
        self.character = 'd'
        self.x = random.randrange(Constants.SCREEN_WIDTH)
        self.y = random.randrange(Constants.SCREEN_HEIGHT - 1)
