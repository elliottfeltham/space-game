import random
import pygame

SCREEN_SIZE = (800, 400)
SCREEN_CENTER = (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2)

def get_offscreen_location():
    x_top_bottom = random.randint(-200, SCREEN_SIZE[0] + 200)
    x_right = random.randint(SCREEN_SIZE[0] + 200, SCREEN_SIZE[0] + 400)
    x_left = random.randrange(-400, -200)

    y_left_right = random.randint(-200, SCREEN_SIZE[1] + 200)
    y_top = random.randint(-400, -200)
    y_bottom = random.randrange(SCREEN_SIZE[1] + 200, SCREEN_SIZE[1] + 400)

    coordinates = random.choice([(x_right, y_left_right), (x_left, y_left_right), (x_top_bottom, y_top), (x_top_bottom, y_bottom)])
    return coordinates

class Text:
    def __init__(self, string, size, pos, color):
        self.string = string
        self.size = size
        self.pos = pos
        self.color = color

        font = pygame.font.Font("/Users/elliottfeltham/Workspace/python-repos/space-game/fonts/Pixeltype.ttf", self.size)

        self.text = font.render(self.string, False, self.color)
        self.rect = self.text.get_rect(center=pos)


    def render(self, surf):
        surf.blit(self.text, self.rect)
