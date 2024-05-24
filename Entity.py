import pygame 
import random

class Entity(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, game):
        super().__init__()
        self.gravity = 0.5  # Adjust gravity force
        self.image = pygame.Surface((20, 20))  # Create a surface for the entity
        self.image.fill((255, 255, 255))  # Fill the surface with white color (you can replace it with your image)
        self.rect = self.image.get_rect(topleft=(x, y))  # Set initial position
        self.velocity = pygame.math.Vector2(0, 0)
        self.game = game
        self.can_wall_hop = False
        self.wall_touching = False

    def draw(self):
        self.game.window.blit(self.image, self.rect)  # Blit the entity's image onto the game window

    def is_on_ground(self):
        # Check collision when moved down
        self.rect.y += 1
        on_ground = any(self.rect.colliderect(platform.rect) for platform in self.game.platform_array)
        self.rect.y -= 1
        
        if on_ground:
            self.can_wall_hop = True
        return on_ground
    

    def is_on_wall(self):
        # Check collision when moved left
        self.rect.x -= 1
        on_wall_left = any(self.rect.colliderect(platform.rect) for platform in self.game.platform_array)
        self.rect.x += 1  # Reset position

        # Check collision when moved right
        self.rect.x += 1
        on_wall_right = any(self.rect.colliderect(platform.rect) for platform in self.game.platform_array)
        self.rect.x -= 1  # Reset position

        # Return if either collision check is true
        return on_wall_left or on_wall_right

    def update(self,dt):
        if not self.is_on_ground():
            # add max fall cap
            if self.velocity.y < 10:  # Adjust the max fall velocity as needed
                self.velocity.y += self.gravity

        self.rect.x += self.velocity.x
        self.handle_collision(self.velocity.x, 0)
        self.rect.y += self.velocity.y
        self.handle_collision(0, self.velocity.y)

    def handle_collision(self, dx, dy):
        for platform in self.game.platform_array:
            if self.rect.colliderect(platform.rect):
                if dx > 0:  # Moving right
                    self.rect.right = platform.rect.left
                elif dx < 0:  # Moving left
                    self.rect.left = platform.rect.right
                elif dy > 0:  # Moving down
                    self.rect.bottom = platform.rect.top
                    self.velocity.y = 0
                    self.on_ground = True
                elif dy < 0:  # Moving up
                    self.rect.top = platform.rect.bottom
                    self.velocity.y = 0

    def random_movement(self):
        self.rect.x += random.randint(-1, 1)
        self.rect.y += random.randint(-1, 1)
