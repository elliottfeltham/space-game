import pygame
import math

class Player(pygame.sprite.Sprite):
    def __init__(self, size=(32,32), pos=(0,0), color=(255,255,255)):
        super().__init__()

        self.size = size
        self.color = color
        self.original_image = pygame.Surface(self.size).convert_alpha()

        self.points = [(0, self.size[1]), (self.size[0] // 2, 0), (self.size[0], self.size[1]), (self.size[0] // 2, self.size[1] // 1.5)]
        pygame.draw.polygon(self.original_image, self.color, self.points , width=3)

        self.image = self.original_image.copy()
        self.rect = self.original_image.get_rect(center=pos)


    def rotate(self):
        # work out rotation angle based of mouse position
        mouse_pos = pygame.mouse.get_pos()
        x_dist = mouse_pos[0] - self.rect.centerx
        y_dist = - (mouse_pos[1] - self.rect.centery)
        self.angle = math.degrees(math.atan2(y_dist, x_dist))

        self.image = pygame.transform.rotate(self.original_image, self.angle - 90)
        center = self.rect.center
        self.rect = self.image.get_rect(center=center)

    def fire(self):
        # fire method creates bullets using class
        mouse_pos = pygame.mouse.get_pos()
        direction = pygame.math.Vector2(mouse_pos) - pygame.math.Vector2(self.rect.center) # use vectors to get bullet directions
        direction = direction.normalize()
        muzzle_distance = self.size[1] // 2
        spawn_pos = pygame.math.Vector2(self.rect.center) + (direction * muzzle_distance)
        return Bullet(spawn_pos, direction, 10)

    def update(self):
        self.rotate()
        

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, direction, speed):
        super().__init__()

        self.speed = speed
        self.pos = pos

        self.image = pygame.Surface((5,5))
        pygame.draw.circle(self.image, (255,255,255),(2.5,2.5), 2.5)
        self.rect = self.image.get_rect(center=pos)

        self.velocity = direction * self.speed

        self.spawn_time = pygame.time.get_ticks()

    def update(self):
        self.pos += self.velocity
        self.rect.center = self.pos

        current_time = pygame.time.get_ticks()
        if current_time - self.spawn_time > 3000:
            self.kill()

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, pos, player_pos, speed):
        super().__init__()

        self.pos = pygame.math.Vector2(pos)
        self.speed = speed

        self.image = pygame.Surface((32,32)).convert_alpha()
        self.rect = self.image.get_rect(center=self.pos)
        pygame.draw.circle(self.image, (255,255,255), (16,16), 16, 3)

        direction = pygame.math.Vector2(player_pos) - pygame.math.Vector2(self.rect.center)
        direction = direction.normalize()

        self.velocity = direction * self.speed

    def update(self):
        self.pos += self.velocity
        self.rect.center = self.pos


            
            

        
