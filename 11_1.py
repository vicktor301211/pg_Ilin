import pygame
import sys
import abc
import random
import os

from pygame.constants import K_BACKSPACE
import pygame.mixer
pygame.mixer.init()

difficulty = int(input("Введите сложность от 1 до 3: "))

pygame.mixer.music.load('resourse/light_music.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)


class State(abc.ABC):
    @abc.abstractmethod
    def handle_events(self, events):
        pass

    @abc.abstractmethod
    def update(self):
        pass

    @abc.abstractmethod
    def draw(self, screen):
        pass


class SplashScreen(State):
    def __init__(self):

        self.background_image = pygame.image.load('resourse/zastavka.png')

        self.hint_visible = True
        self.hint = 'Нажмите [LMB] для продолжения'
        self.hint_surface = font.render(self.hint, True, (0, 0, 0))

        self.hint_time = pygame.time.get_ticks()

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                return MenuScreen()
        return self

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.hint_time > 750:
            self.hint_visible = not self.hint_visible
            self.hint_time = current_time

    def draw(self, screen):
        screen.fill((255, 255, 255))

        screen.blit(self.background_image, [0, 0])
        if self.hint_visible:
            hint_rect = self.hint_surface.get_rect()

            hint_rect.centerx = screen.get_rect().centerx
            hint_rect.centery = screen.get_rect().centery + 100

            screen.blit(self.hint_surface, hint_rect)


class MenuScreen(State):
    def __init__(self):
        self.background_image = pygame.image.load('resourse/zastavka.png')
        self.items = ['Играть', 'Выбрать имя игрока', 'Выйти']
        self.surfaces = [font.render(item, True, (0, 0, 0)) for item in self.items]
        self.selected = 0

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    return self.process_item()
                elif event.key == pygame.K_UP:
                    self.prev()
                elif event.key == pygame.K_DOWN:
                    self.next()
        return self

    def update(self):
        pass

    def draw(self, screen):
        screen.fill((255, 255, 255))
        screen.blit(self.background_image, [0, 0])
        for i, surface in enumerate(self.surfaces):
            rect = surface.get_rect()
            rect.centerx = screen.get_rect().centerx
            rect.top = screen.get_rect().top + 150 * (i + 1)
            if i == self.selected:
                surface = font.render(self.items[i], True, (255, 0, 0))
            screen.blit(surface, rect)


    def next(self):
        if self.selected < len(self.items) - 1:
            self.selected += 1

    def prev(self):
        if self.selected > 0:
            self.selected -= 1

    def process_item(self):
        if self.selected == 0:
            return GameScreen()
        elif self.selected == 1:
            return NameScreen()
        elif self.selected == 2:
            pygame.quit()
            exit()


class NameScreen(State):
    def __init__(self):
        self.background_image = pygame.image.load('resourse/zastavka.png')
        self.text = 'Введите имя игрока'
        self.surface = font.render(self.text, True, BACKGROUND)
        self.name = ''
        self.name_surface = None

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if len(self.name) > 0:
                        self.name = self.name[:-1]
                        self.name_surface = font.render(self.name, True, (0, 0, 0))
                elif event.key == pygame.K_RETURN:
                    global player_name
                    player_name = self.name
                    return MenuScreen()
                else:
                    if event.unicode.isalnum() and len(self.name) < 10:
                        self.name += event.unicode
                        self.name_surface = font.render(self.name, True, BACKGROUND)
        return self

    def update(self):
        pass

    def draw(self, screen):
        screen.fill((255, 255, 255))
        screen.blit(self.background_image, [0, 0])
        rect = self.surface.get_rect()
        rect.centerx = screen.get_rect().centerx
        rect.top = screen.get_rect().top + 150
        screen.blit(self.surface, rect)
        if self.name_surface is not None:
            name_rect = self.name_surface.get_rect()
            name_rect.centerx = screen.get_rect().centerx
            name_rect.top = screen.get_rect().top + 250
            screen.blit(self.name_surface, name_rect)


class GameScreen(State):
    def __init__(self):
        self.difficulty = difficulty
        self.ROWS = self.difficulty * 3
        self.COLS = self.ROWS
        self.MARGIN = 2
        self.timer = 0
        self.swaps = 0
        self.selected = None
        self.game_completed = False
        self.SAVE_FILE_NAME = 'statistic.txt'

        # Загрузка изображения
        pictures = os.listdir('pictures')
        picture = random.choice(pictures)
        self.image = pygame.image.load('pictures/' + picture)

        # Инициализация пазла
        self.init_puzzle()

        # Шрифты
        self.info_font = pygame.font.SysFont('Arial', 32)
        self.game_over_font = pygame.font.SysFont('Arial', 64)

        # Кнопка возврата в меню
        self.back_text = self.info_font.render('Назад в меню - [Backspace]', True, (255, 255, 255))
        self.back_rect = self.back_text.get_rect()
        self.back_rect.topleft = (800, 20)

    def init_puzzle(self):
        image_width, image_height = self.image.get_size()
        self.TILE_WIDTH = image_width // self.COLS
        self.TILE_HEIGHT = image_height // self.ROWS

        self.tiles = []
        for i in range(self.ROWS):
            for j in range(self.COLS):
                rect = pygame.Rect(j * self.TILE_WIDTH, i * self.TILE_HEIGHT,
                                   self.TILE_WIDTH, self.TILE_HEIGHT)
                tile = self.image.subsurface(rect)
                self.tiles.append(tile)

        self.origin_tiles = self.tiles.copy()

        # Перемешиваем пазл
        while True:
            random.shuffle(self.tiles)
            if self.tiles != self.origin_tiles:
                break

    def is_puzzle_solved(self):
        for i in range(len(self.tiles)):
            if self.tiles[i] != self.origin_tiles[i]:
                return False
        return True

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.save()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not self.game_completed:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for i in range(len(self.tiles)):
                    row = i // self.ROWS
                    col = i % self.COLS
                    x = col * (self.TILE_WIDTH + self.MARGIN) + self.MARGIN
                    y = row * (self.TILE_HEIGHT + self.MARGIN) + self.MARGIN

                    if x <= mouse_x <= x + self.TILE_WIDTH and y <= mouse_y <= y + self.TILE_HEIGHT:
                        if self.selected is not None and self.selected != i:
                            self.tiles[i], self.tiles[self.selected] = self.tiles[self.selected], self.tiles[i]
                            self.selected = None
                            self.swaps += 1
                            # Проверяем, собран ли пазл после каждого хода
                            if self.is_puzzle_solved():
                                self.game_completed = True
                        elif self.selected == i:
                            self.selected = None
                        else:
                            self.selected = i
            elif event.type == pygame.KEYDOWN and event.key == K_BACKSPACE:
                self.save()
                return MenuScreen()
        return self

    def update(self):
        if not self.game_completed:
            self.timer += 1

    def draw(self, screen):
        screen.fill((50, 80, 65))

        # Рисуем кнопку "Назад"
        pygame.draw.rect(screen, (50, 50, 50), self.back_rect.inflate(10, 10))
        screen.blit(self.back_text, self.back_rect)

        # Рисуем пазл
        self.draw_tiles(screen)

        # Рисуем информацию
        self.draw_info(screen)

        # Если игра завершена - показываем сообщение
        if self.game_completed:
            self.draw_game_over(screen)

    def save(self):
        with open(self.SAVE_FILE_NAME, 'w') as f:
            f.write(f'{player_name}, {self.timer//60}, {self.swaps}, {self.difficulty}')

    def draw_tiles(self, screen):
        for i in range(len(self.tiles)):
            tile = self.tiles[i]
            row = i // self.ROWS
            col = i % self.COLS
            x = col * (self.TILE_WIDTH + self.MARGIN)
            y = row * (self.TILE_HEIGHT + self.MARGIN)
            if i == self.selected:
                pygame.draw.rect(screen, (0, 255, 0),
                                 (x - self.MARGIN, y - self.MARGIN,
                                  self.TILE_WIDTH + self.MARGIN * 2,
                                  self.TILE_HEIGHT + self.MARGIN * 2))
            screen.blit(tile, (x, y))

    def draw_info(self, screen):
        # Имя игрока
        name_text = self.info_font.render(f'Игрок: {player_name}', True, (255, 255, 255))
        screen.blit(name_text, (800, 60))

        # Сложность
        diff_text = self.info_font.render(f'Сложность: {self.difficulty}', True, (255, 255, 255))
        screen.blit(diff_text, (800, 100))

        # Размер
        size_text = self.info_font.render(f'Размер: {self.ROWS}x{self.COLS}', True, (255, 255, 255))
        screen.blit(size_text, (800, 140))

        # Таймер
        time_text = self.info_font.render(f'Время: {self.timer // 60}', True, (255, 255, 255))
        screen.blit(time_text, (800, 180))

        # Перемещения
        swaps_text = self.info_font.render(f'Ходов: {self.swaps}', True, (255, 255, 255))
        screen.blit(swaps_text, (800, 220))

    def draw_game_over(self, screen):
        text = self.game_over_font.render('Пазл собран!', True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (screen.get_rect().centerx, screen.get_rect().centery + 200)
        pygame.draw.rect(screen, (0, 0, 0), text_rect.inflate(20, 20))
        screen.blit(text, text_rect)




# Инициализация pygame
pygame.init()
pygame.font.init()
size = (1280, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Пазлы")
BACKGROUND = (0, 0, 0)
screen.fill(BACKGROUND)
FPS = 60
clock = pygame.time.Clock()

player_name = 'Guest'
font = pygame.font.SysFont(None, 64)

running = True
state = SplashScreen()

while running:
    events = pygame.event.get()

    # Обработка событий
    for event in events:
        if event.type == pygame.QUIT:
            running = False


    state = state.handle_events(events)
    state.update()
    state.draw(screen)


    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()