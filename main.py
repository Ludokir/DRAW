import pygame
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'

WIDTH_WIN, HEIGHT_WIN = 400, 400
BG = (128, 128, 128)

pygame.init()
pygame.display.set_caption('DRAW and COLLIDE')
screen = pygame.display.set_mode((WIDTH_WIN, HEIGHT_WIN))

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                run = False

    screen.fill(BG)
    pygame.display.update()
