from game_engine.game import Game
import pygame, sys

game = Game(256, 256)


@game.events.register(pygame.QUIT)
def quit_game(event: pygame.event.Event):
    pygame.quit()
    sys.exit()


@game.events.register_keydown(pygame.K_SPACE)
def pressed_space(event: pygame.event.Event):
    print("Pressed space")


game.run()