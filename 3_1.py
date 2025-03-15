from all_colors import *
import pygame

pygame.init()
size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Моя игра")
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)

rect_1 = pygame.Rect(100, 100, 200, 150)
rect_2 = pygame.Rect(250, 150, 200, 150)
rect_3 = pygame.Rect(500, 100, 200, 150)
rect_4 = pygame.Rect(600, 300, 200, 150)

width = 5

def collision(rect, other_rect):
    if rect.colliderect(other_rect):
        pygame.draw.rect(screen, RED, rect, width)
        pygame.draw.rect(screen, RED, other_rect, width)
    else:
        pygame.draw.rect(screen, BLUE, rect, width)
        pygame.draw.rect(screen, BLUE, other_rect, width)

collision(rect_1, rect_2)
collision(rect_3, rect_4)

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
    #screen.fill(BACKGROUND)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()