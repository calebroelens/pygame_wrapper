import pygame
from game_engine.game import Game


class GameKeyEventManager:

    def __init__(self):
        self._register = {}
        self._register_key_down = {}
        self._register_key_up = {}

    def update(self, game: Game):
        # Todo: Make this generic
        for event in pygame.event.get():
            if event.type in self._register:
                for event_function in self._register[event.type]:
                    event_function(game, event)
            # Iterate event register
            event_register = {}
            match event.type:
                case pygame.KEYUP:
                    event_register = self._register_key_up
                case pygame.KEYDOWN:
                    event_register = self._register_key_down

            if event_register:
                if event.key in event_register:
                    for event_function in event_register[event.key]:
                        event_function(game, event)

    def register(self, event: type):
        def wrap(f):
            self._register.setdefault(event, []).append(f)
            return f
        return wrap

    def register_keydown(self, key: pygame.constants):
        def wrap(f):
            self._register_key_down.setdefault(key, []).append(f)
            return f
        return wrap

    def register_keyup(self, key: pygame.constants):
        def wrap(f):
            self._register_key_up.setdefault(key, []).append(f)
            return f
        return wrap


