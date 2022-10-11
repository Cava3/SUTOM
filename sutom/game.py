"""The SUTOM game's control file.
It manages the course of the game.
"""

MAX_ROUNDS: int = 6

class Game():
    """Represents a SUTOM game"""

    def __init__(self, word):
        """Initializes the game."""
        self.word: str = word
        self.found: bool = False
        self.rounds: int = 0

        self.loop()

    def loop(self):
        """Plays the game."""
        while not self.found and self.rounds < MAX_ROUNDS:

            self.rounds += 1

