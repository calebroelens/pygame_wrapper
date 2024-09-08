import pygame
from game_engine import fonts
from game_engine import events


class Game:

    def __init__(self, width: int, height: int, target_framerate: int = 60):
        pygame.display.init()
        pygame.font.init()
        self._screen = pygame.display.set_mode(size=(width, height))
        self._clock = pygame.time.Clock()
        self._font_library = fonts.FontLibrary()
        self._target_framerate = target_framerate
        # States
        self._running = True
        # Events
        self._events = events.GameKeyEventManager()

    def run(self):
        while self._running:
            self._events.update()
            pygame.display.update()
            self._clock.tick(self._target_framerate)

    @property
    def fonts(self):
        return self._font_library

    @property
    def events(self):
        return self._events
