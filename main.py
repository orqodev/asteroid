import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot

x = SCREEN_WIDTH / 2
y = SCREEN_HEIGHT / 2




def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    dt = 0
    clock = pygame.time.Clock()
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shoots = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = updatable
    Shot.containers = (updatable,drawable,shoots)
    AsteroidField()

    primary_player = Player(x,y)
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")

        # RENDER YOUR GAME HERE
        for obj in updatable:
            obj.update(dt)

        for obj in drawable:
            obj.draw(screen)

        for obj in asteroids:
            is_collision = obj.collision(primary_player)
            if is_collision:
                print("Game Over!")
                pygame.quit()
            for bullet in shoots:
                is_hit = obj.collision(bullet)
                if is_hit:
                    obj.split()
                    bullet.kill()








        # flip() the display to put your work on screen
        pygame.display.flip()

        dt = clock.tick(60)/1000  # limits FPS to 60

    pygame.quit()

if __name__ == "__main__":
    main()