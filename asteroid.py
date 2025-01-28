import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y , radius):
        super().__init__(x,y,radius)
        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = radius


    def draw(self, screen):
        #drawing the asteroids
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)
        

    def update(self,dt):
        self.position += (self.velocity * dt)
        

         
