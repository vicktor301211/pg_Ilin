from all_colors import*
import pygame
pygame.init()
size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Моя игра")
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)

width, height = 100, 100
x, y = 50, 50
color = RED
speed = 5

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
                print(f'Нажата клавиша вверх')
            elif event.key == pygame.K_DOWN:
                print(f'Нажата клавиша вниз')
            elif event.key == pygame.K_LEFT:
                print(f'Нажата клавиша влево')
            elif event.key == pygame.K_RIGHT:
                print(f'Нажата клавиша вправо')
            else:
                print(f'Нажата клавиша {event.key}')
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                print(f'Отпущена клавиша вверх')
            elif event.key == pygame.K_DOWN:
                print(f'Отпущена клавиша вниз')
            elif event.key == pygame.K_LEFT:
                print(f'Отпущена клавиша влево')
            elif event.key == pygame.K_RIGHT:
                print(f'Отпущена клавиша вправо')
            else:
                print(f'Отпущена клавиша {event.key}')
    #Основная логика
    #Отрисовка объектов
    screen.fill(BACKGROUND)

    pygame.draw.rect(screen, color, (x, y, width, height))

    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()