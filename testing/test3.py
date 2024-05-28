import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Invisible Buttons Example")

# Define the invisible button area
button_rect = pygame.Rect(100, 100, 200, 100)  # (x, y, width, height)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse click is within the button area
            if button_rect.collidepoint(event.pos):
                print("Invisible Button Clicked!")

    # Fill the screen with a color
    screen.fill((255, 255, 255))

    # Draw the invisible button (for demonstration purposes)
    #^ pygame.draw.rect(screen, (0, 0, 0), button_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
