import random
import sys
import pygame
from pygame.locals import *

# Global Variables for the game 

FPS = 32
SCREENWIDTH = 289GAME_SPRITES['numbers'] = (
    pygame.image.load('/gallery/sprites/0.png').convert_alpha(),
    pygame.image.load('/gallery/sprites/0.pn1').convert_alpha(),
    pygame.image.load('/gallery/sprites/0.pn2').convert_alpha(),
    pygame.image.load('/gallery/sprites/0.pn3').convert_alpha(),
    pygame.image.load('/gallery/sprites/0.pn4').convert_alpha(),
    pygame.image.load('/gallery/sprites/0.png').convert_alpha(),
    pygame.image.load('/gallery/sprites/0.png').convert_alpha(),
    pygame.image.load('/gallery/sprites/0.png').convert_alpha(),
    pygame.image.load('/gallery/sprites/0.png').convert_alpha(),
    pygame.image.load('/gallery/sprites/0.png').convert_alpha(),
)
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS  = {}
PLAYER = '/gallery/sprites/bird.png'
BACKGROUND = '/gallery/sprites/background.png'
PIPE = '/gallery/sprites/pipe.png'

if __name__ == '__main__':
    # This will be our main point from out game will start

    pygame.init() # Initialize all pygame modules
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_cation('Flappy Bird')
    GAME_SPRITES['numbers'] = (
        pygame.image.load('/gallery/sprites/0.png').convert_alpha(),
        pygame.image.load('/gallery/sprites/1.png').convert_alpha(),
        pygame.image.load('/gallery/sprites/2.png').convert_alpha(),
        pygame.image.load('/gallery/sprites/3.png').convert_alpha(),
        pygame.image.load('/gallery/sprites/4.png').convert_alpha(),
        pygame.image.load('/gallery/sprites/5.png').convert_alpha(),
        pygame.image.load('/gallery/sprites/6.png').convert_alpha(),
        pygame.image.load('/gallery/sprites/7.png').convert_alpha(),
        pygame.image.load('/gallery/sprites/8.png').convert_alpha(),
        pygame.image.load('/gallery/sprites/9.png').convert_alpha(),
    )

    GAME_SPRITES['message'] = pygame.image.load('/gallery/sprites/message.png').convert_alpha()



