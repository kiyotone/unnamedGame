import pyglet   # type: ignore

class Entity:
    def __init__(self, x: int, y: int, game):
        self.gravity = -5.8  # Gravity force
        self.image = pyglet.shapes.Rectangle(x, y, 20, 20, color=(0, 0, 255))
        self.velocity = pyglet.math.Vec2(0, 0)
        self.game = game
        self.right = self.image.x + self.image.width
        self.left = self.image.x
        self.top = self.image.y + self.image.height
        self.bottom = self.image.y
        

    def draw(self):
        self.image.draw()
    
    def colliderect(self, platform):
        return (
            self.image.x < platform.right and
            self.image.x + self.image.width > platform.left and
            self.image.y < platform.top and
            self.image.y + self.image.height > platform.bottom
        )


    def is_on_ground(self):
        # Check if the player is on the ground by moving down a little and checking for collision
        self.image.y -= 1
        on_ground = any(self.colliderect(platform) for platform in self.game.platform_array)
        self.image.y += 1
        if on_ground:
            self.jump_count = 0
        return on_ground
    

    def update(self, dt):
        if not self.is_on_ground() :
            self.velocity.y += self.gravity
            
        self.image.x += self.velocity.x * dt
        self.handle_collision(self.velocity.x, 0)
        self.image.y += self.velocity.y * dt
        self.handle_collision(0, self.velocity.y)
                

    def handle_collision(self, dx, dy):
        for platform in self.game.platform_array:
            if self.colliderect(platform):
                if dx > 0:  # Moving right
                    self.image.x = platform.image.x - self.image.width
                elif dx < 0:  # Moving left
                    self.image.x = platform.image.x + platform.image.width
                elif dy > 0:  # Moving down
                    self.image.y = platform.image.y - self.image.height
                elif dy < 0:  # Moving up
                    self.image.y = platform.image.y + platform.image.height
                    self.velocity.y = 0

