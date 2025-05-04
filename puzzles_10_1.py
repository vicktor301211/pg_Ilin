
import pygame
import random
import os
from tkinter import *
def game():
    def draw_difficulty():
        font = pygame.font.SysFont('Arial', 32)
        text = font.render(f'Сложность: {difficulty}', True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (800, 250)
        pygame.draw.rect(screen, (0, 0, 0), text_rect.inflate(4, 4))
        screen.blit(text, text_rect)

    def draw_rows_cols():
        font = pygame.font.SysFont('Arial', 32)
        text = font.render(f'Размер: {ROWS}x{COLS}', True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (800, 150)
        pygame.draw.rect(screen, (0, 0, 0), text_rect.inflate(4, 4))
        screen.blit(text, text_rect)

    def draw_timer():
        font = pygame.font.SysFont('Arial', 32)
        text = font.render(f'Время: {timer//60}', True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (800, 50)
        pygame.draw.rect(screen, (0, 0, 0), text_rect.inflate(4, 4))
        screen.blit(text, text_rect)

    def draw_swaps():
        font = pygame.font.SysFont('Arial', 32)
        text = font.render(f'Кол-во перестановок: {swaps}', True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)
        pygame.draw.rect(screen, (0, 0, 0), text_rect.inflate(4, 4))
        screen.blit(text, text_rect)


    def game_over():
        font = pygame.font.SysFont('Arial', 64)
        text = font.render(f'Картинка собрана!', True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)
        pygame.draw.rect(screen, (0, 0, 0), text_rect.inflate(4, 4))
        screen.blit(text, text_rect)



    def draw_tiles():
        for i in range(len(tiles)):
            tile = tiles[i]
            row = i // ROWS
            col = i % COLS
            x = col * (TILE_WIDTH + MARGIN) + MARGIN
            y = row * (TILE_HEIGHT + MARGIN) + MARGIN
            if i == selected:
                pygame.draw.rect(screen, (0, 255, 0),
                                 (x - MARGIN, y - MARGIN, TILE_WIDTH + MARGIN * 2, TILE_HEIGHT + MARGIN * 2))
            screen.blit(tile, (x, y))


    def is_puzzle_solved():
        # Сравниваем текущие позиции с оригинальными
        for i in range(len(tiles)):
            if tiles[i] != origin_tiles[i]:
                return False
        return True


    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 800
    difficulty = int(input("Введите сложность от 1 до 3: "))
    if difficulty > 3:
        difficulty = 3
    elif difficulty < 1:
        difficulty = 1
    ROWS = difficulty * 3
    COLS = ROWS
    MARGIN = 2

    timer = 0

    def u_t():
        global timer
        timer += 1
        canv.after(1000, u_t)
    def timer_stop():
        canv.after(10000000, u_t)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Пазлы")
    clock = pygame.time.Clock()


    w = Tk()
    w.title('Танки на минималках 2.0')
    canv = Canvas(w, width=0, height=0, bg = 'white')


    pictures = os.listdir('pictures')
    picture = random.choice(pictures)
    image = pygame.image.load('pictures/' + picture)

    image_width, image_height = image.get_size()
    TILE_WIDTH = image_width // COLS
    TILE_HEIGHT = image_height // ROWS

    tiles = []
    for i in range(ROWS):
        for j in range(COLS):
            rect = pygame.Rect(j * TILE_WIDTH, i * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT)
            tile = image.subsurface(rect)
            tiles.append(tile)

    origin_tiles = tiles.copy()

    # Убедимся, что пазл решаем (перемешиваем, пока не станет решаемым)
    while True:
        random.shuffle(tiles)
        # Проверка на решаемость (можно упростить для демонстрации)
        if tiles != origin_tiles:
            break

    selected = None
    swaps = 0
    game_completed = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_completed:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for i in range(len(tiles)):
                    row = i // ROWS
                    col = i % COLS
                    x = col * (TILE_WIDTH + MARGIN) + MARGIN
                    y = row * (TILE_HEIGHT + MARGIN) + MARGIN

                    if x <= mouse_x <= x + TILE_WIDTH and y <= mouse_y <= y + TILE_HEIGHT:
                        if selected is not None and selected != i:
                            tiles[i], tiles[selected] = tiles[selected], tiles[i]
                            selected = None
                            swaps += 1
                            # Проверяем, собран ли пазл после каждого хода
                            if is_puzzle_solved():
                                game_completed = True
                        elif selected == i:
                            selected = None
                        else:
                            selected = i

        screen.fill((0, 0, 0))
        draw_tiles()
        draw_swaps()
        draw_timer()
        draw_rows_cols()
        draw_difficulty()


        if game_completed:
            game_over()
            timer_stop()
        if game_completed == False:
            u_t()
        pygame.display.flip()
        clock.tick(60)

