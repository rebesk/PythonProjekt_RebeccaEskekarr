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
enemyX_change = -0.3

def enemy(x, y):
    screen.blit(enemyImage, (x, y)) # draw enemy on image

def player(x, y):
    screen.blit(playerImage, (x, y)) #draw player on image

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

 
    enemy(enemyX, enemyY)
    player(playerX, playerY) #calling player
    pygame.display.update()

pygame.exit()