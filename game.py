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
background = pygame.image.load('Screenshot_25-11-2024_95359_wallpaperaccess.com.jpeg')  # Replace with your image file path

# Load the background music
pygame.mixer.music.load("audio.mp3")  # Replace with your audio file path
pygame.mixer.music.play(-1)  # Loop the background music indefinitely

# Load sound effects
jump_sound = pygame.mixer.Sound("jump.wav")  # Replace with your jump sound file path

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Play the jump sound when space is pressed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            jump_sound.play()

    # Fill the screen with the background image
    screen.blit(background, (0, 0))  # Blit the background at the top-left corner (0, 0)

    # Update the display
    pygame.display.flip()

# Stop music and quit Pygame
pygame.mixer.music.stop()
pygame.quit()
sys.exit()
