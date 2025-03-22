from all_colors import *
import pygame as pg

pg.init()

screen_width = 1280
screen_height = 720
screen = pg.display.set_mode([screen_width, screen_height], pg.FULLSCREEN)
pg.mouse.set_visible(False)

pg.display.set_caption('Самолёты')

background_image = pg.image.load('resourse/Nebo.png').convert()

plane_1_image = pg.image.load('resourse/Plane_1.png').convert()

plane_1_image.set_colorkey((0, 0, 0))
plane_1_rect = plane_1_image.get_rect()

plane_2_image = pg.image.load('resourse/Plane_2.png').convert_alpha()
plane_2_rect = plane_2_image.get_rect()

clock = pg.time.Clock()

FPS = 60
running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.blit(background_image, [0, 0])

    mouse_position = pg.mouse.get_pos()

    plane_1_rect.x = mouse_position[0]
    plane_1_rect.y = mouse_position[1]

    keys = pg.key.get_pressed()

    if keys[pg.K_LEFT] and plane_2_rect.left > -100:
        plane_2_rect.x -= 5
    elif keys[pg.K_RIGHT] and plane_2_rect.right < screen_width + 100:
        plane_2_rect.x += 5
    elif keys[pg.K_UP] and plane_2_rect.top > -150:
        plane_2_rect.y -= 5
    elif keys[pg.K_DOWN] and plane_2_rect.bottom < screen_height + 150:
        plane_2_rect.y += 5
    elif keys[pg.K_x]:
        exit()

    screen.blit(plane_1_image, plane_1_rect)
    screen.blit(plane_2_image, plane_2_rect)

    pg.display.flip()
    clock.tick(FPS)

pg.quit()