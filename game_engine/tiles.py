import pygame
from typing import Union


class GameSprite(pygame.sprite.Sprite):

    def __init__(self, position: tuple, size: Union[int, tuple[int, int]]):
        """
        Game sprite class
        :param position:
        :param size:
        """
        super().__init__()
        if isinstance(size, int):
            size = (size, size)
        self.image = pygame.surface.Surface(size, flags=pygame.SRCALPHA)
        self.rect = self.image.get_rect(topleft=position)


class GameSpriteGroup(pygame.sprite.Group):

    def __init__(self, **sprites):
        super().__init__(self)
        self.add(sprites)
