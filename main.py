import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroidsgroup = pygame.sprite.Group()
    shotsgroup = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroidsgroup, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shotsgroup, updateable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0,0,0))
        updateable.update(dt)
        for asts in asteroidsgroup:
            if asts.collides_with_circle(player):
                print("Game over!")
                sys.exit()
            for shot in shotsgroup:
                if asts.collides_with_circle(shot):
                    shot.kill()
                    asts.split()
        
        for drawn in drawable:
            drawn.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
