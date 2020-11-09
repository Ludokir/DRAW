import pygame
import os
import random

os.environ['SDL_VIDEO_CENTERED'] = '1'

WIDTH_WIN, HEIGHT_WIN = 600, 600
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
block1 = False
block2 = False

rect_size = w, h = (WIDTH_WIN * 0.375), (HEIGHT_WIN * 0.375)
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


def move():
    global speed_x
    global speed_y
    global ball_rect
    ball_rect = ball_rect.move(speed_x, speed_y)
    if ball_rect.left < 0 or ball_rect.right > WIDTH_WIN:
        speed_x = -speed_x
    if ball_rect.top < 0 or ball_rect.bottom > HEIGHT_WIN:
        speed_y = -speed_y


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

    move()

    rect2 = pygame.draw.rect(
        screen, RED if collide or collide1 else BLUE, (rect_pos, rect_size))
    rect3 = pygame.draw.polygon(screen, RED if collide2 else GREEN, [
        [(WIDTH_WIN - 150), (HEIGHT_WIN - 75)], [(WIDTH_WIN - 75), (
            HEIGHT_WIN - 75)], [(WIDTH_WIN - 112.5), (HEIGHT_WIN - 150)]])

    text = font.render(str(num), 1, BLACK)
    text_render = text.get_rect(center=((WIDTH_WIN - 100), 50))

    text1 = font1.render(str(num1), 1, BLUE)
    text_render1 = text1.get_rect(center=(100, 50))

    text2 = font2.render(str(num2), 1, GREEN)
    text_render2 = text2.get_rect(center=((WIDTH_WIN // 2), 50))

    if ball_rect.colliderect(rect2):
        collide1 = True
        if not block1:
            num1 += 1
        block1 = True
    else:
        collide1 = False
        block1 = False

    if rect1.colliderect(rect2):
        collide = True
        if not block:
            num += 1
        block = True
    else:
        collide = False
        block = False

    if rect1.colliderect(rect3) or ball_rect.colliderect(rect3):
        collide2 = True
        if not block2:
            num2 += 1
        block2 = True
    else:
        collide2 = False
        block2 = False

    screen.blit(text2, text_render2)
    screen.blit(surface, rect1)
    screen.blit(text, text_render)
    screen.blit(text1, text_render1)
    screen.blit(ball, ball_rect)
    pygame.display.update()
    clock.tick(FPS)
