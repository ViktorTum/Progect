import pygame

platform_image = pygame.image.load("Tiles/Map/untitled - 2020-08-01T144248.637.png")


class Platform(pygame.sprite.Sprite):
    def __init__(self, groups, x, y, w, h):
        super().__init__(groups)
        self.image = pygame.transform.scale(platform_image, (180, 180))
        self.rect = self.image.get_rect(x=x, y=y)
