import pygame
from pygame.locals import * ; from colors import * ; from testing.roymain import * ; from functions import * ; from ui import *

pygame.init()

icon = pygame.image.load("images/greencity-transformed.png")
pygame.display.set_caption("GREENCITY : For a new home") ; pygame.display.set_icon(icon)

#! Main Game
if __name__ == "__main__":
    game = RunGame()
    game.run_game()