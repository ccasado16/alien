import pygame


class Ship:
    """Manage ship's behavior"""

    def __init__(self, game_settings, screen) -> None:
        """Initialize user's ship and set its starting position"""

        # Movement flags
        self.moving_right = False
        self.moving_left = False

        self.screen = screen
        self.game_settings = game_settings

        # Load ship's image and resize it
        self.image = pygame.image.load("images/rocket.png")
        width, height = self.image.get_size()
        self.image = pygame.transform.scale(
            self.image, ((width * 0.15), (height * 0.15))
        )

        # Get Rects
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center
        self.center = float(self.rect.centerx)

    def update(self):
        """Update ship's position based on the movement flag"""

        if self.moving_right:
            self.center += self.game_settings.ship_speed_factor
        if self.moving_left:
            self.center -= self.game_settings.ship_speed_factor

        # Update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location"""

        self.screen.blit(self.image, self.rect)
