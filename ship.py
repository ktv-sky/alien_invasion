import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        '''Инициализирует корабль и задает его начальную позицию'''
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Загрузка изображения корабля
        self.image = pygame.image.load('images/ship2.png')
        self.rect = self.image.get_rect() # - создаем прямоугольник корабля
        self.screen_rect = screen.get_rect() # - создаем прямоугльник экрана

        # каждый новый корабль появляется у нижнего края экрана
        # - центр прямоугольника корабля равен центру прямоугольника экрана
        self.rect.centerx = self.screen_rect.centerx
        # - низ прямоугольника корабля равен низу центра прямоугольника экрана
        self.rect.bottom = self.screen_rect.bottom

        # Сохранение вещественной координаты центра корабля
        self.center = float(self.rect.centerx)

        # Флаг перемещения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''Обновляет позиция корабля с учетом флага'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Обновление атрибута rect на основании self.center
        self.rect.centerx = self.center

    def blitme(self):
        '''Рисует корабль в текущей позиции'''
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        '''Размещает корабль в центре нижней стороны'''
        self.center = self.screen_rect.centerx