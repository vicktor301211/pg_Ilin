from pygame.constants import *
from all_colors import *
import pygame


pygame.init()
size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Моя игра")
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)


FPS = 60
clock = pygame.time.Clock()

speed = 5
move = {K_LEFT: (-speed, 0),
        K_RIGHT: (speed, 0),
        K_UP: (0, -speed),
        K_DOWN: (0, speed)}

player = pygame.Rect(0, 0, 100, 40)
player.midleft = (0, size[1]//2)

enemy = pygame.Rect(0, 0, 100, 40)
enemy.midleft = (size[0]-100, size[1]//2)


running = True



while running:
    # Обработка событий
    old_pos = player.topleft
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    for key in move:
        if keys[key]:
            v = move[key]
            player.move_ip(v)
    #Основная логика
    if player.colliderect(enemy):
        player.topleft = old_pos
    #Отрисовка объектов
    screen.fill(BACKGROUND)

    pygame.draw.rect(screen, MAROON, player)
    pygame.draw.rect(screen, BLUE, enemy)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()