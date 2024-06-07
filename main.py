import pygame
import sys
from functions import * ; from colors import * ; from ui import *

# Initialize Pygame 
pygame.init()

icon = pygame.image.load("images/greencity-transformed.png")
pygame.display.set_caption("GREENCITY : For a new home") ; pygame.display.set_icon(icon)

if __name__ == "__main__": 
    game = RunGame()
    game.run_game()
