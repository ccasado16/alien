import pygame
from pygame.sprite import Group

import game_functions as gf
from enemy import Enemy
from settings import Settings
from ship import Ship


def run_game():
    pygame.init()

    game_settings = Settings()

    screen = pygame.display.set_mode(
        (game_settings.screen_width, game_settings.screen_height)
    )
    pygame.display.set_caption("Alien")

    # Make the ship
    ship = Ship(game_settings, screen)
    # Make a group to store bullets
    bullets = Group()
    # Make an enemy
    enemy = Enemy(game_settings, screen)

    while True:
        gf.check_events(game_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(game_settings, screen, ship, bullets, enemy)


run_game()
