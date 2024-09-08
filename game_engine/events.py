import pygame


class GameKeyEventManager:

    def __init__(self):
        self._register = {}
        self._register_key = {}

    def update(self):
        for event in pygame.event.get():
            if event.type in self._register:
                for event_function in self._register[event.type]:
                    event_function(event)
            if event.type == pygame.KEYDOWN:
                if event.key in self._register_key:
                    for event_function in self._register_key[event.key]:
                        event_function(event)

    def register(self, event: type):
        def wrap(f):
            self._register.setdefault(event, []).append(f)
            return f
        return wrap

    def register_keydown(self, key: pygame.constants):
        def wrap(f):
            self._register_key.setdefault(key, []).append(f)
            return f
        return wrap


