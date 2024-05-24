import pygame
import random
import math

from Entity import Entity  # Assuming Entity is defined in a separate file

class Enemy(Entity):
    def __init__(self, x: int, y: int, game):
        super().__init__(x, y, game)

        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        self.facing_left = False

        self.vision_range = 100

        self.image = pygame.Surface((20, 20))  # Create a surface for the enemy's image
        self.image.fill((0, 255, 0))  # Fill the surface with green color
        self.image.set_colorkey((0, 0, 0))  # Set black color as transparent

        # Create the vision circle surface
        
    def draw(self):
        # Draw the enemy image
        self.game.window.blit(self.image, self.rect.topleft)

        vision_circle = pygame.Surface((self.vision_range * 2, self.vision_range * 2), pygame.SRCALPHA)
        pygame.draw.circle(vision_circle, (255, 0, 0, 100), (self.vision_range, self.vision_range), self.vision_range)

        # Draw the vision circle
        self.game.window.blit(vision_circle, vision_circle.get_rect(center=self.rect.center))


    def update(self, dt):
        super().update(dt)

        if self.velocity.x < 0:
            self.facing_left = True
            
        else:
            self.facing_left = False
            
        if self.game.time_passed % 1 < 0.1:
            if self.is_within_vision(self.game.player.rect):
                if self.rect.x < self.game.player.rect.x:
                    self.velocity.x = 1
                else:
                    self.velocity.x = -1
            else:
                self.velocity.x = 1 * random.randint(-1, 1)
        
        self.rect.x += self.velocity.x * dt
        # print(self.is_within_vision(self.game.player.rect))


    def is_within_vision(self, rect):
        # Calculate the closest point on the rectangle to the enemy's center
        closest_x = max(rect.left, min(self.rect.centerx, rect.right))
        closest_y = max(rect.top, min(self.rect.centery, rect.bottom))

        # Calculate the distance from the closest point to the enemy's center
        distance = math.hypot(self.rect.centerx - closest_x, self.rect.centery - closest_y)
        return distance < self.vision_range