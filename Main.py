import pygame
from ClassHero import Hero
from Menu import Menu
from level import level1
from settings import USER_SCREEN_H, USER_SCREEN_W
from classPlatform import Platform
from classEnemy import Enemy
from classBird import Bird

# настраиваем экран
pygame.init()
win = pygame.display.set_mode((USER_SCREEN_W, USER_SCREEN_H), pygame.FULLSCREEN)
pygame.display.set_caption("хз")

bg = pygame.image.load('Tiles/bg/bg.png')
bg = pygame.transform.scale(bg, (USER_SCREEN_W, USER_SCREEN_H))

# Тамер и фпс
clock = pygame.time.Clock()
FPS = 60

# Группы
eng = []
all_sprites_group = pygame.sprite.Group()  # Группа вообще всех игровы объектов
platform_group = pygame.sprite.Group()  # Группа платформ
enemy_group = pygame.sprite.Group()  # Группа врагов
bot_group = pygame.sprite.Group()  # Группа животных
for i in range(len(enemy_group)):
    eng.append(Enemy)
hero = Hero(all_sprites_group, USER_SCREEN_H, enemy_group)  # Создаём персонажа по шаблону из класса
hero_group = pygame.sprite.Group()
hero_group.add(hero)

# def draw_level():
#    Отрисовываем статичный фон
# Создаём персонажа по шаблону из класса

GRASS = pygame.image.load("Tiles/Map/untitled - 2020-08-01T143755.478.png")  # трава

TREE1 = pygame.image.load("Tiles/Map/untitled - 2020-07-17T194613.279.png")  # дерево№1
TREE2 = pygame.image.load("Tiles/Map/untitled - 2020-07-17T195149.536.png")  # дерево№2
TREE3 = pygame.image.load("Tiles/Map/untitled - 2020-07-17T195540.200.png")  # дерево№3
TREE4 = pygame.image.load("Tiles/Map/untitled - 2020-07-17T194842.678.png")  # дерево№4

FLOWER1 = pygame.image.load("Tiles/Map/untitled - 2020-07-17T200113.601.png")  # цветок№1
FLOWER2 = pygame.image.load("Tiles/Map/untitled - 2020-07-17T200151.579.png")  # цветок№2

GRASS_sprite = pygame.transform.scale(GRASS, (650, 650))  # уменьшение размера травы

TREE1_sprite = pygame.transform.scale(TREE1, (250, 250))  # уменьшение размера дерева1
TREE2_sprite = pygame.transform.scale(TREE2, (450, 450))  # уменьшение размера дерева2
TREE3_sprite = pygame.transform.scale(TREE3, (650, 650))  # уменьшение размера дерева3
TREE4_sprite = pygame.transform.scale(TREE4, (465, 465))  # уменьшение размера дерева4

FLOWER1_sprite = pygame.transform.scale(FLOWER1, (150, 150))  # уменьшение размера цветка1
FLOWER2_sprite = pygame.transform.scale(FLOWER2, (125, 125))  # уменьшение размера цветка2


def drawWindow():
    win.blit(bg, (0, 0))  # фон
    platform_group.draw(win)  # Отрисвываем уровень
    enemy_group.draw(win)
    bot_group.draw(win)  # боты в будущем
    win.blit(hero.image, hero.rect)  # главный герой
    pygame.display.update()  # обновление экрана


def showMenu():
    #    стартовое меню
    menu = Menu(win)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_UP:
                    menu.up()
                if event.key == pygame.K_DOWN:
                    menu.down()
                if event.key == 13:
                    if menu.activeButton == 0:  # Если выбрано "START GAME"
                        return
                    elif menu.activeButton == 1:
                        pygame.quit()

        menu.update()


def draw_level():
    bg.blit(TREE1_sprite, TREE1_sprite.get_rect(x=635, y=750))  # создание дерева1
    bg.blit(TREE2_sprite, TREE2_sprite.get_rect(x=65, y=550))  # создание дерева2
    bg.blit(TREE3_sprite, TREE3_sprite.get_rect(x=800, y=425))  # создание дерева3
    bg.blit(TREE4_sprite, TREE4_sprite.get_rect(x=1500, y=565))  # создание дерева4

    bg.blit(FLOWER1_sprite, FLOWER1_sprite.get_rect(x=1250, y=880))  # создание цветка1
    bg.blit(FLOWER2_sprite, FLOWER2_sprite.get_rect(x=120, y=890))  # создание цветка2

    bg.blit(GRASS_sprite, GRASS_sprite.get_rect(x=0, y=630))  # создание травы
    bg.blit(GRASS_sprite, GRASS_sprite.get_rect(x=635, y=630))
    bg.blit(GRASS_sprite, GRASS_sprite.get_rect(x=635 * 2, y=630))


def create_platforms():
    # все
    platformSizeX = USER_SCREEN_W // len(level1[0])
    platformSizeY = USER_SCREEN_H // len(level1)

    x = 0
    y = 0
    for line in level1:
        for b in line:
            if b == "H":
                # Перемещаем ГГ на спавн
                hero.rect.x = x
                hero.rect.y = y
            elif b == 1:  # Создаём спрайт платформы
                Platform((all_sprites_group, platform_group), x, y, platformSizeX, platformSizeY)
            elif b == "E":
                # Создаём спрайт врага
                Enemy((all_sprites_group, enemy_group), x, y, platformSizeX, platformSizeY)
            elif b == "B":
                Bird((all_sprites_group, bot_group), x, y, platformSizeX, platformSizeY)

            x += platformSizeX
        x = 0
        y += platformSizeY


showMenu()
create_platforms()
draw_level()

run = True
while run:
    clock.tick(FPS)  # ограничиваем ФПС
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Если нажали на крестикв углу (его не видно в фуллскрин)
            run = False
        if event.type == pygame.KEYDOWN:  #
            if event.key == pygame.K_ESCAPE:
                run = False

    hero.update(platform_group)  # Обновляем героя
    enemy_group.update(hero_group)
    bot_group.update()
    # all_sprites_group.update()
    drawWindow()  # обновляем экран

pygame.quit()
