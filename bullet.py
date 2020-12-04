import os
import pygame

class bullet():

    def __init__(self, playerposx, playerposy):
        self.img = "bullet.png"
        self.img = pygame.image.load(os.path.join('./assets', 'bullet.png'))
        self.img = pygame.transform.scale(self.img, (25, 25))
        self.bulletposx = playerposx
        self.bulletposy = playerposy
        self.bulletspeed = 10
        self.state = 'ready'
        self.enemystate = 'ready'


    def fire(self, screen, width, playerposx, playerposy):
        self.state = 'fire'
        screen.blit(self.img, [self.bulletposx + 70, self.bulletposy + 20])

        #resets position after reaching the end of the screen might change this to recognize collision.

        if self.bulletposx >= width:
            self.state ='ready'
            self.bulletposx = playerposx
            self.bulletposy = playerposy

    def enemyfire(self, screen, enemyposx, enemyposy):
        screen.blit(self.img, [self.bulletposx - 60, enemyposy])
        self.bulletposx -= 8


        if self.bulletposx <= 0:
            self.enemystate = 'ready'
            self.bulletposx = enemyposx
            self.bulletposy = enemyposy


    def drawbullet(self, screen, bulletposx, bulletposy):
        screen.blit(self.img, [bulletposx, bulletposy])


