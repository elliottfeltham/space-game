import sys
import pygame
from scripts.entities import Player, Bullet, Asteroid
from scripts.utils import SCREEN_SIZE, SCREEN_CENTER, get_offscreen_location

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("space game")

        self.clock = pygame.time.Clock()

        self.all_sprites = pygame.sprite.Group()

        self.player = Player((32,32), SCREEN_CENTER)
        self.all_sprites.add(self.player)
 
        self.bullets = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bullet = self.player.fire()
                        self.all_sprites.add(bullet)
                        self.bullets.add(bullet)

                    if event.key == pygame.K_UP:
                        asteroid = Asteroid(get_offscreen_location(), self.player.rect.center, 2)
                        self.all_sprites.add(asteroid)
                        self.asteroids.add(asteroid)


            self.screen.fill((0,0,0))

            self.all_sprites.update()
            self.all_sprites.draw(self.screen)



            pygame.display.update()
            self.clock.tick(60)
Game().run() 