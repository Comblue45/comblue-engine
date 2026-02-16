import pygame
from ..core.entity import Entity

class Label(Entity):
    """Label GUI Element."""

    def __init__(self,
                 game,
                 text: str = "",
                 font: pygame.font.Font = None, 
                 size: int|float = 50,
                 color: str|tuple[int, int, int] = (255, 255, 255),
                 position = (0, 0)):
        """Inistiates an instance of the Label class."""
        if not isinstance(text, str):
            raise TypeError("text must be of type str")
        if font:
            if not isinstance(font, pygame.font.Font):
                raise TypeError("font must be of type pygame.font.Font")
        if not isinstance(size, int):
            raise TypeError("size must be of type int")
        if size < 0:
            raise ValueError("size must be bigger than 0")
        if not isinstance(color, str):
            if isinstance(color, tuple):
                if not all(isinstance(element, int) for element in color):
                    raise TypeError("all elements of color as a tupel must be of type int")
                if not len(color) == 3:
                    raise ValueError("color as a tupel must be 3 elements long")
                if not all((element >= 0) and (element <= 255) for element in color):
                    raise ValueError("all elements of color as a tuple must be between 0 and 255 big")
            else:
                raise TypeError("color must be of type tupel or str")
        
        self.text = text
        self.size = size
        self.color = color
        self.font = font if font else pygame.font.Font(None, size=self.size)

        super().__init__(game, self.font.render(self.text, False, self.color), position)

    def update_label(self) -> None:
        """Updates every part of a label instance."""
        self.surface = self.font.render(self.text, False, self.color)
        last_pos = self.physics.topleft
        self.physics = self.surface.get_rect()
        self.physics.topleft = last_pos