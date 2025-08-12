import sys
import pygame
from scripts.entities import Player

SCREEN_SIZE = (800, 400)
SCREEN_CENTER = (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2)

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("space game")

        self.clock = pygame.time.Clock()

        self.player = Player((32,32), SCREEN_CENTER)


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


            self.screen.fill((0,0,0))

            self.player.update()
            self.player.render(self.screen)
            
            pygame.display.update()
            self.clock.tick(60)
Game().run()