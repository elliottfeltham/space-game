import pygame
import math

class Player():
    def __init__(self, size=(32,32), pos=(0,0), color=(255,255,255)):
        self.size = size
        self.color = color
        self.original_image = pygame.Surface(self.size).convert_alpha()

        self.points = [(0, self.size[1]), (self.size[0] // 2, 0), (self.size[0], self.size[1]), (self.size[0] // 2, self.size[1] // 1.5)]
        pygame.draw.polygon(self.original_image, self.color, self.points , width=3)

        self.image = self.original_image.copy()
        self.rect = self.original_image.get_rect(center=pos)
        self.rect.center = pos

    def movement(self):
        mouse_pos = pygame.mouse.get_pos()
        x_dist = mouse_pos[0] - self.rect.centerx
        y_dist = - (mouse_pos[1] - self.rect.centery)
        self.angle = math.degrees(math.atan2(y_dist, x_dist))

    def update(self):
        self.movement()
        self.image = pygame.transform.rotate(self.original_image, self.angle - 90)
        center = self.rect.center
        self.rect = self.image.get_rect(center=center)
    
    def render(self, surf):
        surf.blit(self.image, self.rect)
        
