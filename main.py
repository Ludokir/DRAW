import pygame
import os
import random

os.environ['SDL_VIDEO_CENTERED'] = '1'

WIDTH_WIN, HEIGHT_WIN = 800, 800
collide = False
collide2 = False
num = 0
num1 = 0
num2 = 0
speed_x = random.randint(4, 10)
speed_y = random.randint(4, 10)
block = False
collide1 = False
collide2 = False
g = False
m = False

rect_size = w, h = 300, 300
rect_pos = ((WIDTH_WIN - w) // 2, (HEIGHT_WIN - h) // 2)

pol_size = w, h = 50, 50
pol_pos = (300, 300)

circle_radius = 35
circle_pos = (0, 0)

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0, 180)
BG = (128, 128, 128)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

pygame.init()
pygame.display.set_caption('DRAW and COLLIDE')
screen = pygame.display.set_mode((WIDTH_WIN, HEIGHT_WIN))
FPS = 120
clock = pygame.time.Clock()

surface = pygame.Surface(
    (circle_radius * 2, circle_radius * 2), pygame.SRCALPHA)
pygame.draw.circle(
    surface, YELLOW, (circle_radius, circle_radius), circle_radius)
rect1 = surface.get_rect()

ball = pygame.image.load('img/ball.png')
ball_rect = ball.get_rect(topleft=(0, 0))

font = pygame.font.SysFont('Arial', 20, True, False)
font1 = pygame.font.SysFont('Arial', 20, True, False)
font2 = pygame.font.SysFont('Arial', 20, True, False)


def mo(x, y):
    if ball_rect.left < 0 or ball_rect.right > WIDTH_WIN:
        x = -x
    if ball_rect.top < 0 or ball_rect.bottom > HEIGHT_WIN:
        y = -y


run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                run = False
        elif e.type == pygame.MOUSEMOTION:
            rect1.center = e.pos

    screen.fill(BG)

    rect2 = pygame.draw.rect(
        screen, RED if collide or collide1 else BLUE, (rect_pos, rect_size))
    rect3 = pygame.draw.polygon(screen, RED if collide2 else GREEN, [
        [600, 700], [700, 700], [650, 600]])

    text = font.render(str(num), 1, BLACK)
    text_render = text.get_rect(center=((WIDTH_WIN - 100), 50))

    text1 = font1.render(str(num1), 1, BLUE)
    text_render1 = text1.get_rect(center=(100, 50))

    text2 = font2.render(str(num2), 1, GREEN)
    text_render2 = text2.get_rect(center=(400, 50))

    ball_rect = ball_rect.move(speed_x, speed_y)
    mo(speed_x, speed_y)

    if ball_rect.colliderect(rect2):
        collide1 = True
        if not g:
            num1 += 1
        g = True
    else:
        collide1 = False
        g = False

    if rect1.colliderect(rect2):
        collide = True
        if not block:
            num += 1
        block = True
    else:
        collide = False
        block = False

    if rect1.colliderect(rect3):
        collide2 = True
        if not m:
            num2 += 1
        m = True
    else:
        collide2 = False
        m = False

    screen.blit(text2, text_render2)
    screen.blit(surface, rect1)
    screen.blit(text, text_render)
    screen.blit(text1, text_render1)
    screen.blit(ball, ball_rect)
    pygame.display.update()
    clock.tick(FPS)
