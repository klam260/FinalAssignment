import pygame, sys
from surface import background
from player import player
from bullet import bullet
from enemy import enemy

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

clock = pygame.time.Clock()

# for experimenting with timer

screen_width = 1600
screen_height = 900
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('2d-diver')


#initiate background
background = background('background.png', screen_width, screen_height)

#initiate player (health, level)
player = player(10, 1)

#initiate bullet
bullet = bullet(player.posx, player.posy)

#initiate enemy
enemy = enemy(screen_width, screen_height)

#initiate timer
current_time = 0


while True:

    #initiates the background for the screen
    background.drawbg(screen)

    #draws player to background
    player.drawplayer(screen)

    #draws enemy to screen
    enemy.drawenemy(screen)



    #for character movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player.playermovey(-1, screen_height)

    if keys[pygame.K_s]:
        player.playermovey(1, screen_height)

    if keys[pygame.K_a]:
        player.playermovex(-1, screen_width)

    if keys[pygame.K_d]:
        player.playermovex(1, screen_width)

    enemy.enemymovement(player.posy,screen)


    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet.fire(screen, screen_width, player.posx, player.posy)

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

      # bullet movement, if state is fire in bullet object, proceed to calculate movements through while loop
    if bullet.state == 'fire':
        bullet.fire(screen, screen_width, player.posx, player.posy)
        bullet.bulletposx += bullet.bulletspeed


    #for enemy firing, currently stuck in an infinite loop freezing the game.
    enemy.enemyfire(screen)
    bullet.isCollision(enemy.posx, enemy.posy, bullet.bulletposx, bullet.bulletposy)




    clock.tick(60)
    pygame.event.pump()
    pygame.display.update()



