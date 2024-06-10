import pygame 
import random

class Entity(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, game , *groups):
        super().__init__(groups)
        self.gravity = 0.5  # Adjust gravity force
        self.image = pygame.Surface((20, 20))  # Create a surface for the entity
        self.image.fill((255, 255, 255))  # Fill the surface with white color (you can replace it with your image)
        self.rect = self.image.get_rect(topleft=(x, y))  # Set initial position
        self.velocity = pygame.math.Vector2(0, 0)
        self.game = game
        self.can_wall_hop = False
        self.wall_touching = False

    def draw_vision(self):
        vision_circle = pygame.Surface((self.vision_range * 2, self.vision_range * 2), pygame.SRCALPHA)
        pygame.draw.circle(vision_circle, (255, 0, 0, 100), (self.vision_range, self.vision_range), self.vision_range)
        
        vision_circle2 = pygame.Surface((self.vision_range * 2, self.vision_range * 2), pygame.SRCALPHA)
        pygame.draw.circle(vision_circle2, (255, 255, 0, 100), (self.vision_range, self.vision_range), self.vision_range - 10)

        # Draw the vision circle
        self.game.window.blit(vision_circle, vision_circle.get_rect(center=self.rect.center))
        self.game.window.blit(vision_circle2, vision_circle2.get_rect(center=self.rect.center))
    

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

    def is_wall_ahead(self, rect, tolerance=10):
        # Find the closest x-coordinate on the platform's rectangle to the enemy's center
        closest_x = max(rect.left, min(self.rect.centerx, rect.right))
        closest_y = max(rect.top, min(self.rect.centery, rect.bottom))
        
        # Calculate horizontal the distance from the closest point to the enemy's center
        
        #check if is in direction of movement
        if self.facing_left:
            if closest_x < self.vision_range + self.rect.centerx:
                if rect.top < self.rect.bottom and rect.bottom > self.rect.top:
                    return False 
                return True
        else:
            if closest_x > self.rect.centerx:
                return True
            
                
    def check_platform_ahead(self):
        for platform in self.game.platform_array:
            if self.is_wall_ahead(platform.rect):
                print("wall ahead")    
                return True
        return False            
    