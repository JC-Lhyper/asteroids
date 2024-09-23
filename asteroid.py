import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):

    def draw(self, screen):
        pygame.draw.circle(screen, 'red', self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        new_vectors = [self.velocity.rotate(random_angle), self.velocity.rotate(-random_angle)]
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        for vector in new_vectors:
            new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid.velocity = (vector * 1.2)

