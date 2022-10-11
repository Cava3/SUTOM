"""SUTOM main program file.
Checks the command line arguments and calls the appropriate functions.
"""

import sys
import time as t
from sutom import Game

def main():
    """Main function."""
    if len(sys.argv) != 2:
        print("Usage: sutom.py <word>")
        sys.exit(1)

    input_file = sys.argv[1]
    print("Chosen word: " + input_file)

    t.sleep(1)
    game: Game = Game(input_file)


if __name__ == "__main__":
    main()
