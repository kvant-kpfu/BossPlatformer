import pygame as pg



class Events:

    LMBpressed = False
    LMBreleased = False
    RMBpressed = False
    RMBreleased = False
    space = False
    a = False
    s = False
    d = False
    run = True
    @staticmethod
    def keysReset():
        Events.LMBpressed = False
        Events.LMBreleased = False
        Events.RMBpressed = False
        Events.RMBreleased = False
        Events.space = False
        Events.a = False
        Events.s = False
        Events.d = False

    @staticmethod
    def update():
        Events.keysReset()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                Events.run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                Events.LMBpressed = True
            if event.type == pg.KEYDOWN:

                if event.key == pg.K_ESCAPE:
                    Events.run = False
                if event.key == pg.K_SPACE:
                    Events.space = True
                if event.key == pg.K_a:
                    Events.a = True
                if event.key == pg.K_d:
                    Events.d = True
                if event.key == pg.K_s:
                    Events.s = True

