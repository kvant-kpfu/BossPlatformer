import csv

from Scene import *
from settings import *
import spritesheet
from BulletCounter import *
from HealthBar import *
from BossBar import *
import random





map1 = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
        [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]

map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 2, 2, 0, 0, 0, 4, 0, 0, 0, 2, 2, 0, 1],
       [1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
       [1, 1, 0, 2, 2, 0, 0, 0, 0, 0, 2, 2, 0, 1, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 2, 2, 0, 0, 3, 0, 0, 0, 0, 2, 2, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 1, 0, 2, 2, 0, 0, 0, 0, 0, 2, 2, 0, 1, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 1],
       [1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
       [1, 0, 2, 2, 2, 0, 0, 0, 0, 0, 2, 2, 2, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


Scene.setZoom(1)

# player
Scene.createObject(Player(fRect(4 * 64, 33 * 64, 24, 40)))
Scene.lastObject.setTextureRect(fRect(18 * 64, 0 * 64, 1 * 64, 2 * 64), ss)
player = Scene.lastObject




with open("C:/Users/ПК/PycharmProjects/gamebebra/maps/etiles2.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
map = data

# map generating
for y in range(40):
    for x in range(40):

        if map[y][x] == str(187) or map[y][x] == str(62):
            Scene.createObject(Platform(fRect(64 * x, 64 * y, 64, 48)))
            Scene.lastObject.setTextureRect(fRect(15 * 64, 2 * 64 + 16, 3 * 64, 1 * 48), ss)

        if map[y][x] == str(0):
            Scene.createObject(Block(fRect(64 * x, 64 * y, 64, 64)))
            Scene.lastObject.setTextureRect(fRect(0 * 64, 0 * 64, 1 * 64, 1 * 64), ss)

        if map[y][x] == str(186):
            Scene.createObject(Block(fRect(64 * x, 64 * y, 64, 64)))
            Scene.lastObject.setTextureRect(fRect(0 * 64, 3 * 64 - 1, 1 * 64, 1 * 64), ss)

        if map[y][x] == str(15):
            Scene.createObject(Block(fRect(64 * x, 64 * y, 64, 64)))
            Scene.lastObject.setTextureRect(fRect(15 * 64, 0 * 64, 1 * 64, 1 * 64), ss)

        if map[y][x] == str(16):
            Scene.createObject(Block(fRect(64 * x, 64 * y, 64, 64)))
            Scene.lastObject.setTextureRect(fRect(16 * 64, 0 * 64, 1 * 64, 1 * 64), ss)

        # if map[y][x] == 2:
        #     Scene.createObject(Platform(fRect(64 * x, 64 * y, 64, 16)))
        #     Scene.lastObject.setCol(pg.Color(255, 128, 0))
        #
        # if map[y][x] == 3:
        #     Scene.createObject(Boss(fRect(64 * x, 64 * y, 192, 192)))
        #     Scene.lastObject.setTextureRect(fRect(64, 0, 192, 192), ss)
        #
        # if map[y][x] == 4:
        #     Scene.createObject(Spawner(fRect(64 * x, 64 * y, 64, 64)))
        #     Scene.lastObject.setCol(pg.Color(0, 255, 0))



Scene.setCameraRect(fRect(0, 0, 40 * 64, 40 * 64))


Scene.createObject(Boss(fRect(64 * 5, 0, 192, 192)))
Scene.lastObject.setTextureRect(fRect(64, 0, 192, 192), ss)




ticks = 0
reload = 0

while Events.run:
    sc.fill(scCol)
    pg.time.Clock().tick(fps)
    Events.update()

    ticks += 1

    if ticks % (fps * 2) == 0:
        spos = Scene.boss.getCenterSpawn()
        Scene.createObject(Mosquito(fRect(spos.x, spos.y, 32, 32)))
        Scene.lastObject.setTextureRect(fRect(5 * 64, 1 * 64, 2 * 64, 2 * 64), ss)

    # if ticks % (fps * 5) == 0:
    #     rpos = Scene.spawners[random.randint(0, len(Scene.spawners) - 1)].getRandPos()
    #     Scene.createObject(Collectable(fRect(rpos.x - 16, rpos.y - 16, 32, 32)))
    #     if Scene.lastObject.type == "hp":
    #         Scene.lastObject.setCol(pg.Color(0, 255, 255))
    #     elif Scene.lastObject.type == "ammo":
    #         Scene.lastObject.setCol(pg.Color(255, 255, 0))

    Scene.boss.vel.x = -3 * (Scene.boss.rect.center.x - Scene.player.rect.center.x)
    Scene.boss.vel.y = -1 * (Scene.boss.rect.center.y - (Scene.player.rect.center.y - 300))



    if reload > 0:
        reload -= 1


    Scene.collision()


    for obj in Scene.getAllObjects():
        obj.update()



    if player.alive:
        for obj in Scene.mosquito:
            obj.aim(player.rect.center)
        player.movement()
        Scene.setCameraPosInRect(Scene.player.rect.center, sc)

        if Events.LMBpressed and Scene.player.ammo > 0 and reload < 1:



            mpos = Scene.getMousePos()
            Scene.createObject(Bullet(fRect(player.rect.center.x - 12, player.rect.center.y - 12, 24, 24)))
            v = mpos - player.rect.center
            Scene.lastObject.setVel(v / length(v) * 400)
            Scene.lastObject.setTextureRect(fRect(64 * 5, 64 * 0, 64 * 1, 64 * 1), ss)
            Scene.player.delAmmo(1)
            reload = fps / 6



    Scene.draw(sc)
    HealthBar.draw(player.hp, sc)
    BulletCounter.draw(player.ammo, sc)
    BossBar.draw(Scene.boss.hp, sc)





    pg.display.update()

quit()
