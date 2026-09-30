import pygame
import sys
from constants import *
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
from shot import Shot
from pointboard import Pointboard
from calculate import calc_points_from_kill

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    pointboards = pygame.sprite.Group()
    resetable = pygame.sprite.Group()
    Player.containers = (updatable, drawable, resetable)
    Asteroid.containers = (asteroids, updatable, drawable, resetable)
    AsteroidField.containers = (updatable, resetable)
    Shot.containers = (shots, updatable, drawable, resetable)
    Pointboard.containers = (pointboards, drawable, resetable)
    asteroid_field = AsteroidField()
    scoreboard = Pointboard("SCORE", 0, 1000, 10)
    dt = 0.0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    livesboard = Pointboard("LIVES LEFT", player.lives, 10, 10)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
                    scoreboard.add_amount(calc_points_from_kill(asteroid))
            if asteroid.collides_with(player):
                log_event("player_hit")
                asteroid.split()
                player.lose_life()
                livesboard.add_amount(-1)
                if player.lives <=0:
                    for object in resetable:
                        object.reset()
        screen.fill("black")
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        if pygame.key.get_pressed()[pygame.K_q]:
            sys.exit()


if __name__ == "__main__":
    main()
