import pygame
from Entity import Entity

class Player(Entity):
    def __init__(self, x: int, y: int, game, *groups):
        super().__init__(x, y, game , groups)
        self.jump_strength = 10  # Jump force
        self.jump_count = 0  # Number of jumps made
        self.jump_pressed = False  # If the jump key is pressed
        self.image = pygame.Surface((20, 20))  # Create a surface for the player's image
        self.image.fill((255, 0, 0))  # Fill the surface with red color
        self.rect = self.image.get_rect(topleft=(x, y))  # Set initial position
        self.hit_rect = pygame.Rect(0, 0, 20, 20)
        self.facing_left = False
        
        # Animations
        self.idle_frames = []
        self.run_frames = []
        self.jump_frames = []
        self.fall_frames = []

        self.load_images()
        self.current_frame = 0
        self.time_since_last_frame = 0
        self.frame_duration = 0.1
        self.current_animation = self.idle_frames
        
        self.velocity = pygame.math.Vector2(0, 0)
        self.vision_range = 100
        
    def draw(self):
        self.game.window.blit(self.image, self.rect)
        pygame.draw.rect(self.game.window, (0, 255, 0), self.hit_rect, 2)
        
        # self.draw_vision()
        
        
    def load_images(self):
        # Load each image
        for i in range(4):
            image = pygame.image.load(f'assets/idle/adventurer{i+1}.png').convert_alpha()
            self.idle_frames.append(image)
        
        for i in range(6):
            image = pygame.image.load(f'assets/run/adventurer{i+1}.png').convert_alpha()
            self.run_frames.append(image)
        
        for i in range(4):
            image = pygame.image.load(f'assets/jump/adventurer{i+1}.png').convert_alpha()
            self.jump_frames.append(image)
        
        for i in range(2):
            image = pygame.image.load(f'assets/fall/adventurer{i+1}.png').convert_alpha()
            self.fall_frames.append(image)
        
        self.rect = self.idle_frames[0].get_rect(topleft=(self.rect.x, self.rect.y))
        # Set the hit rect to match the player's rect
        self.hit_rect = self.rect.copy()

        
        
    def jump(self):
        if self.is_on_ground():  # First jump            
            self.velocity.y = -self.jump_strength
            self.jump_count = 1
        elif self.can_wall_hop and self.is_on_wall():  # Wall hop
            self.velocity.y = -self.jump_strength
            self.velocity.x = -self.velocity.x  # Reverse direction
        elif self.jump_count < 2:  # Double jump
            self.velocity.y = -self.jump_strength
            self.jump_count += 1
            
        
        
    def player_input(self):
        self.velocity.x = 0
        if self.game.left_pressed:
            self.velocity.x = -3
            self.facing_left = True
        if self.game.right_pressed:
            self.velocity.x = 3
            self.facing_left = False
            
        
    def handle_collision(self, dx, dy):
        return super().handle_collision(dx, dy)
        
    def update(self, dt):
        super().update(dt)
        
        self.player_input()
        
        
        if self.is_on_ground():
            self.jump_count = 0  # Reset jump count when on the ground
        
        # Update animation
        self.animate(dt)
        
        self.rect.x += self.velocity.x * dt
        self.handle_collision(self.velocity.x, 0)
        self.rect.y += self.velocity.y * dt
        self.handle_collision(0, self.velocity.y)
        
        self.hit_rect.topleft = self.rect.topleft
        
        # self.check_platform_ahead()

   
    
    def animate(self,dt):
        self.time_since_last_frame += dt
              
        if self.time_since_last_frame >= self.frame_duration:
            self.current_frame += 1
            self.time_since_last_frame = 0
        
        if self.velocity.x != 0:
            self.current_animation = self.run_frames
        else:
            self.current_animation = self.idle_frames
        
        if self.velocity.y < 0:
            self.current_animation = self.jump_frames
        elif self.velocity.y > 0:
            self.current_animation = self.fall_frames
        
        
        # Update image based on animation
        if self.current_frame >= len(self.current_animation):   
            self.current_frame = 0
        self.image = self.current_animation[self.current_frame] # Set the current frame
        
        if self.facing_left:
            self.image = pygame.transform.flip(self.image, True, False)
        else:
            self.image = pygame.transform.flip(self.image, False, False)

