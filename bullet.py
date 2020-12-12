import os
import pygame
import math


class bullet():

    def __init__(self, posx, posy):
        self.img = pygame.image.load(os.path.join('./assets', 'bullet.png'))
        self.img = pygame.transform.scale(self.img, (25, 25))
        self.bulletposx = posx
        self.bulletposy = posy
        self.bulletspeed = 20
        self.enemybulletspeed = 8
        self.state = 'ready'
        self.enemystate = 'ready'


    def fire(self, screen):
        screen.blit(self.img, [self.bulletposx + 70, self.bulletposy + 20])

    def enemyfire(self, screen, enemyposx, enemyposy):
        self.enemystate = 'fire'
        screen.blit(self.img, [self.bulletposx - 60, self.bulletposy])
        self.bulletposx -= self.enemybulletspeed #change the bullet position speed here if you don't want to make it the same.
        # print(self.bulletposx)
        if self.bulletposx <= 0:
            self.enemystate = 'ready'
            self.bulletposx = enemyposx
            self.bulletposy = enemyposy

    #for collision from player bullets
    def enemyCollision(self, positionx, positiony, bulletx, bullety):
        distance = math.sqrt((math.pow(positionx - bulletx, 2)) + (math.pow(positiony-bullety,2)))
        # print(f"this is the distance from player to enemy: {distance}")
        if distance < 27:
           #moves bullet off screen upon contact, when trying to move bullet back to player, it starts looping.
            self.bulletposx = 2000
            self.bulletposy = 2000
            self.state = 'ready'
            return True

    #for collision from enemy bullets.
    def playerCollision(self, playerx, playery, enemyposx, enemyposy, bulletx, bullety):
        distance = math.sqrt((math.pow(playerx - bulletx, 2)) + (math.pow(playery-bullety,2)))
        # print(f"this is the distance from enemy to player: {distance}")
        if distance < 70:
           #moves bullet off screen upon contact, when trying to move bullet back to player, it starts looping.
            # print(f'collision from enemy occured at {distance}' )
            self.bulletposx = enemyposx
            self.bulletposy = enemyposy
            self.enemystate = 'ready'
            return True


# this function was created to see if it gets rid of a bug where bullet fired does not consistently follow where the player is if player moves and fires at the same time.
    def updateposition(self, posx, posy):
        self.bulletposx = posx
        self.bulletposy = posy

    def drawbullet(self, screen, bulletposx, bulletposy):
        screen.blit(self.img, [bulletposx, bulletposy])


