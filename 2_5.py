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

rect = pygame.Rect(0, 100, 200, 150)

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
    rect.x += speed
    if rect.x > screen.get_width():
        rect.x = -rect.width
    #Отрисовка объектов
    screen.fill(BACKGROUND)

    pygame.draw.rect(screen, BLUE, rect)

    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()