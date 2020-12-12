import os
import pygame
from bullet import bullet
from player import player
from surface import surface

class enemy():

    def __init__(self, width, height, font):
        self.enemylvl = 1
        self.hp = 3
        self.basehp = 3 #basehp is stored so that it can be used to calculate HP increase when leveling
        self.posx = (width - 250)
        self.posy = (height - 500)
        self.dmg = 1
        self.enemyspeed = 1
        self.totalbullets = [] #might not be used
        self.bullet = bullet(self.posx, self.posy)
        self.player = player(font)
        self.surface = surface(width, height, font)
        self.font = font

        #initiating images here to reduce load time
        self.img = pygame.image.load(os.path.join('./assets', 'enemy.png'))
        self.img = pygame.transform.scale(self.img, [100, 100])
        self.imglvl2 = pygame.image.load(os.path.join('./assets', 'enemylvl2.png'))
        self.imglvl2 = pygame.transform.scale(self.imglvl2, [125, 125])
        self.imglvl3 = pygame.image.load(os.path.join('./assets', 'enemylvl3.png'))
        self.imglvl3 = pygame.transform.scale(self.imglvl3, [150, 150])

    def enemymovement(self, playerposy):
        if playerposy > self.posy:
            self.posy += self.enemyspeed
        elif playerposy < self.posy:
            self.posy -= self.enemyspeed
        elif playerposy == self.posy:
            self.posy = playerposy

    #fires bullet relative to where the enemy is first, then calls the player collision method, if collision occurs, true is returns and health deduction occurs
    #once player health reaches 0, blit image off screen
    def enemyfire(self, screen, playerx, playery, player):
        self.bullet.enemyfire(screen, self.posx - 60, self.posy)
        if self.bullet.playerCollision(playerx, playery, self.posx, self.posy, self.bullet.bulletposx, self.bullet.bulletposy):
            if player.hp >= 1:
                player.hp -= self.dmg
        if player.hp <= 0 or self.hp <= 0: #if player hp hits zero or enemy own hp hits zero, remove bullet being fired
            # must remove bullet from game over here due to the current structure, as bullet from enemy is kept track in this function
            self.bullet.bulletposx = self.posx
            self.bullet.bulletposy = self.posy


    def enemynextlvl(self):
        self.enemylvl += 1
        self.hp += 1
        self.dmg += 1
        self.enemyspeed += 1
        self.basehp += 1


    def removeenemy(self):
        self.posy = 3000

    def enemyrestart(self, height):
        self.posy = height - 500 #takes screen height and then places enemy 500 above.
        self.hp = self.basehp

    def displayhp(self, screen):
        hp = self.font.render(str(self.hp), True, (255, 255, 255))
        screen.blit(hp, (self.posx + 30, self.posy - 60))

    def drawenemy(self, screen):

        if self.enemylvl == 1:
            screen.blit(self.img, [self.posx, self.posy])
        elif self.enemylvl == 2:
            screen.blit(self.imglvl2, [self.posx, self.posy])
        elif self.enemylvl == 3:
            screen.blit(self.imglvl3, [self.posx, self.posy])






















