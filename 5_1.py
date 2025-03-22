import sys
from random import *
from all_colors import *
import pygame
pygame.init()

ai_mode = True

if len(sys.argv) > 1:
    if sys.argv[1] == '--human':
        ai_mode = False

name_1 = input('Введите имя первого игрока: ')
if ai_mode == True:
    name_2 = "ИИ"
else:
    name_2 = input('Введите имя второго игрока: ')


SCR_WIDTH = 1280
SCR_HEIGHT = 720
screen = pygame.display.set_mode([SCR_WIDTH, SCR_HEIGHT])
pygame.display.set_caption("Пинг-понг")

directs = [-5, 5]

PADDLE_WIDTH = 25
PADDLE_HEIGHT = 100
PADDLE_SPEED = 10

BALL_SIZE = 15
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

screen_rect = pygame.Rect(0, 0, SCR_WIDTH, SCR_HEIGHT)

paddle_1_rect = pygame.Rect(0, SCR_HEIGHT//2 - PADDLE_HEIGHT//2,
                            PADDLE_WIDTH, PADDLE_HEIGHT)

paddle_2_rect = pygame.Rect(SCR_WIDTH - PADDLE_WIDTH,
                            SCR_HEIGHT//2 - PADDLE_HEIGHT//2,
                            PADDLE_WIDTH, PADDLE_HEIGHT)

ball_rect = pygame.Rect(SCR_WIDTH//2 - BALL_SIZE//2,
                            SCR_HEIGHT//2 - BALL_SIZE//2, BALL_SIZE, BALL_SIZE)

score_1 = 0
score_2 = 0
font = pygame.font.SysFont(None, 32)



BACKGROUND = BLACK
screen.fill(BACKGROUND)
FPS = 60
clock = pygame.time.Clock()
running = True


def ai():
    if ball_rect.x > SCR_WIDTH//2:
        if ball_rect.centery < paddle_2_rect.centery:
            paddle_2_rect.y -= PADDLE_SPEED
        elif ball_rect.centery > paddle_2_rect.centery:
            paddle_2_rect.y += PADDLE_SPEED

        if paddle_2_rect.top <= 0:
            paddle_2_rect.top = 0
        if paddle_2_rect.bottom >= SCR_HEIGHT:
            paddle_2_rect.bottom = SCR_HEIGHT

    else:
        paddle_2_rect.centery += (SCR_HEIGHT//2 - paddle_2_rect.centery) / PADDLE_SPEED



while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and paddle_2_rect.top > 0:
        paddle_2_rect.y -= PADDLE_SPEED
    elif keys[pygame.K_DOWN] and paddle_2_rect.bottom < SCR_HEIGHT:
        paddle_2_rect.y += PADDLE_SPEED
    elif keys[pygame.K_w] and paddle_1_rect.top > 0:
        paddle_1_rect.y -= PADDLE_SPEED
    elif keys[pygame.K_s] and paddle_1_rect.bottom < SCR_HEIGHT:
        paddle_1_rect.y += PADDLE_SPEED
    if ai_mode:
        ai()

    ball_rect.x += BALL_SPEED_X
    ball_rect.y += BALL_SPEED_Y

    if ball_rect.top <= 0 or ball_rect.bottom >= SCR_HEIGHT:
        BALL_SPEED_Y *= -1

    # Если поверхность мяча столкнулась с поверхностью первой ракетки или поверхность мяча столкнулась с поверхностью второй ракетки: скорость мяча по оси x умножить на минус единицу

    if ball_rect.colliderect(paddle_1_rect) or ball_rect.colliderect(paddle_2_rect):
        BALL_SPEED_Y += 1
        BALL_SPEED_X += 1
        BALL_SPEED_X *= -1

    if ball_rect.left <= 0:
        ball_rect.center = (SCR_WIDTH//2, SCR_HEIGHT//2)
        BALL_SPEED_X = choice(directs)
        BALL_SPEED_Y = choice(directs)
        score_2 += 1

    elif ball_rect.left >= SCR_WIDTH:
        ball_rect.center = (SCR_WIDTH//2, SCR_HEIGHT//2)
        BALL_SPEED_X = choice(directs)
        BALL_SPEED_Y = choice(directs)
        score_1 += 1





    #Основная логика
    #Отрисовка объектов
    screen.fill(BACKGROUND)
    if score_1 >= 10:
        BALL_SPEED_Y = 0
        BALL_SPEED_X = 0
        screen.fill(RED)
        win_text = font.render(f'{name_1} Победил(а)!', True, WHITE)
        screen.blit(win_text, (SCR_WIDTH // 2 - win_text.get_width() // 2, 50))
    elif score_2 >= 10:
        BALL_SPEED_Y = 0
        BALL_SPEED_X = 0
        screen.fill(BLUE)
        win_text = font.render(f'{name_2} Победил(а)!', True, WHITE)
        screen.blit(win_text, (SCR_WIDTH // 2 - win_text.get_width() // 2, 50))

    pygame.draw.rect(screen, RED, paddle_1_rect)
    pygame.draw.rect(screen, BLUE, paddle_2_rect)
    pygame.draw.ellipse(screen, WHITE, ball_rect)

    pygame.draw.line(screen, WHITE, (SCR_WIDTH//2, 0), (SCR_WIDTH//2, SCR_HEIGHT), 2)

    score_text = font.render(f'{score_1} : {score_2}', True, WHITE)
    screen.blit(score_text, (SCR_WIDTH // 2 - score_text.get_width() // 2, 10))

    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()


#Добавления:
#1. Звуки. 2. При отскоке увеличивается скорость(до 30). 3. Отображение скорости. 4. Завершение игры(уже есть)