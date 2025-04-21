import pygame


def init(width, height, caption, fps, bg_color, running):
    global size, screen, BACKGROUND, FPS
    pygame.init()
    size = (width, height)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(f'{caption}')
    BACKGROUND = bg_color
    screen.fill(BACKGROUND)
    FPS = fps
    clock = pygame.time.Clock()
    running = running
    while running:
            # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            #Основная логика
            #Отрисовка объектов
        screen.fill(BACKGROUND)
        pygame.display.flip()
        clock.tick(FPS)
