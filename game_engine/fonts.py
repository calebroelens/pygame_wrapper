import pygame


class FontLibrary(dict[str, pygame.font.Font]):

    def __init__(self):
        super().__init__()

    def add_font(self, font_key, *args, **kwargs):
        self[font_key] = pygame.font.SysFont(*args, **kwargs)
