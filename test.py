from game_engine.game import Game
import pygame, sys

game = Game(256, 256, target_framerate=144)


@game.events.register(pygame.QUIT)
def quit_game(g: Game, event: pygame.event.Event):
    pygame.quit()
    sys.exit()


@game.events.register(pygame.KEYDOWN)
def pressing_a_key(g: Game, event: pygame.event.Event):
    print(f"Any key: {event.key}")


@game.events.register_keydown(pygame.K_SPACE)
def pressed_space(g: Game, event: pygame.event.Event):
    print("Pressed space down")


@game.events.register_keyup(pygame.K_SPACE)
def pressed_space_up(g: Game, event: pygame.event.Event):
    print("Pressed space up")


game.run()