import pygame
import math
import os

class surface():

    def __init__(self, width, height, font):
        self.lvl = 1
        self.startimg = pygame.image.load(os.path.join("./assets", 'start.png')).convert()
        self.startimg = pygame.transform.scale(self.startimg, (width, height))
        self.width = width
        self.height = height
        self.bgimg = "initate"
        self.bonusposx = 800
        self.bonusposy = 400
        self.font = font

        #initiating images here to prevent lag
        self.bgimg = pygame.image.load(os.path.join("./assets", 'background.png')).convert_alpha()
        self.bgimg = pygame.transform.scale(self.bgimg, (self.width, self.height))

        self.bgimglvl2 = pygame.image.load(os.path.join("./assets", 'backgroundlvl2.png')).convert_alpha()
        self.bgimglvl2 = pygame.transform.scale(self.bgimglvl2, (self.width, self.height))

        self.bgimglvl3 = pygame.image.load(os.path.join("./assets", 'backgroundlvl3.png')).convert_alpha()
        self.bgimglvl3 = pygame.transform.scale(self.bgimglvl3, (self.width, self.height))

        self.bgimglvl4 = pygame.image.load(os.path.join("./assets", 'background.png')).convert_alpha()
        self.bgimglvl4 = pygame.transform.scale(self.bgimglvl4, (self.width, self.height))


    def drawbg(self, screen):
        if self.lvl == 1:
            screen.blit(self.bgimg, [0, 0])
        elif self.lvl == 2:
            screen.blit(self.bgimglvl2, [0, 0])
        elif self.lvl == 3:
            screen.blit(self.bgimglvl3, [0, 0])
        elif self.lvl == 4:
            screen.blit(self.bgimglvl4, [0, 0])

    def gameover(self, screen):
        # font = pygame.font.Font(os.path.join('./assets', 'square.ttf'), 56)
        gameover = self.font.render('GAME OVER press R to restart', True, (255, 0, 0))
        screen.blit(gameover, (400, 420))

    def victory(self, screen):
        # font = pygame.font.Font(os.path.join('./assets', 'square.ttf'), 56)
        victory = self.font.render('Victory press T to proceed to next level', True, (0, 255, 0))
        screen.blit(victory, (300, 400))

    def startscreen(self, screen):
       screen.blit(self.startimg, [0,0])
       # font = pygame.font.Font(os.path.join('./assets', 'square.ttf'), 50)
       menu = self.font.render('Welcome to 2d Divers! Press P to start!', True, (0, 0, 0))
       subtext = self.font.render('Travel across the world on your pirate ship', True, (0, 0, 0))
       subtext2 = self.font.render('and defeat enemies to find treasure!', True, (0, 0, 0))
       screen.blit(menu, (200, 255))
       screen.blit(subtext,(200, 355))
       screen.blit(subtext2, (200, 455))

    def bgnextlvl(self):
        self.lvl += 1

    def drawbonusitem(self, screen):
        bonusitem = pygame.image.load(os.path.join("./assets", 'treasure.png'))
        bonusitem = pygame.transform.scale(bonusitem, (80, 80))
        screen.blit(bonusitem, (self.bonusposx, self.bonusposy))

    def bonusitemmessage(self, screen):
        # font = pygame.font.Font(os.path.join('./assets', 'square.ttf'), 50)
        msg = self.font.render('Congratulations on winning the game! Press X to exit', True, (0, 255, 0))
        screen.blit(msg, (200, 255))


    #display fps for debugging purposes
    def displayfps(self, screen, clock):
        fps = self.font.render(f"FPS: {str(int(clock.get_fps()))}", True, [0, 0, 0])
        screen.blit(fps, (1000, 100))


class score():

    def __init__(self, font):
        self.score = 0
        self.font = font

    def updatescore(self, scoreamount):
        self.score += scoreamount

    def drawscore(self, screen):
        # font = pygame.font.Font(os.path.join('./assets', 'square.ttf'), 28)
        score = self.font.render(f'SCORE: {self.score}', True, (255, 0, 0))
        screen.blit(score, (50, 50))

class timer():

    def __init__(self, font):
        self.seconds = 0
        self.bonus = 100
        self.minutes = 0
        self.state = True
        self.font = font
        self.basetime = 200

    def bonusscore(self, seconds):
        self.basetime -= seconds
        return math.trunc(self.basetime) * self.bonus

    def drawtimer(self, screen, seconds):
        # font = pygame.font.Font(os.path.join('./assets', 'square.ttf'), 28)
        timer = self.font.render(f" Time in seconds: {math.trunc(seconds)}", True, (255, 0, 0))
        screen.blit(timer, (800, 50))










