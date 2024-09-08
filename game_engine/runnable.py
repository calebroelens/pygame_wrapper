import pygame


class GameRunnable:

    def __init__(self, method):
        self._method = method
        self._running = False

    def run(self):
        while self._running:
            self._method()
