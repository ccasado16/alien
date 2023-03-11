import pygame
from pygame.sprite import Group

import game_functions as gf
from settings import Settings
from ship import Ship


def run_game():
    pygame.init()

    game_settings = Settings()

    screen = pygame.display.set_mode(
        (game_settings.screen_width, game_settings.screen_height)
    )
    pygame.display.set_caption("Alien")

    # Make a ship, a group of bullets and a group of enemies
    ship = Ship(game_settings, screen)
    bullets = Group()
    enemies = Group()

    # Create ememy fleet
    gf.create_fleet(game_settings, screen, enemies)

    while True:
        gf.check_events(game_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(game_settings, screen, ship, bullets, enemies)


run_game()
