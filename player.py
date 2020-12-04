import os
import pygame
from bullet import bullet

class player():

    def __init__(self, health, playerlvl):

        self.health = health
        self.posx = 200
        self.posy = 500
        self.speed = 5
        self.totalbullets = []

        # if state defines which ship to use depending on player level.

        if playerlvl == 1 :
            self.image = pygame.image.load(os.path.join('./assets', 'playerlvl1.png'))
            self.image = pygame.transform.scale(self.image, (75, 75))
        elif playerlvl == 2 :
            self.image = pygame.image.load(os.path.join('./assets', 'playerlvl2.png'))
            self.image = pygame.transform.scale(self.image, (75, 75))
        elif playerlvl == 3 :
            self.image = pygame.image.load(os.path.join('./assets', 'playerlvl3.png'))
            self.image = pygame.transform.scale(self.image, (75, 75))

    #for moving left and right
    def playermovex(self, num, width):
        self.posx += num * self.speed

        if self.posx <= 0 or self.posx >= width:
            self.posX -= 1

    #for moving up and down
    def playermovey(self, num, height):
        self.posy += num * self.speed

        if self.posy <= 0:
            self.posy = 0

    #draws player to the screen
    def drawplayer (self, screen):
        screen.blit(self.image, [self.posx, self.posy])


