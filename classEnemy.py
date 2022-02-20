import pygame
from settings import USER_SCREEN_W

walk = {pygame.image.load("Tiles/Bots/Bot1/Run/Armature_run_00.png"),
        pygame.image.load("Tiles/Bots/Bot1/Run/Armature_run_01.png"),
        pygame.image.load("Tiles/Bots/Bot1/Run/Armature_run_02.png"),
        pygame.image.load("Tiles/Bots/Bot1/Run/Armature_run_03.png"),
        pygame.image.load("Tiles/Bots/Bot1/Run/Armature_run_04.png"),
        pygame.image.load("Tiles/Bots/Bot1/Run/Armature_run_05.png"),
        pygame.image.load("Tiles/Bots/Bot1/Run/Armature_run_06.png"),
        pygame.image.load("Tiles/Bots/Bot1/Run/Armature_run_07.png"),
        pygame.image.load("Tiles/Bots/Bot1/Run/Armature_run_08.png"),
        pygame.image.load("Tiles/Bots/Bot1/Run/Armature_run_09.png"),
        pygame.image.load("Tiles/Bots/Bot1/Run/Armature_run_10.png")}

'''walk = [pygame.image.load("Tiles\Character\Animation\Run\Run_01.PNG"),
        pygame.image.load("Tiles\Character\Animation\Run\Run_02.PNG"),
        pygame.image.load("Tiles\Character\Animation\Run\Run_03.PNG"),
        pygame.image.load("Tiles\Character\Animation\Run\Run_04.PNG"),
        pygame.image.load("Tiles\Character\Animation\Run\Run_05.PNG"),
        pygame.image.load("Tiles\Character\Animation\Run\Run_06.PNG"),
        pygame.image.load("Tiles\Character\Animation\Run\Run_07.PNG"),
        pygame.image.load("Tiles\Character\Animation\Run\Run_08.PNG")]'''

ENEMY_W = 200
ENEMY_H = 200
SPEED = 10
JUMP = 20
runAnimation = []

for image in walk:
    runAnimation.append(pygame.transform.scale(image, (ENEMY_W, ENEMY_H)))


class Enemy(pygame.sprite.Sprite):
    def __init__(self, groups, x, y, width, height):
        super().__init__(groups)

        self.animCount = 0
        self.image = runAnimation[self.animCount]
        self.rect = self.image.get_rect(x=x, bottom=y + height + 500)
        self.speedX = 0
        self.Left = False
        self.hp = 2
        # Движение по Y
        self.speedY = 0
        self.grav = 2  # гравитация - скорость движения вниз
        self.onGrond = True  # Стоит на земле
        self.isJump = False  # прыгает или нет
        self.GROUND = y + height + 40
        self.y = y
        self.x = x
        self.range = 40
        self.hhp = 0

    def update(self, herogroup):
        """
        Функция запускается из главной программы постоянно(в цикле)
        :param platforms:
        :return:
        """
        self.herogroup = herogroup
        keys = pygame.key.get_pressed()

        # враг ходит от края я к краю

        if self.Left == False:
            self.speedX = SPEED
            if self.rect.right > USER_SCREEN_W:
                self.speedX = 0
                self.Left = True
        if self.Left == True:
            self.speedX = -SPEED
            if self.rect.right < 150:
                self.speedX = 0
                self.Left = False

        self.rect.x += self.speedX


        #
        # if keys[pygame.K_SPACE] and self.onGrond:
        #     self.speedY -= JUMP
        #     self.onGrond = False
        #
        # self.rect.x += self.speedX
        self.rect.y += self.speedY
        #
        if not self.onGrond:
            self.speedY += self.grav
        #
        if self.rect.bottom >= self.GROUND:
            self.rect.bottom = self.GROUND
            self.onGrond = True
            self.speedY = 0

        self.animation()
        #self.check_collizion(platforms)
        if keys[pygame.K_e]:

            self.attacka()
            if self.hhp == 9:
                pygame.quit()

    def check_collizion(self, platforms):
        """
        Проверка на столкновение с платформами
        :return:
        """
        if pygame.sprite.spritecollideany(self, platforms):

            if self.speedY != 0:
                if self.speedY > 0:
                    self.onGrond = True
                self.speedY = 0
        else:
            self.speedY += self.grav

    def animation(self):
        '''
        ВСЯ АНИМАЦИЯ ПЕРСОНАЖА
        :return:
        '''

        if self.speedX != 0:  # Если скорость по Х не нулевая, значит я иду
            self.animCount += 1  # Счётчик подсчитывает, какую картинку по счёту я должен показать
            if self.animCount == len(runAnimation):  # если я дошёл до последней картинки в списке картинок
                self.animCount = 0  # то обнуляю счётчик, чтобы начать сначала

            self.image = runAnimation[self.animCount]  # Достаю картинку с нужным номером из списка
            if self.speedX > 0:  # Если двигаюсь вправо,
                self.image = pygame.transform.flip(self.image, True, False)  # то отзеркаливаю картинку персонажа

    def get_coords(self):
        return self.x, self.y

    def attacka(self):
        hits = pygame.sprite.spritecollide(self, self.herogroup, False, pygame.sprite.collide_circle)
        if hits:
            print('ac')
            self.hhp += 1
            return True
