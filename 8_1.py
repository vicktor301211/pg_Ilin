import pygame



pygame.init()
size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Рисование")
BACKGROUND = (0,0,0)
screen.fill(BACKGROUND)

points = []

FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            points.append(event.pos)
    #Основная логика
    #Отрисовка объектов
    screen.fill(BACKGROUND)

    for i in range(len(points) - 1):
        start_pos = points[i]
        end_pos = points[i+1]

        pygame.draw.line(screen, (255,255,255), start_pos, end_pos, 3)

    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()