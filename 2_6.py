from pygame.constants import *

from all_colors import*
from random import choice
import pygame
pygame.init()
size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Моя игра")
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)

x, y = 0, 0
rect_size = 200
colors = COLORS
rects = []

for i in range(1 ,13):
    rect = pygame.Rect(x, y, rect_size-20*i, rect_size-20*i)
    rect.center = (screen.get_width()//2, screen.get_height()/2)
    rects.append(rect)


speed = 5

FPS = 60
clock = pygame.time.Clock()

running = True

while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()









    #Основная логика
    # if x < 0:
    #     x = 0
    #     color = choice(COLORS)
    #     continue
    # if x > 1280 - width:
    #     x = 1280 - width
    #     color = choice(COLORS)
    #     continue
    # if y < 0:
    #     y = 0
    #     color = choice(COLORS)
    #     continue
    # if y > 720 - height:
    #     y = 720 - height
    #     color = choice(COLORS)
    #     continue

    #Отрисовка объектов
    for rect in rects:
        pygame.draw.rect(screen, choice(colors), rect, 20, border_radius=10)

    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()