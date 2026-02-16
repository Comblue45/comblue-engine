import pygame

class ImageLoader:
    """Class which containts all functions to handle loadingen images in Tiny Engine."""

    @classmethod
    def load_sprite(cls, 
                    path: str,
                    scale_by: float = 1) -> pygame.Surface:
        """Loads an image by it's path and changes it scale if needed."""
        if not isinstance(path, str):
            raise TypeError("path must be of type str")
        if not isinstance(scale_by, int):
            raise TypeError("scale_by must be of type int")
        if scale_by < 0:
            raise TypeError("scale_by must be bigger than 0")
        return pygame.transform.scale_by(pygame.image.load(path) , scale_by) # Add try an exepct statment for pygame.image.load here