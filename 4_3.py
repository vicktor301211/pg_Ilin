from random import *
from all_colors import *
import pygame
pygame.init()
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Моя игра")
BACKGROUND = (135, 206, 235)
screen.fill(BACKGROUND)

snowflake = pygame.Surface((50, 50))
snowflake.set_colorkey((0, 0, 0))

pygame.draw.circle(snowflake, WHITE, (25, 25), 10)
pygame.draw.line(snowflake, WHITE, (25, 5), (25, 45), 5)
pygame.draw.line(snowflake, WHITE, (5, 25), (45, 25), 5)
pygame.draw.line(snowflake, WHITE, (10, 10), (40, 40), 5)
pygame.draw.line(snowflake, WHITE, (10, 40), (40, 10), 5)



snowflakes = []

# screen.blit(snowflake, pos)
SNOWFLAKES_COUNT = 25

for i in range(SNOWFLAKES_COUNT):
    pos = [randint(0, 800), randint(0, 600)]
    screen.blit(snowflake, pos)
    snowflakes.append(pos)
print(snowflakes)



FPS = 60
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

    for pos in snowflakes:
        pos[1] += 1
        screen.blit(snowflake, pos)
        if pos[1] > 600:
            pos[0] = randint(0, 800)
            pos[1] = 0


    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()