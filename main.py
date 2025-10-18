
# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # setting game to 60 FPS to reduce CPU costs
    time_clock = pygame.time.Clock()
    dt = 0

    # experimenting with groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    space_rocks = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (space_rocks, updatable, drawable)

    # making the player
    space_ship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 7)

    # python
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = time_clock.tick(60) / 1000
        updatable.update(dt)

        screen.fill(0)
        for ship in drawable:
            ship.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
