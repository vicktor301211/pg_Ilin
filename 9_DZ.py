from all_colors import *


def create_palett():            #Функция для создания палитры
    palette.fill(bg_color)
    for i in range(12):
        color_rect = pygame.Rect(i * size, 0, size, size)
        pygame.draw.rect(palette, COLORS[i], color_rect)

    border_rect = pygame.Rect(CUR_INDEX * size, 0, size, size)
    pygame.draw.rect(palette, BORDER_COLOR, border_rect, width=3)
    screen.blit(palette, palette_rect.topleft)

#Дальше мне лень писать комментарии

import pygame

pygame.init()
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Рисовалка')
bg_color = (255, 255, 255)
brush_color = COLORS[5]
brush_width = 5

rects = []

BORDER_COLOR = (0, 0, 0)
CUR_INDEX = 5
RECT_COLOR = (255, 0, 0)

top_left = (0, 0)
rect_size = (0, 0)
contur = 1

canvas = pygame.Surface(screen.get_size())
canvas.fill(bg_color)

size = 50
square_size = 50
palette_rect = pygame.Rect(10, 10, size * 12, size)
palette = pygame.Surface(palette_rect.size)

font = pygame.font.SysFont(None, 24)

dragging = False
filling = False

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

            elif event.key == pygame.K_c:
                canvas.fill(WHITE)
                rects = []
                rect_size = (0,0)

            elif event.key == pygame.K_z:
                brush_width = 5

            elif event.key == pygame.K_SPACE:
                filling = not filling

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                top_left = event.pos
                rect_size = 0,0
                dragging = True
                filling = False

        elif event.type == pygame.MOUSEMOTION and dragging:
            right_bottom = event.pos
            rect_size = (right_bottom[0] - top_left[0], right_bottom[1] - top_left[1])

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 3:
                right_bottom = event.pos
                rect_size = (right_bottom[0] - top_left[0], right_bottom[1] - top_left[1])
                dragging = False
                rect = pygame.Rect(top_left, rect_size)
                color = brush_color
                rects.append((rect, color))

        if filling == False:
            contur = 1
        elif filling == True:
            contur = 0

    mouse_pos = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()


    if pressed[0]:
        if palette_rect.collidepoint(mouse_pos):
            selected_index = ((mouse_pos[0] - palette_rect.left) // size)
            CUR_INDEX = selected_index
            brush_color = COLORS[CUR_INDEX]
        else:
            pygame.draw.circle(canvas, brush_color, mouse_pos, brush_width)





    # Основная логика
    # Отрисовка объектов

    brush_size_text = font.render(f'Размер кисти: {brush_width}', True, BLACK)
    screen.blit(canvas, (0, 0))
    screen.blit(brush_size_text, (10, 70))

    pygame.draw.rect(screen, RECT_COLOR, (top_left, rect_size), contur)
    for rectangle, color in rects:
        pygame.draw.rect(screen, color, rectangle, contur)



    create_palett()
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()