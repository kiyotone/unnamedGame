import pyglet  # type: ignore
from Entity import Entity
import random


class Enemy(Entity):
    def __init__(self, x: int, y: int, game):
        super().__init__(x, y, game)
        
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)

        # Set the color of the image using the generated values
        
        self.image = pyglet.shapes.Rectangle(x, y, 20, 20, color=(0, 255, 0))
        self.image.color = (red, green, blue)
        self.velocity = pyglet.math.Vec2(0, 0)
    
    def draw(self):
        self.image.draw()
    
    def update(self, dt):
        super().update(dt)
        #check if a ceratin time has passed using dt
        
        if self.game.time_passed % 1 < 0.1:
            self.velocity.x = 20 * random.randint(-1, 1)

            
        self.image.x += self.velocity.x * dt