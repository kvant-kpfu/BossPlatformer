import pygame as pg
from Scene import *
from settings import *

class HealthBar:
    @staticmethod
    def draw(n, sc):
        obj = Object(fRect(0, 0, 48, 48))
        obj.setTextureRect(fRect(17 * 64, 1 * 64, 1 * 64, 1 * 64), ss)
        for i in range(0, n):
            obj.draw(sc, Vector2(90 + 68 * i, 20))
