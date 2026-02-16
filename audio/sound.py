import pygame.mixer

class Sound:
    """Sound class for adding sound to a game in Tiny Engine."""

    def __init__(self, path: str) -> None:
        """Initialises an instance of the Sound class."""
        self.sound = pygame.mixer.Sound(path)
    
    def set_volume(self, new_volume: int|float) -> None:
        """Sets the volume of the sound instance."""
        if not isinstance(new_volume, (int, float)):
            raise TypeError("new_volume must be of type int")
        if (new_volume > 1.0) or (new_volume < 0.0):
            raise TypeError("new_volume must be a value between 0.0 and 1.0")
        self.sound.set_volume(new_volume)