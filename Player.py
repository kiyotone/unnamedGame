import pyglet  # type: ignore
from Entity import Entity

class Player(Entity):
    def __init__(self, x: int, y: int, game):
        super().__init__(x, y, game)
        self.jump_strength = 200  # Jump force
        self.jump_count = 0  # Number of jumps made
        self.jump_pressed = False  # If the jump key is pressed
        self.image.color = (255, 0, 0)  # Change the player color to red
        self.move_left = False
        self.move_right = False
    
    def draw(self):
        super().draw()
    
    def collide(self, dx: int, dy: int):
        return super().collide(dx, dy)
    
    def is_on_ground():
        super().is_on_ground()
    
    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.SPACE:
            self.jump()
        if symbol == pyglet.window.key.LEFT:
            self.move_left = True  # Increase velocity towards left
        if symbol == pyglet.window.key.RIGHT:
            self.move_right = True
            
    def on_key_release(self, symbol, modifiers):
        if symbol == pyglet.window.key.LEFT:
            self.move_left = False
        if symbol == pyglet.window.key.RIGHT:
            self.move_right = False
        
    def jump(self):
        if self.is_on_ground():  # First jump
            self.velocity.y = self.jump_strength  # Apply upward force for jump
            self.jump_count = 1  # Reset jump count to 1 after the first jump
        elif self.jump_count < 2:  # Double jump
            self.velocity.y = self.jump_strength
            self.jump_count += 1  # Increment the jump count

    def player_input(self):
        if self.move_left:
            self.velocity.x = -100
        if self.move_right:
            self.velocity.x = 100
        if (not self.move_left and not self.move_right) or (self.move_left and self.move_right):
            self.velocity.x = self.velocity.x * .9
    
    def is_on_ground(self):
        super().is_on_ground()
    
    def update(self, dt):
        super().update(dt)
        self.player_input()
        if self.is_on_ground():
            self.jump_count = 0  # Reset jump count when on the ground