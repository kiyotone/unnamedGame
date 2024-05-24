import pygame # type: ignore
import random


class Platform():
    def __init__(self, x, y, w, h ,game):
        self.image = pygame.Surface((w, h))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.game = game
   
    def update(self):
        pass
    
    def draw(self):
        self.game.window.blit(self.image, self.rect)
