from all_colors import *
import pygame
pygame.init()
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Моя игра")
BACKGROUND = YELLOW
screen.fill(BACKGROUND)


my_surface = pygame.Surface((200, 100))
my_surface.fill(WHITE)
pygame.draw.circle(my_surface, RED, (100, 50), 40)

my_surface.set_colorkey((WHITE))
my_surface.set_alpha(128)

my_rect = my_surface.get_rect()
my_rect.center = (400, 300)

screen.blit(my_surface, my_rect)


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