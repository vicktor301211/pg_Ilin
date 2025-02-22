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

player = pygame.Rect(0, 0, 100, 40)
player.midleft = (0, size[1]//2)

enemy = pygame.Rect(0, 0, 100, 40)
enemy.midleft = (size[0]-100, size[1]//2)

running = True



while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #Основная логика
    #Отрисовка объектов
    screen.fill(BACKGROUND)

    pygame.draw.rect(screen, MAROON, player)
    pygame.draw.rect(screen, CYAN, enemy)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()