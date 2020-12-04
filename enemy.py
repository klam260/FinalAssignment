import os
import pygame
from bullet import bullet

class enemy():

    def __init__(self, width, height):
        self.enemyhp = 1
        self.posx = (width - 250)
        self.posy = (height - 500)
        self.speed = 5
        self.enemyspeed = 2
        self.totalbullets = []
        self.bullet = bullet(self.posx, self.posy)
        self.img = pygame.image.load(os.path.join('./assets', 'enemy.png'))
        self.img = pygame.transform.scale(self.img, [100,100])

    def drawenemy(self, screen):
        screen.blit(self.img, [self.posx, self.posy])

    def enemymovement(self, playerposy, screen):
        if playerposy >= self.posy:
            self.posy += self.enemyspeed
            screen.blit(self.img, [self.posx, self.posy])
        elif playerposy <= self.posy:
            self.posy -= self.enemyspeed
            screen.blit(self.img, [self.posx, self.posy])

    def enemyfire(self, screen):
        bulletposx = self.posx
        bulletposy = self.posy
        self.bullet.enemyfire(screen, bulletposx - 60, bulletposy)














