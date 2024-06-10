import pygame # type: ignore
import random


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h ,game , *groups):
        super().__init__(groups)
        self.image = pygame.Surface((w, h))
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        self.image.fill((red, green, blue))

        self.rect = self.image.get_rect(topleft=(x, y))
        self.game = game
   
    def update(self):
        pass
    
    def draw(self):
        self.game.window.blit(self.image, self.rect)
