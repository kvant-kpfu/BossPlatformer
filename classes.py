import random

from Events import *
from pygame.math import *
from settings import *
import spritesheet


class fRect:
    def __init__(self, x, y, w, h):
        self.size = Vector2(w, h)
        self.center = Vector2(x, y) + self.size / 2

    def setPos(self, pos):
        self.center = pos + self.size / 2

    def getPos(self):
        return Vector2(self.left(), self.top())

    def getRect(self):
        return self.getPos(), self.size

    def left(self):
        return self.center.x - self.size.x / 2

    def right(self):
        return self.center.x + self.size.x / 2

    def top(self):
        return self.center.y - self.size.y / 2

    def bottom(self):
        return self.center.y + self.size.y / 2


class Object(pg.sprite.Sprite):
    def __init__(self, rect):
        super().__init__()
        self.rect = rect
        self.image = pg.Surface(self.rect.size)

    def setCol(self, col):
        self.image.fill(col)

    def setTextureRect(self, textureRect, ss):
        self.image = ss.image_at(textureRect.getRect(), -1)
        self.image = pg.transform.scale(self.image, self.rect.size)

    def draw(self, sc, pos):
        sc.blit(self.image, pos)


class GameObject(Object):
    def __init__(self, rect):
        super().__init__(rect)

        self.vel = Vector2(0, 0)
        self.m = 1
        self.onGround = False
        self.image = pg.transform.scale(self.image, self.rect.size / GameObject.zoom)

    cameraPos = Vector2(0, 0)
    zoom = 1

    def addForce(self, force):
        self.vel += force / self.m

    def setVel(self, vel):
        self.vel = vel

    def move(self, v):
        self.rect.center += v

    def update(self):
        self.rect.center += self.vel * dt

    def setTextureRect(self, textureRect, ss):
        self.image = ss.image_at(textureRect.getRect(), -1)
        self.image = pg.transform.scale(self.image, self.rect.size / GameObject.zoom)

    def draw(self, sc):
        sc.blit(self.image, (self.rect.getPos() - GameObject.cameraPos) / GameObject.zoom)


class Player(GameObject):
    def __init__(self, rect):
        super().__init__(rect)
        self.sideForce = 14
        self.jumpForce = 825 * 1.5
        self.sideForceCoeff = 10
        self.jumpCoeff = 1.1
        self.groundCoeff = 1.7

        self.allowCollide = True
        self.alive = True
        self.maxhp = 5
        self.hp = 5
        self.maxAmmo = 100
        self.ammo = 100

        self.damageCD = fps / 6
        self.currdamageCD = self.damageCD

    g = 2500
    airFriction = 0.98
    friction = 0.96

    def heal(self, n):
        self.hp += n
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def damage(self, n):
        if self.currdamageCD == 0:
            self.hp -= n
            self.currdamageCD = self.damageCD
        if self.hp <= 0:
            self.hp = 0
            self.alive = False
            self.setCol(pg.Color(255, 0, 0))

    def addAmmo(self, n):
        self.ammo += n
        if self.ammo > self.maxAmmo:
            self.ammo = self.maxAmmo

    def delAmmo(self, n):
        self.ammo -= n
        if self.ammo < 0:
            self.ammo = 0

    def setSideForce(self, force):
        self.sideForce = force

    def setJumpForce(self, force):
        self.jumpForce = force

    def update(self):
        if self.currdamageCD > 0:
            self.currdamageCD -= 1

        self.vel.y += Player.g * dt
        self.vel.x *= Player.airFriction
        if self.onGround:
            self.vel.x *= Player.friction
        self.rect.center += self.vel * dt

    def movement(self):
        keys = pg.key.get_pressed()
        if Events.a:
            self.addForce(Vector2(-self.sideForce, 0) * self.sideForceCoeff)
        if keys[pg.K_a]:
            if self.onGround:
                self.addForce(Vector2(-self.sideForce, 0) * self.groundCoeff)
            else:
                self.addForce(Vector2(-self.sideForce, 0))

        if Events.d:
            self.addForce(Vector2(self.sideForce, 0) * self.sideForceCoeff)
        if keys[pg.K_d]:
            if self.onGround:
                self.addForce(Vector2(self.sideForce, 0) * self.groundCoeff)
            else:
                self.addForce(Vector2(self.sideForce, 0))

        if keys[pg.K_SPACE] and self.onGround:
            self.vel.y = 0
            self.move(Vector2(0, -1))
            self.vel.x *= self.jumpCoeff
            self.addForce(Vector2(0, -self.jumpForce))

        if Events.s:
            self.allowCollide = False


class Block(GameObject):
    def __init__(self, rect):
        super().__init__(rect)


class Platform(GameObject):
    def __init__(self, rect):
        super().__init__(rect)


class Mosquito(GameObject):
    def __init__(self, rect):
        super().__init__(rect)
        self.speed = 200

    def aim(self, targetPos):
        v = targetPos - self.rect.center
        self.vel = v / length(v) * self.speed


class Bullet(GameObject):
    def __init__(self, rect):
        super().__init__(rect)
        self.speed = 200
        self.image = pg.transform.rotate(self.image, 45)


class Boss(GameObject):
    def __init__(self, rect):
        super().__init__(rect)
        self.hp = 30

    def damage(self, n):
        self.hp -= n
        if self.hp <= 0:
            self.hp = 0

    def getCenterSpawn(self):
        return self.rect.center


class Spawner(GameObject):
    def __init__(self, rect):
        super().__init__(rect)

    def getRandPos(self):
        return Vector2(random.randint(self.rect.left(), self.rect.right()),
                       random.randint(self.rect.top(), self.rect.bottom()))


class Collectable(GameObject):
    def __init__(self, rect):
        super().__init__(rect)
        self.type = random.choice(["hp", "ammo"])


class Explosion(GameObject):
    def __init__(self, rect):
        super().__init__(rect)
        self.damage = 2
        self.life_time = 60
        if length(player_pos - self.rect.center):
            Scene.player.damage(self.damage)

    def update(self):
        self.life_time -= 1


class Bomb(GameObject):
    g = 2500

    def __init__(self, rect):
        super().__init__(rect)
        self.life_time = 100

    def update(self):
        self.vel += Bomb.g * dt
        self.life_time -= 1
