import pygame
import sys
import abc



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
        self.text = 'Заставка'
        self.surface = font.render(self.text, True, (255,255,255))


    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        return self


    def update(self):
        pass


    def draw(self, screen):
        screen.fill(BACKGROUND)
        rect = self.surface.get_rect()
        rect.center = (size[0]//2, size[1]//2)
        screen.blit(self.surface, rect)

pygame.init()
pygame.font.init()
size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Моя игра")
BACKGROUND = (0, 0, 0)
screen.fill(BACKGROUND)
FPS = 60
clock = pygame.time.Clock()

player_name = 'Guest'

font = pygame.font.SysFont(None, 64)

running = True

state = SplashScreen()

while running:
    # Обработка событий
    events = pygame.event.get()
    # for event in events:
    #     if event.type == pygame.QUIT:
    #         pygame.quit()
    #         sys.exit()

    state = state.handle_events(events)

    state.update()

    state.draw(screen)
    #Основная логика
    #Отрисовка объектов

    pygame.display.flip()
    clock.tick(FPS)
