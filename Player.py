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
        self.image = pyglet.shapes.Rectangle(x, y, 20, 20, color=(255, 0, 0))
        
        #Animations
        self.idle_frames = []
        self.run_frames = []
        self.jump_frames = []

        self.load_images()
        self.current_frame = 0
        self.time_since_last_frame = 0
        self.frame_duration = 1 / 60  # 60 fps
        
        self.idle_animation = pyglet.image.Animation.from_image_sequence(
            self.idle_frames, duration=.2, loop=True
        )
        
        self.run_animation = pyglet.image.Animation.from_image_sequence(
            self.run_frames, duration=.2, loop=True
        )
        
        self.jump_animation = pyglet.image.Animation.from_image_sequence(
            self.jump_frames, duration=.05, loop=False
        )
        
        
        # Create sprite with animation
        self.sprite = pyglet.sprite.Sprite(self.idle_animation, x=self.image.x, y=self.image.y)
        self.sprite.anchor_x = self.sprite.width // 2
        self.sprite.anchor_y = 0       
        #States
        self.moving = False
        self.jumping = False
        self.falling = False

        
      
    
    def draw(self):
        # self.image.draw() 
        self.sprite.draw() 
        
    def load_images(self):
        # Load each image
        
        for i in range(4):
            image = pyglet.image.load(f'assets/idle/adventurer{i+1}.png')
            image.anchor_x = image.width // 2
            image.anchor_y = image.height // 2
            self.idle_frames.append(image)
        
        for i in range(6):
            image = pyglet.image.load(f'assets/run/adventurer{i+1}.png')
            image.anchor_x = image.width // 2
            image.anchor_y = image.height // 2
            self.run_frames.append(image)
        
        for i in range(4):
            image = pyglet.image.load(f'assets/jump/adventurer{i+1}.png')
            image.anchor_x = image.width // 2
            image.anchor_y = image.height // 2
            self.jump_frames.append(image)
        
        
        
    
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
        elif self.jump_count < 1:  # Double jump
            self.velocity.y = self.jump_strength
            self.jump_count += 1  # Increment the jump count
        elif self.can_wall_hop and self.is_on_wall() and not self.is_on_ground():
            self.velocity.y = self.jump_strength
            self.velocity.x = self.velocity.x * -1
            self.can_wall_hop = False

    def player_input(self):
        self.velocity.x = 0
        if self.move_left:
            self.velocity.x = -100
            if not self.sprite.scale_x < 0:
                self.sprite.scale_x = -self.sprite.scale_x
        if self.move_right:
            self.velocity.x = 100
            if self.sprite.scale_x < 0:
                self.sprite.scale_x = -self.sprite.scale_x
    
    def is_on_ground(self):
        super().is_on_ground()
    
    def update(self, dt):
        super().update(dt)
        # Center the sprite based on the image's position
        self.sprite.x = self.image.x + self.image.width // 2
        self.sprite.y = self.image.y - self.image.height + self.sprite.height
        self.player_input()
        if self.is_on_ground():
            self.jump_count = 0  # Reset jump count when on the ground
        self.state_manager()
        self.animation_manager(dt)
    
    def state_manager(self):
        if self.velocity.x != 0:
            self.moving = True
        else:
            self.moving = False
        if self.velocity.y > 0:
            self.jumping = True
            
        else:
            self.jumping = False
            
    def animation_manager(self, dt):
        print(self.jumping, self.falling, self.moving)
        
        if not self.jumping and not self.falling and self.moving:
            if self.sprite.image != self.run_animation:                
                self.sprite.image = self.run_animation
        
        if not self.moving and not self.jumping and not self.falling:
            if self.sprite.image != self.idle_animation:
                self.sprite.image = self.idle_animation
                
        if self.jumping:
            if self.sprite.image != self.jump_animation:
                self.sprite.image = self.jump_animation