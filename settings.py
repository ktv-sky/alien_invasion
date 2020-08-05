class Settings():
    '''Класс для хранения всех настроек игры'''

    def __init__(self):
        '''Инициализирует статические настройки игры'''
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Настройки корабля  
        self.ship_limit = 3

        # Параметры пули  
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 230, 230, 230
        self.bullets_allowed = 5    
        self.fleet_drop_speed = 10
        
        # Темп ускорения игры
        self.speedup_scale = 1.2
        # Темп роста стоимости пришельцев
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''Инициализирует настройки, изменяющиеся в ходе игры'''
        self.ship_speed_factor = 5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        # fleet_direction = 1 обозначает движение вправо, а -1 - влево
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        '''Увеличивает настройки скорости'''
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)