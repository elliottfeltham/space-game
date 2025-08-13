import sys
import time
import pygame
from scripts.entities import Player, Bullet, Asteroid
from scripts.utils import *

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("space game")

        self.clock = pygame.time.Clock()

        self.game_active = False

        # groups
        self.all_sprites = pygame.sprite.Group()
        self.player_group = pygame.sprite.GroupSingle()
        self.bullets = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()

        # player
        self.player = Player((32,32), SCREEN_CENTER)
        self.player_group.add(self.player)
        self.all_sprites.add(self.player)

        # asteroids
        self.asteroid_spawn_rate = 2000
        self.asteroid_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.asteroid_timer, self.asteroid_spawn_rate)

        # score system
        self.score = 0
        self.high_score = 0


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                
                if self.game_active:

                    # shoot
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.bullet = self.player.fire()
                            self.all_sprites.add(self.bullet)
                            self.bullets.add(self.bullet)

                    # spawn asteroid and increase spawn rate
                    if event.type == self.asteroid_timer:
                            asteroid = Asteroid(get_offscreen_location(), self.player.rect.center, 2)
                            self.all_sprites.add(asteroid)
                            self.asteroids.add(asteroid)
                            self.asteroid_spawn_rate -= 25
                            if self.asteroid_spawn_rate < 100:
                                self.asteroid_spawn_rate = 1000

                            pygame.time.set_timer(self.asteroid_timer, self.asteroid_spawn_rate)
                
            if self.game_active:

                # collisions
                hits = pygame.sprite.groupcollide(self.bullets, self.asteroids, False, True)
                for bullet in hits:
                    bullet.explode()
                    self.score += 1

                if pygame.sprite.groupcollide(self.player_group, self.asteroids, False, False):
                    self.game_active = False
                    self.screen.fill((0,0,0))

                score_display = Text(("SCORE: " + str(self.score)), 32, (400, 50), (255,255,255))
                score_display.render(self.screen)
                self.screen.fill((0,0,0))
                self.all_sprites.update()
                self.all_sprites.draw(self.screen)

            else:
                self.screen.fill((0,0,0))

                # handle text
                title_display = Text("ASTEROIDS", 64, (400, 75), (255,255,255))
                title_display.render(self.screen)

                start_game_text = Text("PRESS SPACE TO START", 48, (400, 200), (255,255,255))
                start_game_text.render(self.screen)

                if self.score > 0 or self.high_score > 0:
                    if self.score > self.high_score:
                        self.high_score = self.score

                    score_display = Text(("HIGH SCORE: " + str(self.high_score)), 32, (400, 350), (255,255,255))
                    score_display.render(self.screen)


                # start game
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    self.game_active = True
                    self.score = 0
                    self.asteroids.empty()
                    self.bullets.empty()
                    self.all_sprites.empty()
                    self.all_sprites.add(self.player)
                    self.player_group.add(self.player)
                    time.sleep(0.5)

        
            pygame.display.update()
            self.clock.tick(60)
Game().run() 