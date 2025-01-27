import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


def main():
    pygame.init()
    screen=pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    dt = 0
    #change in the time or delta
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
        pygame.Surface.fill(screen ,(0,0,0))
        pygame.display.flip()
        #tick also return the time between different frames
        time_diff_between_frames = clock.tick(60)
        dt = time_diff_between_frames/1000
        print(dt)
if __name__ == "__main__":
    main()
