import pygame
from settings import USER_SCREEN_H, USER_SCREEN_W
from ClassHero import walk, idle, Jump, attack


def animation(self):
    #        ВСЯ АНИМАЦИЯ ПЕРСОНАЖА

    # ATAKA
    if self.attack:
        self.animCount += 1  # Для ускоренной анимации атаки
        if self.animCount >= len(attack):  # если я дошёл до последней картинки в списке картинок
            self.animCount = 0  # то обнуляю счётчик, чтобы начать сначала
        self.image = attack[self.animCount]  # Достаю картинку с нужным номером из списка

    # БЕГ
    if self.speedX != 0:  # Если скорость по Х не нулевая, значит я иду
        if self.animCount >= len(walk):  # если я дошёл до последней картинки в списке картинок
            self.animCount = 0  # то обнуляю счётчик, чтобы начать сначала

        self.image = walk[self.animCount]  # Достаю картинку с нужным номером из списка
        # if self.speedX > 0:  # Если двигаюсь вправо,
        #     self.image = pygame.transform.flip(self.image, True, False)  # то отзеркаливаю картинку персонажа

    # СТОИТ
    elif self.speedX == 0:  # иначе скорость = 0, значит стою на месте
        if self.animCount >= len(idle):
            self.animCount = 0
        self.image = idle[self.animCount]

    # Если направление вправо, то зеркалим картинку
    if not self.idleLeft:
        self.image = pygame.transform.flip(self.image, True, False)

    self.animCount += 1  # Счётчик подсчитывает, какую картинку по счёту я должен показать
