import pygame
import random
import os



def draw_tiles():
    for i in range (len(tiles)):
        tile = tiles[i]
        row = i//ROWS
        col = i%COLS
        x = col * (TILE_WIDTH + MARGIN) + MARGIN
        y = row * (TILE_HEIGHT + MARGIN) + MARGIN
        screen.blit(tile, (x, y))

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
ROWS = 3
COLS = 3
MARGIN = 2

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Пазлы")
clock = pygame.time.Clock()

pictures = os.listdir('pictures')
picture = random.choice(pictures)
image = pygame.image.load('pictures/' + picture)

image_width, image_height = image.get_size()
TILE_WIDTH = image_width//COLS
TILE_HEIGHT = image_height//ROWS

tiles = []
for i in range(ROWS):
    for j in range(COLS):
        rect = pygame.Rect(i*TILE_WIDTH, j*TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT)
        tile = image.subsurface(rect)
        tiles.append(tile)

origin_tiles = tiles.copy()

random.shuffle(tiles)

selected = None

swaps = 0

running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # print(mouse_x, mouse_y) #Отладочная ерунда
            for i in range(len(tiles)):
                row = i//ROWS
                col = i%COLS
                x = col * (TILE_WIDTH + MARGIN) + MARGIN
                y = row * (TILE_HEIGHT + MARGIN) + MARGIN

                if x<=mouse_x <= x+TILE_WIDTH and y <= mouse_y <= y + TILE_HEIGHT:
                    if selected is not None and selected != i:
                        tiles[i], tiles[selected] = tiles[selected], tiles[i]
                        selected = None
                        swaps += 1

                    elif selected == i:
                        selected = None

                    else:
                        selected = i


    #Основная логика
    #Отрисовка объектов
    screen.fill((0,0,0))
    draw_tiles()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()