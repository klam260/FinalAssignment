import pygame, sys, math, os
from surface import surface, score, timer
from player import player
from bullet import bullet
from enemy import enemy
from sound import sound

pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()

# for experimenting with timer

screen_width = 1600
screen_height = 900
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('2d-diver')

#attempting to render font here to see if it reduces lag.
font = pygame.font.Font(os.path.join('./assets', 'square.ttf'), 50)

#initiate background
background = surface(screen_width, screen_height, font)

#initiate player (health, level)
player = player(font)

#initiate enemy
enemy = enemy(screen_width, screen_height, font)

# initiate bullet
bullet = bullet(player.posx, player.posy)

#initiate score
score = score(font)

#initiate timer
timer = timer(font)

#initiate sound
sound = sound()

#various states used to manage in game
gameover = False
victory = False
startingscreen = True #triggers at the beginning
scoreupdated = False #might be useless
currentlevel = 1 #used for keeping track of stages
bonusscreen = False #triggers once reach level 4

#for starting screen loop

while startingscreen:

    background.startscreen(screen)

    #initiate fps here
    background.displayfps(screen, clock)

    for event in pygame.event.get():
        sound.startscreenbgm.play()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                startingscreen = False

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()
    pygame.event.pump()


#for making a timer in game
initialtime = pygame.time.get_ticks() #initiates the timer first

#main game loop
while True:

    #used as the timer for in game, only triggers when true. Once game over happens timer.state is set to false and we can retrieve the seconds that passed
    if timer.state:
        seconds = (pygame.time.get_ticks() - initialtime)/1000

    # initiates the background for the screen, must be put into while loop to be shown on screen
    background.drawbg(screen)

    # draws player to background and displays hp
    player.drawplayer(screen)
    player.displayhp(screen)

    # draws enemy to screen and displays hp
    enemy.drawenemy(screen)
    enemy.displayhp(screen)

    # draws score to screen
    score.drawscore(screen)

    # draws timer to screen
    timer.drawtimer(screen, seconds)

    #initiate FPS here for measurement
    background.displayfps(screen, clock)

    enemy.enemymovement(player.posy)

    # for character movements
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player.playermoveup(screen_height)
        # bullet.updateposition(player.posx, player.posy)

    if keys[pygame.K_s]:
        player.playermovedown(screen_height)
        # bullet.updateposition(player.posx, player.posy)

    if keys[pygame.K_a]:
        player.playermoveleft(screen_width)
        # bullet.updateposition(player.posx, player.posy)

    if keys[pygame.K_d]:
        player.playermoveright(screen_width)
        # bullet.updateposition(player.posx, player.posy)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if bullet.state == 'ready':
                    bullet.state = 'fire'
                    bullet.bulletposx = player.posx
                    bullet.bulletposy = player.posy
                    sound.cannon.play()#plays everytime a bullet is fired from player
            if victory:
                if event.key == pygame.K_t:
                    if(currentlevel < 4):
                        background.bgnextlvl()  # upgrades to the next level for background
                        player.playernextlvl()
                        player.playerrestart() #resets position and hp for next level
                        enemy.enemyrestart(screen_height) #resets position and health of enemy
                        enemy.enemynextlvl() #upgrades enemy to scale difficulty
                        # enemy.drawenemy(screen) #draws enemy to screen after applying above
                        currentlevel += 1 #once it reaches level 4, the bonus screen should appear
                        victory = False


            if gameover:
                if event.key == pygame.K_r:
                    background.drawbg(screen) #redraws background
                    player.playerrestart(screen) #calls method to recenter player
                    enemy.enemyrestart(screen_height) #calls method to recenter enemy
                    gameover = False #change gameover back to False to prevent loop
                    timer.state = True

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

      # bullet movement, if state is fire in bullet object, proceed to calculate movements through while loop
    if bullet.state == 'fire':
        if bullet.bulletposx >= screen_width:
            bullet.state ='ready'
            bullet.bulletposx = -100
            bullet.bulletposy = -100
        bullet.fire(screen)
        bullet.bulletposx += bullet.bulletspeed


    #for enemy firing, enemy can fire bullet, returns true if enemy kills player
    if enemy.enemyfire(screen, player.posx, player.posy, player):
        gameover = True

    #if gameover state becomes true, draw the following onto the screen, same with victory
    if gameover:
        player.removeplayer() #sets player off of screen
        enemy.removeenemy()#sets position of enemy in different position
        timer.state = False #stops timer
        background.gameover(screen) #draws game over screen

    if victory:
        timer.state = False #stops timer
        background.victory(screen)

    #responsible for the damage calculations on the enemy side. If enemy hp hits zero, victory becomes true and loop will blit background
    if bullet.enemyCollision(enemy.posx, enemy.posy, bullet.bulletposx, bullet.bulletposy):
        if enemy.hp >= 1:
            enemy.hp -= player.dmg
            if enemy.hp <= 0:
                enemy.removeenemy()
                player.removeplayer()
                score.updatescore(timer.bonusscore(seconds)) #updates score based on time
                victory = True

    #if current level is 4, set bonusscreen to true and break out of while loop to proceed to bonus screen
    if currentlevel == 4:
        bonusscreen = True
        player.playerrestart()
        break

    clock.tick(60)
    pygame.event.pump()
    pygame.display.update()

#States here
displaywinner = False

#loop for ending screen
while bonusscreen:

    background.drawbg(screen)
    player.drawplayer(screen)
    background.drawbonusitem(screen)
    score.drawscore(screen)

    if bullet.enemyCollision(background.bonusposx, background.bonusposy, bullet.bulletposx, bullet.bulletposy): #althought it's called enemy collision the parameters are changed to include the coordinates of the treasure chest
        score.updatescore(100000)  # provide bonus score after hitting treasure box
        bullet.bulletposx = 2000
        displaywinner = True

        # for character movements
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player.playermoveup(screen_height)

    if keys[pygame.K_s]:
        player.playermovedown(screen_height)

    if keys[pygame.K_a]:
        player.playermoveleft(screen_width)

    if keys[pygame.K_d]:
        player.playermoveright(screen_width)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x and displaywinner:
                exit()
            if event.key == pygame.K_SPACE:
                bullet.fire(screen)
                sound.cannon.play()  # plays everytime a bullet is fired from player

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    # if bullet.state == 'fire':
    #     bullet.fire(screen)
    #     bullet.bulletposx += bullet.bulletspeed

    if displaywinner:
        background.bonusitemmessage(screen)
        player.removeplayer()

    # bullet movement, if state is fire in bullet object, proceed to calculate movements through while loop
    if bullet.state == 'fire':
        if bullet.bulletposx >= screen_width:
            bullet.state ='ready'
            bullet.bulletposx = -100
            bullet.bulletposy = -100
        bullet.fire(screen)
        bullet.bulletposx += bullet.bulletspeed

    pygame.display.update()
    pygame.event.pump()



