import pygame
from circleshape import CircleShape, Shot
from constants import SHOT_RADIUS,PLAYER_RADIUS, PLAYER_SHOOT_SPEED, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS, PLAYER_SHOOT_COOLDOWN

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y ,PLAYER_RADIUS)
        self.x = x
        self.y = y
        self.rotation = 0
        self.timer = 0

    
    #traingle 
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    #overiding draw from parent 
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
     
    #moving the player(triangle)
    def rotate(self, dt):
        self.rotation = PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        if self.timer > 0:
            self.timer -= dt

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotation += -(PLAYER_TURN_SPEED * dt)

        if keys[pygame.K_d]:
            self.rotation += PLAYER_TURN_SPEED * dt

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()



    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.timer <= 0:
            shot = Shot(self.position.x, self.position.y , SHOT_RADIUS)
            direction = pygame.Vector2(0,1)
            direction = direction.rotate(self.rotation)
            direction *= PLAYER_SHOOT_SPEED
            shot.velocity = direction
            self.timer = PLAYER_SHOOT_COOLDOWN
            return shot
        return None


                             










