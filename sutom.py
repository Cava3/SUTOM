#!/bin/python3
"""SUTOM main program file.
Checks the command line arguments and calls the appropriate functions.
"""

import sys
import time as t
import random
import os
from sutom.game import Game

def main():
    """Main function."""

    input_file = "words.txt"
    if len(sys.argv) == 2:
        input_file = sys.argv[1]
    
    if not os.path.isfile(input_file):
        print("File not found : " + input_file)
        exit(1)

    words = []
    with open(input_file, "r") as f:
        words = f.read().splitlines()

    word = random.choice(words)

    game: Game = Game(word)
    game.run()


if __name__ == "__main__":
    main()
