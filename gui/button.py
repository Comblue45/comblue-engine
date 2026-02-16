import pygame
from .label import Label
from ..core.entity import Entity

class Button(Entity):
    """Button GUI Element."""

    def __init__(self,
                 game,
                 label: Label = None,
                 size: tuple[int, int] = (100, 100),
                 color: str|tuple[int, int, int] = "blue",
                 position: tuple[int, int] = (0, 0)) -> None:
        """Initialises an instance of the Button class ."""
        if label:
            if not isinstance(label, Label):
                raise TypeError("label must be of type Label")
        if not isinstance(size, tuple):
            raise TypeError("size must be of type tupel")
        if not all(isinstance(element, int) for element in size):
            raise TypeError("all elements of size must be of type int")
        if not len(size) == 2:
            raise ValueError("size must be 2 elements long")
        if not all(element > 0 for element in size):
            raise ValueError("all elements must be bigger than 0")
        if not isinstance(color, str):
            if isinstance(color, tuple):
                if not all(isinstance(element, int) for element in color):
                    raise TypeError("all elements of color as a tupel must be of type int")
                if not len(color) == 3:
                    raise ValueError("color as a tupel must be 3 elements long")
                if not all(element > 0 and element <= 255 for element in color):
                    raise ValueError("all elements of color as a tuple must be of type int")
            else:
                raise TypeError("color must be of type tupel or str")

        self.label = label
        self.size = size
        self.color = color

        super().__init__(game, pygame.Surface(self.size), position)
        
        self.surface.fill(self.color)
        self.label.physics.topleft = self.physics.topleft
        self.was_pressed = False

    def ready(self) -> None:
        """Makes sure that every part of the button gets rendered."""
        super().ready()
        self.game.current_scene.append(self.label)

    def update_button(self) -> None:
        """Updates every part of the button instance so the changes can get rendered."""
        self.surface = pygame.Surface(self.size)
        self.surface.fill(self.color)
        last_pos = self.physics.topleft
        self.physics = self.surface.get_rect()
        self.physics.topleft = last_pos

        self.label.physics.topleft = self.physics.topleft
        self.label.update_label()
    
    def update(self):
        """Triggers on_click and on_pressed events if needed."""
        super().update()
        if self.is_clicked():
            self.on_click()
            if not self.was_pressed:
                self.on_pressed()
            self.was_pressed = True
        else:
            self.was_pressed = False

    def on_click(self) -> None:
        """Method which gets called if a button instance gets clicked."""
        pass

    def on_pressed(self) -> None:
        """Method which gets called if a button instance gets pressed."""
        pass