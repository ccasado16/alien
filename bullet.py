import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """ "A class to manage ship's bullets"""

    def __init__(self, game_settings, screen, ship) -> None:
        """Create a bullet at the ship's current position"""

        super().__init__()
        self.screen = screen

        # Create a bullet and set correct position
        self.rect = pygame.Rect(
            0, 0, game_settings.bullet_width, game_settings.bullet_height
        )
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store the bullet's position as a decimal value
        self.y = float(self.rect.y)

        self.color = game_settings.bullet_color
        self.speed_factor = game_settings.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen"""

        # Update the decimal position of the bullet
        self.y -= self.speed_factor

        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""

        pygame.draw.rect(self.screen, self.color, self.rect)
