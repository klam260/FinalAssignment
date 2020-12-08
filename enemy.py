import os
import pygame
from bullet import bullet
from player import player
from surface import surface

class enemy():

    def __init__(self, width, height):
        self.hp = 2
        self.posx = (width - 250)
        self.posy = (height - 500)
        self.speed = 2
        self.enemyspeed = 2
        self.totalbullets = [] #might not be used
        self.bullet = bullet(self.posx, self.posy)
        self.img = pygame.image.load(os.path.join('./assets', 'enemy.png'))
        self.img = pygame.transform.scale(self.img, [100,100])
        self.player = player()
        self.surface = surface('background.png', width, height)

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
    def enemyfire(self, screen, playerx, playery):
        self.bullet.enemyfire(screen, self.posx - 60, self.posy)
        if self.bullet.playerCollision(playerx, playery, self.posx, self.posy, self.bullet.bulletposx, self.bullet.bulletposy):
            if self.player.hp > 0:
                self.player.hp -= 1
            elif self.player.hp == 0:
                self.player.posy = 3000
                self.surface.gameover(screen)





















