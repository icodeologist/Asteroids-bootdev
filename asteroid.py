import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

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

    def spilt(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            print("spliting")
        random_angle = random.uniform(20, 50)
            # Create two new velocity vectors by rotating the original
        velocity1 = self.velocity.rotate(random_angle)
        velocity2 = self.velocity.rotate(-random_angle)
        self.kill() 
        # Calculate new radius for child asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        # Create two new asteroids at the same position
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        
        # Set their velocities (scaled up by 1.2)
        asteroid1.velocity = velocity1 * 1.2
        asteroid2.velocity = velocity2 * 1.2

         
