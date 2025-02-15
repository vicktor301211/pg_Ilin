import pygame
pygame.init()
size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Моя игра")
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)
FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            print(f'Press {event.key}')
        if event.type == pygame.KEYUP:
            print(f'Release {event.key}')
    #Основная логика
    #Отрисовка объектов
    screen.fill(BACKGROUND)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()