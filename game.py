import sys
import pygame
from scripts.entities import Player, Bullet

SCREEN_SIZE = (800, 400)
SCREEN_CENTER = (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2)

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



            self.screen.fill((0,0,0))

            self.all_sprites.update()
            self.all_sprites.draw(self.screen)

            print(self.bullets)

            pygame.display.update()
            self.clock.tick(60)
Game().run() 