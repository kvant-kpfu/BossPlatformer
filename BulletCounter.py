import pygame as pg
import pygame.math
from Scene import *
import pygame.freetype
from settings import *

class BulletCounter:
    @staticmethod
    def draw(n, sc):
        counter = pg.freetype.Font(None, 48)
        counter.render_to(sc, Vector2(20, 26), str(n), pg.Color(255, 255, 255))
