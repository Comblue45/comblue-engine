import pygame
from .sound import Sound

class Audio:
    """Class which contains all functions to manage audio in Tiny Engine."""
    background_state = "None"

    @classmethod
    def play_sound(cls, sound: Sound) -> None:
        """Plays a sound which must be an instance of the Sound class."""
        if not isinstance(sound, Sound):
            raise TypeError("sound must be of type Sound")
        sound.sound.play()

    @classmethod
    def load_background(cls, path: str) -> None:
        """Loads the background music for a game."""
        if not isinstance(path, str):
            raise TypeError("path must be of type str")
        pygame.mixer.music.load(path) # Add try and exept statement
        cls.background_state = "Loaded"
    
    @classmethod
    def play_background(cls, loop: int = 0) -> None:
        """Starts playing the background music for a game."""
        if not isinstance(loop, int):
            raise TypeError("loop must be of type int")
        pygame.mixer.music.play(loop)
        cls.background_state = "Playing"
 
    @classmethod
    def pause_background(cls) -> None:
        """Pauses the background music for a game."""
        pygame.mixer.music.pause()
        cls.background_state = "Paused"

    @classmethod
    def resume_background(cls) -> None:
        """Unpauses the background music for a game."""
        pygame.mixer.music.unpause()
        cls.background_state = "Playing"