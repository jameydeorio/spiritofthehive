import ConfigParser
import os
import pygame


class Constants:
    DATA_DIR = os.path.abspath(os.path.join(__file__, '../../../data'))
    RES_DIR = os.path.abspath(os.path.join(__file__, '../../../res'))
    CONFIG = ConfigParser.ConfigParser()
    CONFIG.read(os.path.join(DATA_DIR, '../data/config.ini'))

    FPS = 40
    GAME_WIDTH = 40
    SCREEN_WIDTH = GAME_WIDTH
    SCREEN_HEIGHT = 30
    BG_COLOR = pygame.Color(0, 0, 0)
