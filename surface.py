import pygame
import sys
import os

class surface():

    def __init__(self, bgimg, width, height):
        self.bg_surface = pygame.image.load(os.path.join("./assets", bgimg))
        self.bg_surface = pygame.transform.scale(self.bg_surface, (width, height))


    def drawbg(self, screen):
        screen.blit(self.bg_surface, [0,0])

    def gameover(self, screen):
        font = pygame.fontFont(os.path.join('./assets', 'square.ttf'), 28)
        gameover = font.render('GAME OVER', True, (255, 255, 255))
        screen.blit(gameover, (80, 255))

