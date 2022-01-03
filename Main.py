import pygame
from classHero import Hero
from class_menu import Menu
from level import level
from settings import USER_SCREEN_H, USER_SCREEN_W



# настраиваем экран
pygame.init()
win = pygame.display.set_mode((USER_SCREEN_W, USER_SCREEN_H), pygame.FULLSCREEN)
pygame.display.set_caption("хз")

bg = pygame.image.load('Tiles/bg/bg.png')
bg = pygame.transform.scale(bg, (USER_SCREEN_W, USER_SCREEN_H))

# Тамер и фпс
clock = pygame.time.Clock()
FPS = 120

# Группы
all_sprites_group = pygame.sprite.Group()  # Группа вообще всех игровы объектов

hero = Hero(all_sprites_group, USER_SCREEN_H)  # Создаём персонажа по шаблону из класса


def drawWindow():
    win.blit(bg, (0, 0))  # фон
    platform_group.draw(win)  # Отрисвываем уровень
#    enemy_group.draw(win) враги в будущем
#    bot_group.draw(win) боты в будущем
    win.blit(hero.image, hero.rect)  # главный герой
    pygame.display.update()  # обновление экрана
