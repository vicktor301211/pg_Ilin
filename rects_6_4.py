from random import *
from all_colors import *

import pygame
pygame.init()
size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Квадратики")
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)

RECT_COLOR = (255, 0, 0)
top_left = (0, 0)
rect_size = (0, 0)

contur = 1

dragging = False
filling = False

rects = []

FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            top_left = event.pos
            rect_size = 0,0
            dragging = True
            filling = False

        elif event.type == pygame.MOUSEMOTION and dragging:
            right_bottom = event.pos
            rect_size = (right_bottom[0] - top_left[0], right_bottom[1] - top_left[1])

        elif event.type == pygame.MOUSEBUTTONUP:
            right_bottom = event.pos
            rect_size = (right_bottom[0] - top_left[0], right_bottom[1] - top_left[1])
            dragging = False
            rect = pygame.Rect(top_left, rect_size)
            color = choice(COLORS)
            rects.append((rect, color))

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                filling = not filling

        if filling == False:
            contur = 1
        elif filling == True:
            contur = 0


    #Основная логика
    #Отрисовка объектов
    screen.fill(BACKGROUND)

    pygame.draw.rect(screen, RECT_COLOR, (top_left, rect_size), contur)
    for rectangle, color in rects:
        pygame.draw.rect(screen, color, rectangle, contur)

    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()