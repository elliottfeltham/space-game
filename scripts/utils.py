import random

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

get_offscreen_location()