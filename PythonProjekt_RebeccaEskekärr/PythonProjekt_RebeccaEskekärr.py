from turtle import width
import pygame
import random
from sys import exit

#run pygame
pygame.init()
#create a screen
screen = pygame.display.set_mode((800,570))
#Background
background = pygame.image.load('gamebackground.png')

#title and icon
pygame.display.set_caption('Jumping over') # Initial name of game
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

#gravity
gravity = 0.5

#Player
playerImage = pygame.image.load('warrior.png')
playerX = 200
playerY = 380
playerY_change = 0
playerX_change = 0

#Enemy
enemyImage = pygame.image.load('barrier.png')
enemyX = 736
enemyY = 380
enemies = [] # spawn of enemies
enemyX_change = -0.5

# Score (allt som har med score att göra) https://www.makeuseof.com/pygame-game-scores-displaying-updating/ 
score = 0

# Font for score 
font = pygame.font.Font('freesansbold.ttf', 32)

def enemy(x, y):
    for enemy_pos in enemies:
        screen.blit(enemyImage, enemy_pos) # draw enemy on image
        enemy_rect = enemyImage.get_rect() #googlat runt men denna var primär källa av get_rect(): https://www.pygame.org/docs/ref/surface.html#pygame.Surface.get_rect
        enemy_rect.x = enemy_pos[0]
        enemy_rect.y = enemy_pos[1]
        if enemy_rect.colliderect(player_rect):
            game_over()
        if enemy_rect.x + enemy_rect.width < 0:
            enemies.remove(enemy_pos)
            increment_score()

def player(x, y):
    screen.blit(playerImage, (x, y)) #draw player on image
    player_rect = playerImage.get_rect()
    player_rect.x = x
    player_rect.y = y
    return player_rect

def increment_score():
    global score
    score += 1

def show_score():
    score_text = font.render("Final Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (300, 250))
    pygame.display.update()

def game_over():
    global running
    running = False

ENEMY_EVENT = pygame.USEREVENT + 1 # https://coderslegacy.com/python/pygame-userevents/ and https://www.geeksforgeeks.org/how-to-add-custom-events-in-pygame/
pygame.time.set_timer(ENEMY_EVENT, 2000)

#game loop
running = True
while running:
    screen.blit(background, (0,0)) # material av blit https://dr0id.bitbucket.io/legacy/pygame_tutorial01.html 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and playerY_change == 0:
                playerY_change = 18
            if event.key == pygame.K_RIGHT:
                playerX_change = 2
            if event.key == pygame.K_LEFT:
                playerX_change = -2
       
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_LEFT:
                playerX_change = 0

        if event.type == ENEMY_EVENT:
            enemies.append([800, 380])


    playerX += playerX_change
    enemyX += enemyX_change

    #Gör att karaktären hoppar: källa från youtube där koden finns vid 15.56 från youtube videon https://www.youtube.com/watch?v=ZV8TNrwqG1Y
    if playerY_change > 0 or playerY < 380: 
        playerY -= playerY_change
        playerY_change -= gravity
    if playerY > 380:
        playerY = 380
    if playerY == 380 and playerY_change < 0:
        playerY_change = 0

    player_rect = player(playerX, playerY) #calling player

    for enemy_pos in enemies:
        enemy_pos[0] -= 2

    enemy(enemyX, enemyY)

    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()