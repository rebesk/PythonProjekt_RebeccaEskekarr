import pygame
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


#game loop
running = True
while running:

    
    screen.blit(background, (0,0)) # material av blit https://dr0id.bitbucket.io/legacy/pygame_tutorial01.html 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()

    pygame.display.update()

pygame.exit()