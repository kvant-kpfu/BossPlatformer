import pygame as pg
from math import *
import spritesheet
scSize = pg.math.Vector2(1000, 1000)
fps = 120
dt = 1/fps
scCol = (0, 255, 255)

pg.init()
sc = pg.display.set_mode(scSize)
pg.display.set_caption("doodlecock")
ss = spritesheet.spritesheet("C:/Users/ПК/PycharmProjects/gamebebra/images/shitss3.png")


def length(v):
    return sqrt(v.x ** 2 + v.y ** 2)