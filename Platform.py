import pyglet # type: ignore
import random


class Platform():
    def __init__(self, x, y, w, h):
        self.image = pyglet.shapes.Rectangle(x, y, w, h, color=(0, 255, 0))
        self.rect = self.image.x, self.image.y, self.image.width, self.image.height

    def update(self):
        pass
    
    def draw(self):
        self.image.draw()
    
    @property    
    def left(self):
        return self.image.x

    @property
    def right(self):
        return self.image.x + self.image.width

    @property
    def top(self):
        return self.image.y + self.image.height

    @property
    def bottom(self):
        return self.image.y