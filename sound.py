import os
import pygame

class sound():

    def __init__(self):
        self.cannon = pygame.mixer.Sound(os.path.join('./assets/sounds', 'cannon.mp3'))
        self.cannon.set_volume(0.3)
        self.collisionsound = pygame.mixer.Sound(os.path.join('./assets/sounds', 'hit.mp3'))
        self.collisionsound.set_volume(0.3)

    def selectbgm(self, currentlevel):
        if currentlevel == 1:
            pygame.mixer.music.set_volume(0.30)
            pygame.mixer.music.load(os.path.join('./assets/bgm', 'Against All Odds.wav'))
            pygame.mixer.music.play(-1)
        elif currentlevel == 2:
            pygame.mixer.music.set_volume(0.30)
            pygame.mixer.music.load(os.path.join('./assets/bgm', 'Frozen Forest.mp3'))
            pygame.mixer.music.play(-1)
        elif currentlevel == 3:
            pygame.mixer.music.set_volume(0.30)
            pygame.mixer.music.load(os.path.join('./assets/bgm', 'Cynical Ballroom Dance.wav'))
            pygame.mixer.music.play(-1)

    #leveling up chooses a different bgm might be useless
    # def soundlvlup(self):
    #     if self.lvl < 3:
    #         self.lvl += 1
    #     else:
    #         self.lvl = 3

