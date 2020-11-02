import pygame
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'

WIDTH_WIN, HEIGHT_WIN = 400, 400
collide = False
num = 0
block = False

rect_size = w, h = 70, 70
rect_pos = ((WIDTH_WIN - w) // 2, (HEIGHT_WIN - h) // 2)

circle_radius = 35
circle_pos = (0, 0)

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0, 180)
BG = (128, 128, 128)
BLACK = (0, 0, 0)

pygame.init()
pygame.display.set_caption('DRAW and COLLIDE')
screen = pygame.display.set_mode((WIDTH_WIN, HEIGHT_WIN))
FPS = 60
clock = pygame.time.Clock()

surface = pygame.Surface((circle_radius * 2, circle_radius * 2), pygame.SRCALPHA)
pygame.draw.circle(surface, YELLOW, (circle_radius, circle_radius), circle_radius)
rect1 = surface.get_rect()

font = pygame.font.SysFont('Arial', 20, True, False)

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
    
    rect2 = pygame.draw.rect(screen, RED if collide else BLUE, (rect_pos, rect_size))

    text = font.render(str(num), 1, BLACK)
    text_render = text.get_rect(center=(300, 50))

    if rect1.colliderect(rect2):
        collide = True
        if not block:
            num += 1
        block = True
    else:
        collide = False
        block = False

    screen.blit(surface, rect1)
    screen.blit(text, text_render)
    pygame.display.update()
    clock.tick(FPS)
