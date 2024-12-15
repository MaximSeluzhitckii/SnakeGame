import pygame as pg

import game_config
import game_config as config
from game_objects.apple import Apple
from game_dialog import GameDialog
from game_objects.snake import Snake


def load_img(name):
    img = pg.image.load(name)
    # img = img.convert()
    # colorkey = img.get_at((0, 0))
    # img.set_colorkey(colorkey)
    img = pg.transform.scale(img, config.WINDOW_SIZE)
    return img

class SnakeGame():
    """Базовый класс для запуска игры"""
    def __init__(self):
        # Фон игры
        self.background = load_img("picture/grass.png")
        # Скорость обновления кадров
        self.__FPS = config.FPS
        self.__clock = pg.time.Clock()

        # Создаем объект класса GameDialog
        self.__game_dialog = GameDialog()

        # Вызываем метод инициализациии остальных параметров
        self.__init_game()

    def __init_game(self):

        # Текущее значение очков игрока
        self.__current_player_score = 0

        # Создаем объект основного окна
        self.screen = pg.display.set_mode(game_config.WINDOW_SIZE)
        pg.display.set_caption("Змейка")

        # Cписок яблок
        self.apples = pg.sprite.Group()
        self.apple_count = 1

        # Объект змейки
        self.snake = Snake(self.screen)

        # В начале игры будет всего одно яблоко
        for i in range(self.apple_count):
            # Объект яблока
            apple = Apple(self.screen)
            self.apples.add(apple)


    def __draw_scene(self):
        # отрисовка
        self.screen.blit(self.background, (0, 0))

        self.apples.draw(self.screen)
        self.snake.update()
        self.snake.draw()

        # Обновляем экран
        pg.display.update()
        pg.display.flip()
        self.__clock.tick(self.__FPS)
        self.chek_collision()
        self.__draw_score()

    def run_game(self, game_is_run):
        # Основной цикл игры
        while game_is_run:
            # Обрабатываем событие закрытия окна
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()

            # Отрисовываем всё
            self.__draw_scene()

    def chek_collision(self):
        list_colid = pg.sprite.spritecollide(self.snake, self.apples, False)
        if len(list_colid) > 0:
            if self.__game_dialog.show_dialog_game_over():
                self.__init_game()
            else:
                exit()

        for apple in self.apple:
            if apple.rect.y > self.screen.get_height():
                self.__current_player_score += 1
                self.apple.remove(apple)
                self.all_sprites.remove(apple)

                if self.__current_player_score % 3 == 0:
                    self.count_apple += 1

        if len(self.apple) < self.count_apple:
            newApple = Apple(self.screen)
            self.all_sprites.add(newApple)
            self.apple.add(newApple)

    def __draw_score(self):
        font = pg.font.Font(None, 28)
        text_name = font.render(f'Игрок: {self.__playername}', True, 'white')
        text_name_rect = text_name.get_rect(topleft=(10, 30))
        self.screen.bilt(text_name, text_name_rect)

        text_score = font.render(f'Очки: {self.__player_core}', True, 'white')
        text_score_rect = text_score.get_rect(topleft=(10, 50))
        self.screen.bilt(text_score, text_score_rect)