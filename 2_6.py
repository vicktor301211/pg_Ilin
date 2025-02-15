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
colors = [RED, BLACK]

for i in range(1 ,3):
    rect = pygame.Rect(x, y, rect_size//i, rect_size//i)
    rect.center = (screen.get_width()//2, screen.get_height()/2)
    pygame.draw.rect(screen, colors[i-1], rect)
# rect1 = pygame.Rect(x, y, rect_size, rect_size)
# rect1.center = (screen.get_width()//2, screen.get_height()//2)
# pygame.draw.rect(screen, BLACK, rect1)
# rect2 = pygame.Rect(x, y, rect_size//2, rect_size//2)
# rect2.center = (screen.get_width()//2, screen.get_height()//2)
# pygame.draw.rect(screen, RED, rect2)

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

    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()