import os
import pygame

class enemy():

    def __init__(self, width, height):
        self.enemyhp = 1
        self.posx = width / 0.75
        self.posy = height / 1.5
        self.speed = 5
        self.img = pygame.image.load(os.path.join('./assets', 'enemy.png'))
        self.img = pygame.transform.scale(self.img, [100,100])

    def drawenemy(self, screen):
        screen.blit(self.img, [self.posx, self.posy])

    def enemymovement(self, playerposy):
        if playerposy > self.posx:






