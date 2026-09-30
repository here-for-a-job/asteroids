from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import pygame
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle_divergence = random.uniform(20, 50)
        velocity1 = self.velocity.rotate(angle_divergence)
        velocity2 = self.velocity.rotate(-angle_divergence)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        x = self.position.x
        y = self.position.y
        asteroid1 = Asteroid(x, y, new_radius)
        asteroid1.velocity = velocity1 * 1.2
        asteroid2 = Asteroid(x, y, new_radius)
        asteroid2.velocity = velocity2 * 1.2

    def reset(self):
        self.kill()
