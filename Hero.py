import pygame
from settings import USER_SCREEN_H, USER_SCREEN_W


    def animation(self):
#        ВСЯ АНИМАЦИЯ ПЕРСОНАЖА


        #ATAKA
        if self.attack == True:
            self.animCount += 1   # Для ускоренной анимации атаки
            if self.animCount >= len(attackAnimation):    # если я дошёл до последней картинки в списке картинок
                self.animCount = 0        # то обнуляю счётчик, чтобы начать сначала
            self.image = attackAnimation[self.animCount]    # Достаю картинку с нужным номером из списка

        #БЕГ
        elif self.speedX != 0:  # Если скорость по Х не нулевая, значит я иду
            if self.animCount >= len(runAnimation):  # если я дошёл до последней картинки в списке картинок
                self.animCount = 0  # то обнуляю счётчик, чтобы начать сначала

            self.image = runAnimation[self.animCount]  # Достаю картинку с нужным номером из списка
            # if self.speedX > 0:  # Если двигаюсь вправо,
            #     self.image = pygame.transform.flip(self.image, True, False)  # то отзеркаливаю картинку персонажа

        #СТОИТ
        elif self.speedX == 0:  # иначе скорость = 0, значит стою на месте
            if self.animCount >= len(idleAnimation):
                self.animCount = 0
            self.image = idleAnimation[self.animCount]

        #Если направление вправо, то зеркалим картинку
        if self.idleLeft == False:
           self.image = pygame.transform.flip(self.image, True, False)

        self.animCount += 1  # Счётчик подсчитывает, какую картинку по счёту я должен показать
