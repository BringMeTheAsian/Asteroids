import pygame, sys
from asteroid_field import AsteroidField
from logger import log_state, log_event
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from shot import Shot
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    field = AsteroidField()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0.0
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for drawing in drawable:
            drawing.draw(screen)
        updatable.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid) == True:
                    shot.kill()
                    asteroid.split()
                    log_event("asteroid_shot")
            if asteroid.collides_with(player) == True:
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
