import pygame as pg
import random
import math


def convert(point, side_len, offset, height):
    x = round(point[0] * side_len + offset[0])
    y = round(height - offset[1] - point[1] * side_len * math.sqrt(3)/2)
    return x, y


def generate(start, points):
    point = random.choice(points)
    del_x = point[0] - start[0]
    del_y = point[1] - start[1]

    return round(start[0] + del_x / 2, 5), round(start[1] + del_y / 2, 5)


def main():
    # Init pygame
    pg.init()
    clock = pg.time.Clock()

    # Window properties
    HEIGHT = 900
    WIDTH = 900
    window = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("Sierpinski Triangle")

    # Points for triangle (in separate coordinate system)
    p1 = (0, 0)
    p2 = (1, 0)
    p3 = (0.5, 1)

    # Triangle properties
    side_len = 800
    offset = (50, 150)

    # Bottom of triangle
    cand_1 = (random.randint(0, 10000) / 10000, 0)

    # Left side of triangle
    x = random.randint(0, 5000) / 5000
    cand_2 = (x, 2*x)

    # Right side of triangle
    x = random.randint(5000, 10000) / 5000
    cand_3 = (x, 2 - 2*x)

    # Point to draw (including starting point)
    point = random.choice([cand_1, cand_2, cand_3])

    # Colors
    black = (0, 0, 0)
    white = (255, 255, 255)

    running = True
    count = 0
    dots = 20000

    window.fill(white)
    while running:
        if count < dots:
            pg.draw.circle(window, black, convert(point, side_len, offset, HEIGHT), 1)
            point = generate(point, [p1, p2, p3])
            count += 1
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        pg.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
