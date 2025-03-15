import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            vel1 = self.velocity.rotate(random_angle)
            vel2 = self.velocity.rotate(-random_angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS
            
            ast1 = Asteroid(self.position.x, self.position.y, new_radius)
            ast1.velocity = vel1 * 1.2
            ast2 = Asteroid(self.position.x, self.position.y, new_radius)
            ast2.velocity = vel2 * 1.2

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt