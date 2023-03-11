import sys

import pygame

from bullet import Bullet
from enemy import Enemy


def check_keydown_events(event, game_settings, screen, ship, bullets):
    """Respond to keypresses"""

    if event.key == pygame.K_q:  # Q key
        sys.exit()
    elif event.key == pygame.K_LEFT:  # Left arrow key
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


def get_number_enemies_x(game_settings, enemy_width):
    """Determine the number of enemies that fit in a row"""

    available_space_x = game_settings.screen_width - (2 * enemy_width)
    number_enemies_x = int(available_space_x / (2 * enemy_width))

    return number_enemies_x


def create_enemy(game_settings, screen, enemies, enemy_number):
    """Create an enemy and place it in the row"""

    enemy = Enemy(game_settings, screen)
    enemy_width = enemy.rect.width
    enemy.x = enemy_width + 2 * enemy_width * enemy_number
    enemy.rect.x = enemy.x
    enemies.add(enemy)


def create_fleet(game_settings, screen, enemies):
    """Create a enemy fleet"""

    # Create an enemy and find the number of enemies that fits in a row
    # Space between each enemy is equal to one enemy width
    enemy = Enemy(game_settings, screen)
    number_enemies_x = get_number_enemies_x(game_settings, enemy.rect.width)

    # Create the first row of enemies
    for enemy_number in range(number_enemies_x):
        create_enemy(game_settings, screen, enemies, enemy_number)


def update_screen(game_settings, screen, ship, bullets, enemies):
    """Update images on the screen and flip to the new screen"""

    # Redraw the screen during each pass through the loop
    screen.fill(game_settings.bg_color)

    # Draw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    enemies.draw(screen)

    pygame.display.flip()
