"""The SUTOM game's control file.
It manages the course of the game.
"""
import sutom.displayer as dis

MAX_ROUNDS: int = 6

class Game():
    """Represents a SUTOM game"""

    def __init__(self, word):
        """Initializes the game."""
        self.word: str = word
        self.found: bool = False
        self.rounds: int = 0
        self.displayer = dis.Displayer(self)

    def run(self):
        """Plays the game."""
        while not self.found and self.rounds < MAX_ROUNDS:
            self.displayer.clear()
            self.rounds += 1

