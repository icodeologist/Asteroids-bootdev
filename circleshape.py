from contextlib import chdir
import pygame
import numpy as np

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    #checking collision
    def check_for_collisions(self, other_shape):
        distance = self.position.distance_to(other_shape.position)
        distance_radii = (self.radius + other_shape.radius)
        if distance <= distance_radii:
            return True
        else:
            return False
    
class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0,0)

    def update(self,dt):
        self.position += self.velocity * dt
    
    def draw(self,screen):
        pygame.draw.circle(screen, "white",(int(self.position.x) ,int(self.position.y)) ,self.radius)
        




