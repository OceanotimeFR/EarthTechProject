import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 50

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Setup the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Turn-Based Game')

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface((GRID_SIZE, GRID_SIZE))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

# Create players
player1 = Player(RED, 0, 0)
player2 = Player(BLUE, GRID_SIZE, GRID_SIZE)

# Group players
players = pygame.sprite.Group()
players.add(player1)
players.add(player2)

# Turn management
turn = 0  # 0 for player1, 1 for player2

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            
            # Handle movement
            if turn == 0:
                if event.key == pygame.K_LEFT:
                    player1.rect.x -= GRID_SIZE
                elif event.key == pygame.K_RIGHT:
                    player1.rect.x += GRID_SIZE
                elif event.key == pygame.K_UP:
                    player1.rect.y -= GRID_SIZE
                elif event.key == pygame.K_DOWN:
                    player1.rect.y += GRID_SIZE
            elif turn == 1:
                if event.key == pygame.K_a:
                    player2.rect.x -= GRID_SIZE
                elif event.key == pygame.K_d:
                    player2.rect.x += GRID_SIZE
                elif event.key == pygame.K_w:
                    player2.rect.y -= GRID_SIZE
                elif event.key == pygame.K_s:
                    player2.rect.y += GRID_SIZE

            # Change turn
            turn = (turn + 1) % 2

    # Draw everything
    screen.fill(WHITE)
    players.draw(screen)
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
