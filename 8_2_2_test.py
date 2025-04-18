import pygame
pygame.init()
size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Рисование линий")
BACKGROUND = (0, 0, 0)
screen.fill(BACKGROUND)

LINE_COLOR = (255, 255, 255)
PREVIEW_COLOR = (192, 192, 192)

points = []  # Список списков точек (каждый подсписок - отдельная линия)
current_line = []  # Текущая рисуемая линия
drawing_mode = True  # Режим рисования (вкл/выкл)

FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and drawing_mode:  # Левая кнопка - добавить точку
                current_line.append(event.pos)
            elif event.button == 3:  # Правая кнопка - переключить режим/начать новую линию
                if drawing_mode and current_line:  # Если был режим рисования и есть точки
                    points.append(current_line.copy())  # Сохраняем текущую линию
                current_line = []  # Начинаем новую линию
                drawing_mode = True  # Включаем режим рисования

    # Отрисовка
    screen.fill(BACKGROUND)

    # Рисуем все сохранённые линии
    for line in points:
        if len(line) > 1:
            pygame.draw.lines(screen, LINE_COLOR, False, line, 3)

    # Рисуем текущую линию (если есть точки)
    if len(current_line) > 1:
        pygame.draw.lines(screen, LINE_COLOR, False, current_line, 3)

    # Рисуем линию предпросмотра (если есть точки и режим включён)
    if len(current_line) > 0 and drawing_mode:
        last_point = current_line[-1]
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.aaline(screen, PREVIEW_COLOR, last_point, mouse_pos, 3)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()