import sys
import pygame
from pygame.display import update
from constants import (
    SCREEN_WIDTH, 
    SCREEN_HEIGHT,
    ASTEROID_MAX_RADIUS,
    ASTEROID_MIN_RADIUS,
    ASTEROID_KINDS,
    ASTEROID_SPAWN_RATE
)
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape, Shot


def main():
    pygame.init()
    screen=pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    dt = 0
    #creating objects of diff classes
    #the player which is space ship
    
    

    #groups for multiple instances
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids_group =  pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable,asteroids_group)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable, shots)

    player_ = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2) 
    asteroid_field = AsteroidField() 

    updatable.add(player_)
    drawable.add(player_)
    updatable.add(asteroid_field)
    
    clock = pygame.time.Clock()
    while True:
        for  event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            shot = player_.shoot()
            if shot:
                shots.add(shot)
        screen.fill((0,0,0)) 
        #update all objects
            
        for sprite in updatable: 
            sprite.update(dt)
        for sprite  in asteroids_group:
            if sprite.check_for_collisions(player_):
                print("Game over!")
                sys.exit()
            for bullet in shots:
                if sprite.check_for_collisions(bullet):
                    sprite.spilt()
                    bullet.kill()
                    break
                    
        for sprite in drawable:
            sprite.draw(screen)
            
        #tick also return the time between different frames
        time_diff_between_frames = clock.tick(60)
        dt = time_diff_between_frames/1000
            
        pygame.display.flip()
if __name__ == "__main__":
    main()
