import pygame
from pygame.sprite import Sprite


class Enemy(Sprite):
    """Represents a single enemy in the fleet"""

    def __init__(self, game_settings, screen) -> None:
        """Initialize the enemy and set its starting position"""

        super(Enemy, self).__init__()
        self.screen = screen
        self.game_settings = game_settings

        # Load the enemy image and resize it
        self.image = pygame.image.load("images/enemy.png")
        width, height = self.image.get_size()
        self.image = pygame.transform.scale(
            self.image, ((width * 0.08), (height * 0.08))
        )

        self.rect = self.image.get_rect()

        # Start each new enemy near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the enemy's exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the enemy at its current location"""

        self.screen.blit(self.image, self.rect)
