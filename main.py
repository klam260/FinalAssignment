import pygame, sys, math
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


#initiate background
background = surface(screen_width, screen_height)

#initiate player (health, level)
player = player()

#initiate bullet
bullet = bullet(player.posx, player.posy)

#initiate enemy
enemy = enemy(screen_width, screen_height)

#initiate score
score = score()

#initiate timer
timer = timer()

#initiate sound
sound = sound()

#various states used to manage in game
gameover = False
victory = False
startingscreen = True
scoreupdated = False

#for starting screen

while startingscreen:

    background.startscreen(screen)

    for event in pygame.event.get():
        sound.startscreenbgm.play()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                startingscreen = False

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()


#for making a timer in game
initialtime = pygame.time.get_ticks() #initiates the timer first

#main game loop
while True:
    #used as the timer for in game, only triggers when true. Once game over happens timer.state is set to false and we can retrieve the seconds that passed
    if timer.state:
        seconds = (pygame.time.get_ticks() - initialtime)/1000

    #initiates the background for the screen
    background.drawbg(screen)

    #draws player to background and displays hp
    player.drawplayer(screen)
    player.displayhp(screen)

    #draws enemy to screen and displays hp
    enemy.drawenemy(screen)
    enemy.displayhp(screen)

    #draws score to screen
    score.drawscore(screen)

    # draws timer to screen
    timer.drawtimer(screen, seconds)

    #managing sound effects and music

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet.fire(screen, screen_width, player.posx, player.posy)
            if victory:
                if event.key == pygame.K_t:
                    background.drawbg(screen)
                    player.playernextlvl()
                    player.drawplayer(screen)
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

    #for character movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player.playermoveup(screen_height)

    if keys[pygame.K_s]:
        player.playermovedown(screen_height)

    if keys[pygame.K_a]:
        player.playermoveleft(screen_width)

    if keys[pygame.K_d]:
        player.playermoveright(screen_width)

    enemy.enemymovement(player.posy,screen)


      # bullet movement, if state is fire in bullet object, proceed to calculate movements through while loop
    if bullet.state == 'fire':
        bullet.fire(screen, screen_width, player.posx, player.posy)
        bullet.bulletposx += bullet.bulletspeed


    #for enemy firing, enemy can fire bullet but bullet collision is not properly calculated. returns true if enemy kills player
    if enemy.enemyfire(screen, player.posx, player.posy, player):
        gameover = True

    #if gameover state becomes true, draw the following onto the screen, same with victory
    if gameover:
        player.removeplayer()
        enemy.removeenemy()
        timer.state = False
        background.gameover(screen)

    if victory:
        timer.state = False
        background.victory(screen)
        scoreupdated = True

    if scoreupdated:
        score.updatescore(timer.bonusscore(seconds))
        scoreupdated = False

    #responsible for the damage calculations on the enemy side. If enemy hp hits zero, victory becomes true and loop will blit background
    if bullet.enemyCollision(enemy.posx, enemy.posy, bullet.bulletposx, bullet.bulletposy):
        if enemy.hp >= 1:
            enemy.hp -= player.dmg
            if enemy.hp <= 0:
                enemy.removeenemy()
                player.posx = 3000
                victory = True



    clock.tick(60)
    pygame.event.pump()
    pygame.display.update()



