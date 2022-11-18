"""This file manages the SUTOM display options.
It's used to display the game's state, the game's result along with other utils.
"""
import os

class Displayer():
    """Manages the display part of the SUTOM game
    """
    def __init__(self, game):
        """Initializes the displayer.
        """
        self.game = game
        
        self.clear()

    def clear(self):
        """Clears the terminal."""
        os.system('cls' if os.name == 'nt' else 'clear')
