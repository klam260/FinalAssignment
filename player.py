import os
import pygame

class player():

    def __init__(self, font):

        self.hp = 4
        self.posx = 200
        self.posy = 500
        self.speed = 5
        self.playerlvl = 1
        self.image = 'initiate'
        self.dmg = 1
        self.font = font

        # if state defines which ship to use depending on player level.


    #for moving left and right
    def playermoveright(self, width):
        self.posx += self.speed

        if self.posx >= width:
            self.posx -= 1
        elif self.posx <= 0:
            self.posx += 1

    #for moving up and down
    def playermovedown(self, height):
        self.posy += self.speed

        if self.posy <= 0:
            self.posy = 0
        elif self.posy >= height:
            self.posy -= 1

    def playermoveleft(self,width):
        self.posx -= self.speed

        if self.posx >= width:
            self.posx -=1
        elif self.posx <= width:
            self.posx += 1
    def playermoveup(self, height):
        self.posy -= self.speed

        if self.posy <= 0:
            self.posy += 1
        elif self.posy >= height - 60:
            self.posy -= 1

    #draws player to the screen
    def drawplayer (self, screen):
        self.image = pygame.image.load(os.path.join('./assets', 'playerlvl2.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (75, 75))

        screen.blit(self.image, [self.posx, self.posy])


    def playerrestart(self):
        self.posx = 200
        self.posy = 500
        self.hp = 4

    def removeplayer(self):
        self.posx += 3000

    def displayhp(self, screen):
        # font = pygame.font.Font(os.path.join('./assets', 'square.ttf'), 56)
        hp = self.font.render(str(self.hp), True, (255, 255, 255))
        screen.blit(hp, (self.posx + 30, self.posy - 60))



