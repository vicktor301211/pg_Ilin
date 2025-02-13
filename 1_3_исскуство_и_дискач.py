import random

import all_colors
from all_colors import *
import pygame
pygame.init()
music = ['resourse/Disco_music_1.mp3', 'resourse/Disco_music_2.mp3']
random_music = random.choice(music)
pygame.mixer.init()
pygame.mixer.music.load(random_music)
pygame.mixer.music.play(-1)
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

    #Основная логика
    #Отрисовка объектов
    rand_index = random.choice(COLOR)
    screen.fill(rand_index)
    for i in range(25):
        rand_color = random.choice(COLOR)
        rand_x = random.randint(10, 1590)
        rand_y = random.randint(10, 900)
        rand_radius = random.randint(20, 200)
        pygame.draw.ellipse(screen, rand_color, (rand_x, rand_y, rand_radius, rand_radius))
    pygame.display.flip()
    pygame.time.delay(random.randint(200, 800))
pygame.quit()