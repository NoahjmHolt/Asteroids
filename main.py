
# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # setting game to 60 FPS to reduce CPU costs
    time_clock = pygame.time.Clock()
    dt = 0

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color=0)
        pygame.display.flip()

        dt = time_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
