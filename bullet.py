import os
import pygame
import math


class bullet():

    def __init__(self, posx, posy):
        self.img = "bullet.png"
        self.img = pygame.image.load(os.path.join('./assets', 'bullet.png'))
        self.img = pygame.transform.scale(self.img, (25, 25))
        self.bulletposx = posx
        self.bulletposy = posy
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
        self.enemystate = 'fire'
        screen.blit(self.img, [self.bulletposx - 60, self.bulletposy])
        self.bulletposx -= 8
        print(self.bulletposx)
        if self.bulletposx <= 0:
            self.enemystate = 'ready'
            self.bulletposx = enemyposx
            self.bulletposy = enemyposy

    #for collision from player bullets
    def isCollision(self, positionx, positiony, bulletx, bullety):
        distance = math.sqrt((math.pow(positionx - bulletx, 2)) + (math.pow(positiony-bullety,2)))
        print(f"this is the distance from player to enemy: {distance}")
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



    def drawbullet(self, screen, bulletposx, bulletposy):
        screen.blit(self.img, [bulletposx, bulletposy])


