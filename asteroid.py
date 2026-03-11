import pygame
from circleshape import CircleShape
from constants import *
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        first_piece_vector = self.velocity.rotate(random_angle)
        second_piece_vector = self.velocity.rotate(-random_angle)
        piece_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, piece_radius)
        asteroid.velocity = 1.2 * first_piece_vector
        asteroid = Asteroid(self.position.x, self.position.y, piece_radius)
        asteroid.velocity = 1.2 * second_piece_vector

    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt