import pygame



pygame.init()
size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Рисование")
BACKGROUND = (0,0,0)
screen.fill(BACKGROUND)

LINE_COLOR = (255,255,255)
PREVIEW_COLOR = (192,192,192)

points = []
preview = True

FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                points.append(event.pos)

            if event.button == 3:
                preview = not preview
    #Основная логика
    #Отрисовка объектов
    screen.fill(BACKGROUND)

    for i in range(len(points) - 1):
        start_pos = points[i]
        end_pos = points[i+1]

        pygame.draw.line(screen, LINE_COLOR, start_pos, end_pos, 3)


    if len(points) > 0 and preview:
        last_point = points[-1]
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.aaline(screen, PREVIEW_COLOR, last_point, mouse_pos)

    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()