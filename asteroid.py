
import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color("white"), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        neg_roids = self.velocity.rotate(-1 * angle)
        pos_roids = self.velocity.rotate(angle)

        shrink_ray = self.radius - ASTEROID_MIN_RADIUS

        new_roid_1 = Asteroid(self.position.x, self.position.y, shrink_ray)
        new_roid_2 = Asteroid(self.position.x, self.position.y, shrink_ray)

        new_roid_1.velocity = neg_roids * 1.2
        new_roid_2.velocity = pos_roids * 1.2

