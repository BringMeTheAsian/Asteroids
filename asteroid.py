import pygame, random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE_SECONDS, ASTEROID_MAX_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        new_vector = self.velocity.rotate(angle)
        new_neg_vector = self.velocity.rotate(-angle)
        new_radii = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radii)
        asteroid_1.velocity = new_vector * 1.2
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radii)
        asteroid_2.velocity = new_neg_vector * 1.2
        log_event("asteroid_split")
