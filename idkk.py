import pygame
import random

pygame.init()
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Custom Character Game')
# Define colors
WHITE = (255, 255, 255)

# Load character images (replace with your own images)
RUNNING = [pygame.image.load('path/to/run1.png'), pygame.image.load('path/to/run2.png')]
JUMPING = pygame.image.load('path/to/jump.png')

# Set up the clock for controlling frame rate
clock = pygame.time.Clock()

class Character:
    def __init__(self):
        self.x = 80
        self.y = 310
        self.is_jumping = False
        self.jump_count = 10
        self.step_index = 0
        self.image = RUNNING[0]

    def draw(self, screen):
        if self.is_jumping:
            screen.blit(JUMPING, (self.x, self.y))
        else:
            self.image = RUNNING[self.step_index // 5]  # Change image for animation
            screen.blit(self.image, (self.x, self.y))
            self.step_index = (self.step_index + 1) % 10

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True

    def update(self):
        if self.is_jumping:
            if self.jump_count >= -10:
                neg = 1 if self.jump_count >= 0 else -1
                self.y -= (self.jump_count ** 2) * 0.5 * neg
                self.jump_count -= 1
            else:
                self.is_jumping = False
                self.jump_count = 10

def main():
    running = True
    character = Character()
    
    while running:
        clock.tick(30)  # Frame rate control
        screen.fill(WHITE)  # Clear screen

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Jump on spacebar press
                    character.jump()

        character.update()  # Update character position based on jump logic
        character.draw(screen)  # Draw the character on the screen

        pygame.display.update()  # Update the display

    pygame.quit()

if __name__ == "__main__":
    main()