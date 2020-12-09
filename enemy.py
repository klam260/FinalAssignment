import os
import pygame
from bullet import bullet
from player import player
from surface import surface

class enemy():

    def __init__(self, width, height):
        self.enemylvl = 1
        self.hp = 2
        self.posx = (width - 250)
        self.posy = (height - 500)
        self.speed = 2
        self.enemyspeed = 2
        self.totalbullets = [] #might not be used
        self.bullet = bullet(self.posx, self.posy)
        if self.enemylvl == 1:
            self.img = pygame.image.load(os.path.join('./assets', 'enemy.png'))
            self.img = pygame.transform.scale(self.img, [100,100])
            self.dmg = 1
        elif self.enemylvl == 2:
            self.img = pygame.image.load(os.path.join('./assets', 'enemylvl2.png'))
            self.img = pygame.transform.scale(self.img, [150, 150])
            self.dmg = 2
        elif self.enemylvl == 3:
            self.img = pygame.image.load(os.path.join('./assets', 'enemylvl3.png'))
            self.img = pygame.transform.scale(self.img, [150, 150])
            self.dmg = 3

        self.player = player()
        self.surface = surface(width, height)

    def drawenemy(self, screen):
        screen.blit(self.img, [self.posx, self.posy])

    def enemymovement(self, playerposy, screen):
        if playerposy >= self.posy:
            self.posy += self.enemyspeed
            screen.blit(self.img, [self.posx, self.posy])
        elif playerposy <= self.posy:
            self.posy -= self.enemyspeed
            screen.blit(self.img, [self.posx, self.posy])

    #fires bullet relative to where the enemy is first, then calls the player collision method, if collision occurs, true is returns and health deduction occurs
    #once player health reaches 0, blit image off screen
    def enemyfire(self, screen, playerx, playery, player):
        self.bullet.enemyfire(screen, self.posx - 60, self.posy)
        if self.bullet.playerCollision(playerx, playery, self.posx, self.posy, self.bullet.bulletposx, self.bullet.bulletposy):
            if player.hp >= 1:
                player.hp -= self.dmg
                if player.hp <= 0:
                    # must remove bullet from game over here due to the current structure, as bullet from enemy is kept track in this function
                    self.bullet.bulletposx = -3000
                    return True



    def enemynextlvl(self):
        self.enemylvl += 1
        self.hp += self.enemylvl + 1


    def removeenemy(self):
        self.posy = 3000

    def enemyrestart(self, height):
        self.posy = height - 500
        self.hp = 3

    def displayhp(self, screen):
        font = pygame.font.Font(os.path.join('./assets', 'square.ttf'), 56)
        hp = font.render(str(self.hp), True, (255, 255, 255))
        screen.blit(hp, (self.posx + 30, self.posy - 60))























