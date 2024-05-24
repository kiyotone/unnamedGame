import pygame # type: ignore
import sys
import random
from Platform import Platform
from Enemy import Enemy
from Player import Player
import os

class Game:
    def __init__(self):
        self.time_passed = 0
        self.window = pygame.display.set_mode((800, 600) )
        self.platform_array = []
        self.entities = []
        self.player = Player(400, 300, self)
        self.left_pressed = False
        self.right_pressed = False
        self.space_pressed = False
        
        self.platform_pattern = [
    "########################",
    "#                      #",
    "#                      #",
    "#                      #",
    "#                      #",
    "#                      #",
    "#                      #",
    "#                      #",
    "#                      #",
    "#                      #",
    "#                      #",
    "#                      #",
    "#                      #",
    "#                      #",
    "#                      #",
    "#                      #",
    "#                      #",
    "########################"
]
        
    def generate_entities(self):
        for i in range(1):
            x = random.randint(0, 750)  # Ensure platforms fit within the window width
            y = random.randint(0, 590)
            enemy = Enemy(x, y, self)
            self.entities.append(enemy)

    
    def generate_platforms(self):
        for y, row in enumerate(self.platform_pattern):
            for x, char in enumerate(row):
                if char == "#":
                    # Calculate the position and size of the platform
                    platform_size = 32
                    platform_x = x * platform_size
                    platform_y = y * platform_size
                    # Create a platform object and add it to the platform_array
                    platform = Platform(platform_x, platform_y, platform_size, platform_size, self)
                    self.platform_array.append(platform)
        
        for i in range(10):
            x = random.randint(0, 750)
            y = random.randint(0, 590)
            width = random.randint(32, 256)
            platform = Platform(x, y, width, 32, self)
            self.platform_array.append(platform)
            

    def draw(self):
        self.window.fill((0, 0, 0))
        self.player.draw()
        for platform in self.platform_array:
            platform.draw()
        
        for enemy in self.entities:
            enemy.draw()
    
    def update(self, dt):
        
        os.system('cls' if os.name == 'nt' else 'clear')

        
        self.time_passed += dt
        self.player.update(dt)
        for enemy in self.entities:
            enemy.update(dt)
    
    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.left_pressed = True
                if event.key == pygame.K_RIGHT:
                    self.right_pressed = True
                if event.key == pygame.K_SPACE:
                    self.player.jump()
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.left_pressed = False
                if event.key == pygame.K_RIGHT:
                    self.right_pressed = False
                
    
    def run(self):
        self.generate_platforms()
        self.generate_entities()
        
        clock = pygame.time.Clock()
        while True:
            self.get_events()
            dt = clock.tick(60) / 1000.0
            self.update(dt)
            self.draw()
            pygame.display.flip()