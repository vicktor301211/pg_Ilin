import pygame
import math
import random

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

pygame.init()

size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pacman")

# Цвета
BACKGROUND = (0, 0, 0)
POINT_COLOR = (255, 255, 255)
ENEMY_COLOR = (255, 0, 0)
TEXT_COLOR = (255, 255, 255)

# Настройки игрока
pacman = pygame.image.load('resourse/pacman_right.png')
circle_pos = [320, 240]
angle = 20
speed = 4
health = 3
score = 0

# Настройки движения
dist = 0
max_dist = 100
min_speed = 3
max_speed = 5

# Настройки точек
points = []
for _ in range(10):
    points.append([random.randint(0, size[0]), random.randint(0, size[1])])

# Настройки врагов
enemies = []
enemy_spawn_timer = 0
enemy_spawn_interval = 240  # кадры между спавном врагов
enemy_width = 50
enemy_height = 30
enemy_speed = 5

clock = pygame.time.Clock()
running = True
game_over = False
win = False

# Шрифт для текста
font = pygame.font.SysFont(None, 36)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and (game_over or win):
            if event.key == pygame.K_r:
                # Перезапуск игры
                circle_pos = [320, 240]
                health = 3
                score = 0
                points = []
                for _ in range(10):
                    points.append([random.randint(0, size[0]), random.randint(0, size[1])])
                enemies = []
                game_over = False
                win = False

    if not game_over and not win:
        # Управление игроком
        mouse_pos = pygame.mouse.get_pos()
        dx = mouse_pos[0] - circle_pos[0]
        dy = mouse_pos[1] - circle_pos[1]
        angle = math.degrees(math.atan2(dx, dy))

        dist = distance(circle_pos, mouse_pos)
        speed = max_speed - (dist/max_dist) * (max_speed-min_speed)

        dx = speed * math.cos(math.radians(angle))
        dy = speed * math.sin(math.radians(angle))

        circle_pos[0] += dx
        circle_pos[1] += dy

        # Ограничение игрока в пределах экрана
        circle_pos[0] = max(0, min(size[0], circle_pos[0]))
        circle_pos[1] = max(0, min(size[1], circle_pos[1]))

        # Сбор очков
        for point in points[:]:
            if distance(circle_pos, point) < 50:
                points.remove(point)
                score += 1
                # Добавляем новую точку
                points.append([random.randint(0, size[0]), random.randint(0, size[1])])

        # Спавн врагов
        enemy_spawn_timer += 1
        if enemy_spawn_timer >= enemy_spawn_interval and random.random() < 0.05:
            enemies.append([0, circle_pos[1], enemy_width, enemy_height])
            enemy_spawn_timer = 0

        # Движение врагов
        for enemy in enemies[:]:
            enemy[0] += enemy_speed
            # Проверка столкновения с игроком
            if distance(circle_pos, enemy) <= 100:
                enemies.remove(enemy)
                health -= 1
                if health <= 0:
                    game_over = True
            # Удаление врагов за экраном
            elif enemy[0] > size[0]:
                enemies.remove(enemy)

        # Проверка победы
        if score >= 10:
            win = True

    # Отрисовка
    screen.fill(BACKGROUND)

    # Отрисовка точек
    for point in points:
        pygame.draw.circle(screen, POINT_COLOR, point, 10)

    # Отрисовка врагов
    for enemy in enemies:
        pygame.draw.rect(screen, ENEMY_COLOR, enemy)

    # Отрисовка игрока
    rotated_pacman = pygame.transform.rotate(pacman, -angle)
    rotated_pacman_rect = rotated_pacman.get_rect()
    rotated_pacman_rect.center = circle_pos
    screen.blit(rotated_pacman, rotated_pacman_rect)

    # Отрисовка счета и здоровья
    score_text = font.render(f"Очки: {score}", True, TEXT_COLOR)
    health_text = font.render(f"Жизни: {health}", True, TEXT_COLOR)
    screen.blit(score_text, (10, 10))
    screen.blit(health_text, (10, 50))

    # Отрисовка сообщений о конце игры
    if game_over:
        game_over_text = font.render("Игра окончена! Нажмите R для перезапуска", True, TEXT_COLOR)
        screen.blit(game_over_text, (size[0]//2 - 200, size[1]//2))
    if win:
        win_text = font.render("Победа! Нажмите R для перезапуска", True, TEXT_COLOR)
        screen.blit(win_text, (size[0]//2 - 150, size[1]//2))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()