from pygame import Surface, image


class GameSurface(Surface):
    """
    A single game surface
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def from_file(cls, location: str):
        """
        Create a surface from a local image file
        :return:
        """
        return image.load(location).convert_alpha()


class GameSurfaceCollection(list[GameSurface]):
    """
    A collection of game surfaces: For use in animations
    """
    pass


class GameSurfaceDictionary(dict[GameSurface]):
    """
    A collection of game surfaces: For use in animations or state animations (connect variables to game surface)
    """
    pass


class GameTextSurface:

    def __init__(self):
        pass
