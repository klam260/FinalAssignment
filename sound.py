import os
import pygame

class sound():

    def __init__(self):
        self.startscreenbgm = pygame.mixer.Sound( os.path.join('./assets/bgm', 'Against All Odds.wav'))
        self.startscreenbgm.set_volume(0.10)
        self.cannon = pygame.mixer.Sound = pygame.mixer.Sound(os.path.join('./assets/sounds', 'cannon.mp3'))

