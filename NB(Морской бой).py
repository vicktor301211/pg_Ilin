from all_colors import *
import pygame
pygame.init()

import pygame.mixer
pygame.mixer.init()

shot_sound = pygame.mixer.Sound('resourse/shot.mp3')
explosion_sound = pygame.mixer.Sound('resourse/explosion.mp3')
fail_sound = pygame.mixer.Sound('resourse/fail.mp3')

pygame.mixer.music.load('resourse/sonar.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)

shot_sound.set_volume(0.6)




size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Моя игра")
BACKGROUND = CYAN
screen.fill(BACKGROUND)

screen_rect = screen.get_rect()

ship = pygame.Rect(300, 200, 50, 100)
ship.right = screen_rect.right
ship.centery = screen_rect.centery


missiles_counter = 10

missile = pygame.Rect(50, 50, 10, 10)
missile.left = screen_rect.left
missile.centery = screen_rect.centery



missile_speed_x = 0
missile_speed_y = 0

ship_speeed_y = 1

ship_alive = True
missile_alive = True

missile_launched = False

hp_ship = 10

FPS = 60
clock = pygame.time.Clock()
running = True

while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not missile_launched:
                missile_launched = True
                missile_speed_x = 3
                missile_speed_y = 0
                shot_sound.play()
            elif event.key == pygame.K_w and not missile_launched:
                missile_speed_y = -2
            elif event.key == pygame.K_s and not missile_launched:
                missile_speed_y = 2

    #Основная логика

    if missile_alive:
        missile.move_ip(missile_speed_x, missile_speed_y)
        if not missile.colliderect(screen_rect):
            missile_alive = False
            fail_sound.play()



        if ship_alive and missile.colliderect(ship):
            hp_ship -= 1
            missiles_counter -= 1
            if missiles_counter == 0:
                missile_alive = False
            if hp_ship == 0:
                ship_alive = False
            explosion_sound.play()


    #Отрисовка объектов
    screen.fill(BACKGROUND)
    if ship_alive:
        pygame.draw.rect(screen, BLUE, ship)
        ship.move_ip(0, ship_speeed_y)
        if ship.bottom > screen_rect.bottom or ship.top < screen_rect.top:
            ship_speeed_y = -ship_speeed_y
    if missile_alive:
        for i in range(missiles_counter):
            pygame.draw.rect(screen, RED, missile)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()