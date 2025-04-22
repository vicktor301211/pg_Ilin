from all_colors import *


def create_palett():
    palette.fill(bg_color)
    for i in range(12):
        color_rect = pygame.Rect(i * size, 0, size, size)
        pygame.draw.rect(palette, COLORS[i], color_rect)

    border_rect = pygame.Rect(CUR_INDEX * size, 0, size, size)
    pygame.draw.rect(palette, BORDER_COLOR, border_rect, width=3)
    screen.blit(palette, palette_rect.topleft)



import pygame

pygame.init()
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Рисовалка')
bg_color = (255, 255, 255)
brush_color = COLORS[5]
brush_width = 5

figure = 'квадрат'

CUR_FIGURE_IX = 0

BORDER_COLOR = (0, 0, 0)
CUR_INDEX = 5

canvas = pygame.Surface(screen.get_size())
canvas.fill(bg_color)

size = 50
square_size = 50
palette_rect = pygame.Rect(10, 10, size * 12, size)
palette = pygame.Surface(palette_rect.size)

font = pygame.font.SysFont(None, 24)

drag = False

FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                brush_width += 1
            elif event.key == pygame.K_DOWN:
                brush_width -= 1
                if brush_width <= 1:
                    brush_width = 1
            elif event.key == pygame.K_w:
                square_size += 5
            elif event.key == pygame.K_s:
                square_size -= 5
                if square_size <= 20:
                    square_size = 20

            elif event.key == pygame.K_c:
                canvas.fill(WHITE)


            elif event.key == pygame.K_RIGHT:
                CUR_FIGURE_IX += 1
                if CUR_FIGURE_IX >= 1:
                    CUR_FIGURE_IX = 1
            elif event.key == pygame.K_LEFT:
                CUR_FIGURE_IX -= 1
                if CUR_FIGURE_IX < 0:
                    CUR_FIGURE_IX = 0





        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3 and CUR_FIGURE_IX == 0:
                pygame.draw.rect(canvas, brush_color, (event.pos[0], event.pos[1], square_size, square_size))
            elif event.button == 3 and CUR_FIGURE_IX == 1:
                pygame.draw.rect(canvas, brush_color, (event.pos[0], event.pos[1], square_size, square_size), border_radius=50)






    mouse_pos = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()


    if pressed[0]:
        if palette_rect.collidepoint(mouse_pos):
            selected_index = ((mouse_pos[0] - palette_rect.left) // size)
            CUR_INDEX = selected_index
            brush_color = COLORS[CUR_INDEX]
        else:
            pygame.draw.circle(canvas, brush_color, mouse_pos, brush_width)
    elif pressed[1]:
        pygame.draw.rect(canvas, brush_color, (mouse_pos[0], mouse_pos[1], 100, 100))

    if CUR_FIGURE_IX == 0:
        figure = 'квадрат'
    elif CUR_FIGURE_IX == 1:
        figure = 'круг'


    # Основная логика
    # Отрисовка объектов

    brush_size_text = font.render(f'Размер кисти: {brush_width}', True, BLACK)
    figure_size_text = font.render(f'Размер фигуры: {square_size} (для отрисовки нажмите на ПКМ)', True, BLACK)
    figure_text = font.render(f'Фигура: {figure}', True, BLACK)

    screen.blit(canvas, (0, 0))
    screen.blit(brush_size_text, (10, 70))
    screen.blit(figure_size_text,(350, 70))
    screen.blit(figure_text, (170, 70))
    create_palett()
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()