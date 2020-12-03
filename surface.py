import pygame
import sys
import os

class background:

    def __init__(self, bgimg, width, height):
        self.bg_surface = pygame.image.load(os.path.join("./assets", bgimg))
        self.bg_surface = pygame.transform.scale(self.bg_surface, (width, height))


    def drawbg(self, screen):
        screen.blit(self.bg_surface, [0,0])

