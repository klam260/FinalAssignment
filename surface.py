import pygame
import math
import os

class surface():

    def __init__(self, width, height):
        self.lvl = 1
        self.startimg = pygame.image.load(os.path.join("./assets", 'start.png'))
        self.startimg = pygame.transform.scale(self.startimg, (width, height))

        if self.lvl == 1:
            self.bgimg = pygame.image.load(os.path.join("./assets", 'background.png'))
            self.bgimg = pygame.transform.scale(self.bgimg, (width, height))
        elif self.lvl == 2:
            self.bgimg = pygame.image.load(os.path.join("./assets", 'backgroundlvl2.png'))
            self.bgimg = pygame.transform.scale(self.bgimg, (width, height))
        elif self.lvl == 3:
            self.bgimg = pygame.image.load(os.path.join("./assets", 'backgroundlvl3.png'))
            self.bgimg = pygame.transform.scale(self.bgimg, (width, height))
        elif self.lvl == 0:
            self.bgimg = pygame.image.load(os.path.join("./assets", 'start.png'))
            self.bgimg = pygame.transform.scale(self.bgimg, (width, height))


    def drawbg(self, screen):
        screen.blit(self.bgimg, [0,0])

    def gameover(self, screen):
        font = pygame.font.Font(os.path.join('./assets', 'square.ttf'), 56)
        gameover = font.render('GAME OVER', True, (255, 0, 0))
        screen.blit(gameover, (600, 255))

    def victory(self, screen):
        font = pygame.font.Font(os.path.join('./assets', 'square.ttf'), 56)
        victory = font.render('Victory press T to proceed to next level', True, (0, 255, 0))
        screen.blit(victory, (300, 400))

    def startscreen(self, screen):
       screen.blit(self.startimg, [0,0])
       font = pygame.font.Font(os.path.join('./assets', 'square.ttf'), 50)
       menu = font.render('Welcome to 2d Divers! Press P to start!', True, (0, 0, 0))
       subtext = font.render('Travel across the world on your pirate ship', True, (0, 0, 0))
       subtext2 = font.render('and defeat enemies to find treasure!', True, (0, 0, 0))
       screen.blit(menu, (200, 255))
       screen.blit(subtext,(200, 355))
       screen.blit(subtext2, (200, 455))


class score():
    def __init__(self):
        self.score = 0

    def updatescore(self, scoreamount):
        self.score += scoreamount

    def drawscore(self, screen):
        font = pygame.font.Font(os.path.join('./assets', 'square.ttf'), 28)
        score = font.render(f'SCORE: {self.score}', True, (255, 0, 0))
        screen.blit(score, (50, 50))

class timer():
    def __init__(self):
        self.seconds = 0
        self.bonus = 1000
        self.minutes = 0
        self.state = True

    def bonusscore(self, seconds):
        return math.trunc(seconds) * self.bonus

    def drawtimer(self, screen, seconds):
        font = pygame.font.Font(os.path.join('./assets', 'square.ttf'), 28)
        timer = font.render(f" Time in seconds: {math.trunc(seconds)}", True, (255, 0, 0))
        screen.blit(timer, (800, 50))










