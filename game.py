import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pygame Background Example')

# Load a background image
background = pygame.image.load('background.jpg')  # Replace with your image file path

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with the background image
    screen.blit(background, (0, 0))  # Blit the background at the top-left corner (0, 0)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

