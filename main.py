
# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # setting game to 60 FPS to reduce CPU costs
    time_clock = pygame.time.Clock()
    dt = 0

    # making the player
    space_ship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 7)

    # python
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = time_clock.tick(60) / 1000
        space_ship.update(dt)

        screen.fill(0)
        space_ship.draw(screen)
        pygame.display.flip()




if __name__ == "__main__":
    main()
