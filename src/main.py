#!/usr/bin/env python

import os
import sys

import pygame
from classes.bees import Queen, Worker, Drone
from helpers import colors
from lib import pygcurse

from helpers.constants import Constants


# TODO:


class Game(object):
    def __init__(self):
        self.window = pygcurse.PygcurseWindow(Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT, "Spirit of the Hive")
        pygame.mouse.set_visible(Constants.CONFIG.getboolean('game', 'mouse'))
        self.window.autoupdate = False
        # self.clock = pygame.time.Clock()

        font_name = Constants.CONFIG.get('game', 'font')
        font_size = Constants.CONFIG.getint('game', 'font_size')
        self.window.font = pygame.font.Font(os.path.join(Constants.RES_DIR, font_name), font_size)

        self.creatures = []
        self.creatures.append(Queen())

        self.turn = 0

        self.exit_game_loop = False

        # render once to display the initial screen
        # self.window.setscreencolors(None, 'black', clear=True)
        # self.window.fill(bgcolor=Constants.BG_COLOR, region=(1, 1, Constants.SCREEN_WIDTH - 1, Constants.SCREEN_HEIGHT - 1))
        self.render()

    def run(self):
        while 1:
            # self.clock.tick(Constants.FPS)

            # input
            for event in pygame.event.get():
                if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN:
                    self.turn += 1

                    # compute
                    for creature in self.creatures:
                        creature.move()

                    for i in range(50):
                        self.creatures.insert(0, Worker())

                    for i in range(1):
                        self.creatures.insert(0, Drone())

                    # draw
                    self.render()

    def render(self):
        self.window.setscreencolors(None, 'black', clear=True)
        self.window.fill(bgcolor=Constants.BG_COLOR, region=(1, 1, Constants.SCREEN_WIDTH - 1, Constants.SCREEN_HEIGHT - 1))

        for creature in self.creatures:
            creature.draw(self.window)

        self.window.fill(
            bgcolor=colors.WHITE,
            fgcolor=colors.BLACK,
            region=(0, Constants.SCREEN_HEIGHT - 1, Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT)
        )
        self.window.write('TURN: {0}'.format(self.turn), 0, Constants.SCREEN_HEIGHT - 1, colors.BLACK, colors.WHITE)
        number_of_bees = len(self.creatures) * 100
        number_of_bees_message = 'BEES: {0}'.format(number_of_bees)
        self.window.write(
            number_of_bees_message,
            Constants.SCREEN_WIDTH - len(number_of_bees_message) - 1,
            Constants.SCREEN_HEIGHT,
            colors.BLACK,
            colors.WHITE
        )

        self.window.update()


def main():
    while 1:
        game = Game()
        game.run()


if __name__ == '__main__':
    main()
