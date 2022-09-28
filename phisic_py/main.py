import os
from cinetica.mu import Game

if __name__ == "__main__":
    HEIGHT, WIDTH = 600, 1200
    WHITE, BLACK = (210, 210, 210), (0, 0, 0, 0.8)
    FONT = ('comicsans', 16)

    game = Game((WIDTH, HEIGHT), "Movimento Uniforme", FONT)
    game.run()
