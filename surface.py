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
        font = pygame.font.Font(os.path.join('./assets', 'square.ttf'), 56)
        gameover = font.render('GAME OVER', True, (255, 0, 0))
        screen.blit(gameover, (600, 255))

    def victory(self, screen):
        font = pygame.font.Font(os.path.join('./assets', 'square.ttf'), 56)
        gameover = font.render('Victory', True, (0, 255, 0))
        screen.blit(gameover, (600, 255))


