import classes
from classes import *
from pygame.math import *


class Scene:
    blocks = []
    platforms = []
    mosquito = []
    bullets = []
    spawners = []
    collectables = []

    bombs = []
    explosions = []

    lastObject = 0
    player = 0
    boss = 0


    allowCollide = True


    rect = fRect(0, 0, 0, 0)


    @staticmethod
    def getMousePos():
        return Vector2(pg.mouse.get_pos()) * GameObject.zoom + GameObject.cameraPos

    @staticmethod
    def createObject(object):
        Scene.lastObject = object

        if object.__class__ == classes.Player:
            Scene.player = object

        elif object.__class__ == classes.Boss:
            Scene.boss = object

        elif object.__class__ == classes.Block:
            Scene.blocks.append(object)

        elif object.__class__ == classes.Platform:
            Scene.platforms.append(object)

        elif object.__class__ == classes.Mosquito:
            Scene.mosquito.append(object)

        elif object.__class__ == classes.Bullet:
            Scene.bullets.append(object)

        elif object.__class__ == classes.Spawner:
            Scene.spawners.append(object)

        elif object.__class__ == classes.Collectable:
            Scene.collectables.append(object)

    @staticmethod
    def getAllObjects():
        return Scene.blocks + Scene.platforms + Scene.bullets + Scene.mosquito + Scene.collectables + [Scene.player] + [Scene.boss] + Scene.bombs + Scene.explosions

    @staticmethod
    def draw(sc):
        for obj in Scene.blocks + Scene.platforms + Scene.bullets:
            obj.draw(sc)

        Scene.boss.draw(sc)

        for obj in Scene.collectables:
            obj.draw(sc)

        Scene.player.draw(sc)

        for obj in Scene.mosquito:
            obj.draw(sc)

    @staticmethod
    def getSize(sc):
        return Vector2(sc.get_size()) * GameObject.zoom

    @staticmethod
    def setCameraRect(rect):
        Scene.rect = rect

    @staticmethod
    def setZoom(zoom):
        GameObject.zoom = zoom

    @staticmethod
    def updateZoom():
        for obj in Scene.getAllObjects():
            obj.image = pg.transform.scale(obj.image, obj.rect.size / GameObject.zoom)

    @staticmethod
    def setCameraPos(pos, sc):
        GameObject.cameraPos = pos - Vector2(sc.get_size()) * GameObject.zoom / 2

    @staticmethod
    def setCameraPosInRect(pos0, sc):
        pos = Vector2(pos0)

        xr = Scene.rect.right() - Scene.getSize(sc).x / 2
        xl = Scene.rect.left() + Scene.getSize(sc).x / 2
        if xr < pos.x:
            pos.x = xr
        elif pos.x < xl:
            pos.x = xl

        yb = Scene.rect.bottom() - Scene.getSize(sc).y / 2
        yt = Scene.rect.top() + Scene.getSize(sc).y / 2
        if yb < pos.y:
            pos.y = yb
        elif pos.y < yt:
            pos.y = yt

        Scene.setCameraPos(pos, sc)



    @staticmethod
    def collision():

        Scene.player.onGround = False

        for obj in Scene.blocks:
            p = Scene.collisionDetection(Scene.player, obj)
            if p != Vector2(0, 0):
                Scene.player.move(p)
            if p.y != 0:
                Scene.player.vel.y = 0
            if p.y < 0:
                Scene.player.onGround = True
            if abs(p.x) > 0.03:
                Scene.player.vel.x = 0





        check = True
        if Scene.player.vel.y >= 0:
            for obj in Scene.platforms:
                p = Scene.collisionDetection(Scene.player, obj)
                if p != Vector2(0, 0):
                    check = False

                if p.y < 0 and Scene.player.allowCollide:
                    Scene.player.vel.y = 0
                    Scene.player.move(p)
                    Scene.player.onGround = True
        if check:
            Scene.player.allowCollide = True


        for i in range(len(Scene.bullets) - 1, -1, -1):
            for obj in Scene.blocks + [Scene.boss]:
                if len(Scene.bullets) > i:
                    p = Scene.collisionDetection(Scene.bullets[i], obj)
                    if p != Vector2(0, 0):
                        del Scene.bullets[i]
                        if obj.__class__ == classes.Boss:
                            Scene.boss.damage(1)

        for i in range(len(Scene.mosquito) - 1, -1, -1):
            for obj in Scene.bullets + [Scene.player]:
                if len(Scene.mosquito) > i:
                    p = Scene.collisionDetection(obj, Scene.mosquito[i])
                    if p != Vector2(0, 0):
                        if obj.__class__ == classes.Bullet:
                            del Scene.mosquito[i]
                        if obj.__class__ == classes.Player:
                            Scene.player.move(p)
                            v = Scene.player.rect.center - Scene.mosquito[i].rect.center
                            Scene.player.addForce(v / length(v) * 500)
                            Scene.player.damage(1)


        for i in range(len(Scene.collectables) - 1, -1, -1):
            if len(Scene.collectables) > i:
                p = Scene.collisionDetection(Scene.player, Scene.collectables[i])
                if p != Vector2(0, 0):
                    if Scene.collectables[i].type == "hp":
                        Scene.player.heal(5)
                    elif Scene.collectables[i].type == "ammo":
                        Scene.player.addAmmo(10)
                    del Scene.collectables[i]

        p = Scene.collisionDetection(Scene.player, Scene.boss)
        if p != Vector2(0, 0):
            Scene.player.move(p)
            v = Scene.player.rect.center - Scene.boss.rect.center
            Scene.player.addForce(v / length(v) * 400)
            Scene.player.damage(1)









    @staticmethod
    def collisionDetection(obj1, obj2):
        r1 = obj1.rect
        r2 = obj2.rect
        if r1.left() < r2.right() and \
            r2.left() < r1.right() and \
            r1.top() < r2.bottom() and \
            r2.top() < r1.bottom():

            px1 = abs(r2.right() - r1.left())
            px2 = abs(r1.right() - r2.left())

            py1 = abs(r2.bottom() - r1.top())
            py2 = abs(r1.bottom() - r2.top())

            if px1 > px2:
                resx = -px2
            else:
                resx = px1

            if py2 < py1:
                resy = -py2
            else:
                resy = py1

            if abs(resx) < abs(resy):
                return Vector2(resx, 0)
            else:
                return Vector2(0, resy)

        return Vector2(0, 0)


