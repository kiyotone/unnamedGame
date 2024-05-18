import pyglet # type: ignore
import sys
import random
from Platform import Platform
from Entity import Entity
from Player import Player

class Game:
    def __init__(self):
        self.window = pyglet.window.Window(800, 600) 
        self.platform_array = []
        self.entities = []
        self.player = Player(400, 300, self)
        self.window.push_handlers(self)  # Register the Game instance as the event handler
        self.window.push_handlers(self.player)  # Register the Player instance as the event handler
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
        for i in range(20):
            x = random.randint(0, 750)  # Ensure platforms fit within the window width
            y = random.randint(0, 590)
            entity = Entity(x, y, self)
            self.entities.append(entity)

    
    def generate_platforms(self):
        for y, row in enumerate(self.platform_pattern):
            for x, char in enumerate(row):
                if char == "#":
                    # Calculate the position and size of the platform
                    platform_size = 32
                    platform_x = x * platform_size
                    platform_y = y * platform_size
                    # Create a platform object and add it to the platform_array
                    platform = Platform(platform_x, platform_y, platform_size, platform_size)
                    self.platform_array.append(platform)
        
        for i in range(10):
            x = random.randint(0, 750)
            y = random.randint(0, 590)
            width = random.randint(32, 128)
            platform = Platform(x, y, width, 32)
            self.platform_array.append(platform)
            

    def on_draw(self):
        self.window.clear()
        self.player.draw()
        for platform in self.platform_array:
            platform.draw()
        
        for entity in self.entities:
            entity.draw()
    
    def update(self, dt):
        self.player.update(dt)
        for entity in self.entities:
            entity.update(dt)
        
    def run(self):
        self.generate_platforms()
        self.generate_entities()
        pyglet.clock.schedule_interval(self.update, 1/60)
        pyglet.app.run()