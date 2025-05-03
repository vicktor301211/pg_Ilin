

import pygame
import sys
import abc

from pygame.constants import KEYDOWN


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

        self.hint_visible = True
        self.hint = 'Нажмите [LMB] для продолжения'
        self.hint_surface = font.render(self.hint, True, (255, 255, 255))

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
        screen.fill(BACKGROUND)
        rect = self.surface.get_rect()
        rect.centerx = screen.get_rect().centerx
        rect.centery = screen.get_rect().centery - 100
        screen.blit(self.surface, rect)
        if self.hint_visible:
            hint_rect = self.hint_surface.get_rect()

            hint_rect.centerx = screen.get_rect().centerx
            hint_rect.centery = screen.get_rect().centery + 100

            screen.blit(self.hint_surface, hint_rect)

class MenuScreen(State):
    def __init__(self):
        self.text = 'Меню'
        self.surface = font.render(self.text, True, (255,255,255))


    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return NameScreen()
        return self


    def update(self):
        pass


    def draw(self, screen):
        screen.fill(BACKGROUND)
        rect = self.surface.get_rect()
        rect.center = (size[0]//2, size[1]//2)
        screen.blit(self.surface, rect)

class NameScreen(State):
    def __init__(self):
        self.text = 'Имя игрока'
        self.surface = font.render(self.text, True, (255,255,255))


    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return GameScreen()
        return self


    def update(self):
        pass


    def draw(self, screen):
        screen.fill(BACKGROUND)
        rect = self.surface.get_rect()
        rect.center = (size[0]//2, size[1]//2)
        screen.blit(self.surface, rect)

class GameScreen(State):
    def __init__(self):
        self.text = 'Игра'
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
#Дз на 10.05: сделать меню(урок 12), плюс добавить игру в код(это ппц)