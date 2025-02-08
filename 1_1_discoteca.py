import random

import all_colors
from all_colors import *
import pygame
pygame.init()
# pygame.mixer.init()
# pygame.mixer.music.load('resourse/La La Land.mp3')
# pygame.mixer.music.play(-1)
size = (0, 0)
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
pygame.display.set_caption("Моя игра")
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)
COLOR = all_colors.COLORS
clock = pygame.time.Clock()
running = True
timer = 0
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    rand_index = random.choice(COLOR)
    #Основная логика
    #Отрисовка объектов
    screen.fill(rand_index)
    pygame.display.flip()
    pygame.time.delay(random.randint(200, 800))
pygame.quit()