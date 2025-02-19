from random import *
from all_colors import*
import pygame
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Моя игра")
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)
FPS = 60
width = 100
height = 75
rects = []
rects.append(pygame.Rect(0, 0, width, height))

rects.append(pygame.Rect(0, 0, width, height))
rects[-1].topright = (screen_width, 0)

rects.append(pygame.Rect(0, 0, width, height))
rects[-1].bottomright = (screen_width, screen_height)

rects.append(pygame.Rect(0, 0, width, height))
rects[-1].bottomleft = (0, screen_height)

rects.append(pygame.Rect(0, 0, width, height))
rects[-1].center = (screen_width//2, screen_height//2)


clock = pygame.time.Clock()
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #Основная логика
    #Отрисовка объектов
    screen.fill(BACKGROUND)
    for rect in rects:
        color = choice(COLORS)
        pygame.draw.rect(screen, color, rect)
    pygame.display.flip()
    clock.tick(FPS//10)
pygame.quit()