import sys

import pygame


def check_events(ship):
    """Respond to keypresses and mouse events"""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Move ship to the right
                ship.rect.centerx += 1
            if event.key == pygame.K_LEFT:
                # Move ship to the left
                ship.rect.centerx -= 1


def update_screen(game_settings, screen, ship):
    """Update images on the screen and flip to the new screen"""

    # Redraw the screen during each pass through the loop
    screen.fill(game_settings.bg_color)
    ship.blitme()

    pygame.display.flip()
