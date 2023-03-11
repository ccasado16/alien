import sys

import pygame

from bullet import Bullet


def check_keydown_events(event, game_settings, screen, ship, bullets):
    """Respond to keypresses"""

    if event.key == pygame.K_LEFT:  # Left arrow key
        ship.moving_left = True
    elif event.key == pygame.K_RIGHT:  # Right arrow key
        ship.moving_right = True
    elif event.key == pygame.K_SPACE:  # Spacebar key
        fire_bullet(game_settings, screen, ship, bullets)


def check_keyup_events(event, ship):
    """Respond to key releases"""

    if event.key == pygame.K_LEFT:  # Left arrow key
        ship.moving_left = False
    elif event.key == pygame.K_RIGHT:  # Right arrow key
        ship.moving_right = False


def check_events(game_settings, screen, ship, bullets):
    """Respond to keypresses and mouse events"""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def fire_bullet(game_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet"""

    # Create bullet and add it to the bullets group
    if len(bullets) < game_settings.bullets_allowed:
        new_bullet = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet)


def update_bullets(bullets):
    """Update bullets' position and deleting old ones"""

    # Update bullets' position
    bullets.update()

    # Remove bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def update_screen(game_settings, screen, ship, bullets):
    """Update images on the screen and flip to the new screen"""

    # Redraw the screen during each pass through the loop
    screen.fill(game_settings.bg_color)

    # Draw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()

    pygame.display.flip()
