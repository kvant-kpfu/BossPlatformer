import pygame as pg
from Scene import *
from settings import *

class BossBar:
    @staticmethod
    def draw(n, sc):
        obj = Object(fRect(0, 0, 15, 30))
        obj.setCol(pg.Color(230, 20, 20))
        for i in range(0, n):
            obj.draw(sc, Vector2(scSize.x - 30 - 16 * i, 20))