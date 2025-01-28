import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player


def main():
    pygame.init()
    screen=pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    dt = 0

    #the player which is space ship
    player_ = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2) 
    print(player_)

    #groups for multiple instances
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    updatable.add(player_)
    drawable.add(player_)
    
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
        screen.fill((0,0,0)) 
        #update all objects
            
        for sprite in updatable: 
            sprite.update(dt)
        
        for sprite in drawable:
            sprite.draw(screen)

        #tick also return the time between different frames
        time_diff_between_frames = clock.tick(60)
        dt = time_diff_between_frames/1000
            
        pygame.display.flip()
if __name__ == "__main__":
    main()
