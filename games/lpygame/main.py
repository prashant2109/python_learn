import pygame

# Initialize the pygame
pygame.init()

# create the screens
screen = pygame.display.set_mode((800, 600))

# Caption and Icon
pygame.display.set_caption(" Space Invaders ")
icon =  pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480

def player():
    screen.blit(playerImg, (playerX, playerY))

# game loop
running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player()
    pygame.display.update()




             