import sys, pygame

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()
# Set up the drawing window

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))
    surf = pygame.Surface((50,50))

    #color
    surf.fill((0,0,0)) 
    rect = surf.get_rect()


    #screen.blit(surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))        
    surf_center = (
        (SCREEN_WIDTH-surf.get_width()) /2,
        (SCREEN_HEIGHT-surf.get_height()) /2
    )

    screen.blit(surf, surf_center)

    

# Define a Player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'


    # Flip the display
pygame.display.flip()

# Done! Time to quit.
pygame.quit()