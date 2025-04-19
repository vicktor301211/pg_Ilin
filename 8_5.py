


def get_closest_point(mouse_pos):
    closest_point = None
    closest_distance = float('inf')
    for point in points:
        distance = ((point[0] - mouse_pos[0]) ** 2 + (point[1] - mouse_pos[1]) ** 2)**0.5
        if distance <= POINT_RADIUS**2 and distance < closest_distance:
            closest_point = point
            closest_distance = distance
            break
    return closest_point

def save_points():
    with open(POINTS_FILE_NAME, 'w') as f:
        for point in points:
            f.write(f'{point[0]} {point[1]}\n')

def load_points():
    points.clear()
    try:
        with open(POINTS_FILE_NAME, 'r') as f:
            for line in f:
                x,y = map(int, line.split())
                points.append((x, y))
    except FileNotFoundError:
        pass



import pygame
pygame.init()
size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Рисование")
BACKGROUND = (0, 0, 0)
screen.fill(BACKGROUND)

LINE_COLOR = (255, 255, 255)
PREVIEW_COLOR = (192, 192, 192)
REMOVE_RADIUS = 5
POINT_RADIUS = REMOVE_RADIUS
HILIGHT_COLOR = (255, 0, 0)
POINTS_FILE_NAME = 'points.txt'

points = []



FPS = 60
clock = pygame.time.Clock()

running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    closest_point = get_closest_point(mouse_pos)
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if closest_point:
                if event.button == 1:
                    points.append(event.pos)
                    print(points)
                elif event.button == 3:
                    points.remove(closest_point)
            elif event.button == 1:
                points.append(mouse_pos)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_c]:
            points = []
        elif keys[pygame.K_s]:
            save_points()
        elif keys[pygame.K_l]:
            load_points()
        elif keys[pygame.K_e]:
            exit()



    # Основная логика
    # Отрисовка объектов
    screen.fill(BACKGROUND)

    for i in range(len(points) - 1):
        pygame.draw.line(screen, LINE_COLOR, points[i], points[i+1], 3)

    if len(points) > 0:
        pygame.draw.aaline(screen, PREVIEW_COLOR, points[-1], mouse_pos)

    pos = pygame.mouse.get_pos()
    closest_point = get_closest_point(pos)
    if closest_point is not None:
        pygame.draw.circle(screen, HILIGHT_COLOR, closest_point, POINT_RADIUS)


    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()