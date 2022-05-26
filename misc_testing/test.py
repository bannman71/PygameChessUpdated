from matplotlib.style import context
import pygame as pg
import numpy as np
import chess
import chess.svg


BLACK = (118, 150, 86)
WHITE = (238, 238, 210)
BOARD_SIZE = 8
# must be muklitple of boardisez
WINDOW_SIZE = (800 // BOARD_SIZE) * BOARD_SIZE


def fill(surface, colour):
    w, h = pg.Surface.get_size(surface)
    r, g, b = colour
    for x in range(w):
        for y in range(h):
            # finds all colours that are white
            if pg.Surface.get_at(surface, (x, y)) == (0, 0, 0):
                pg.Surface.set_at(surface, (x, y), pg.Color(
                    r, g, b))  # changes them
            elif pg.Surface.get_at(surface, (x, y)) == (255, 255, 255):
                pg.Surface.set_at(
                    surface, (x, y), pg.Color(255-r, 255-g, 255-b))


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Board():

    def __init__(self):
        pass

    def create_grid(self):
        pass

    def draw_grid(self):
        blocksize = WINDOW_SIZE / BOARD_SIZE
        for y in range(0, BOARD_SIZE):
            for x in range(0, BOARD_SIZE//2):
                rect = pg.Rect(
                    (x*2 + ((y + 1) % 2)) * blocksize, y*blocksize, blocksize, blocksize)
                pg.draw.rect(SCREEN, WHITE, rect, 64)

    def draw_bishop(self, x, y):
        bishopImage = pg.image.load(
            r'/Users/maxscullion/Projects/PygameChess/classic_hq/Queen.svg')
        #fill(bishopImage, (0, 0, 0))
        bishopImage = pg.transform.smoothscale(bishopImage, (50, 50))
        SCREEN.blit(bishopImage, (x, y))

    def draw_board(self):
        board = chess.Board(
            "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")

        # calls the SVG render fuction, passes the above board and specifies the size in pixels.

        boardsvg = chess.svg.board(board, size=WINDOW_SIZE)
        outputfile = open('board.svg', "w")
        outputfile.write(boardsvg)
        outputfile.close()

        BoardImage = pg.image.load(
            r'/Users/maxscullion/Projects/PygameChess/board.svg')
        BoardImage = pg.transform.smoothscale(
            BoardImage, (WINDOW_SIZE, WINDOW_SIZE))

        SCREEN.blit(BoardImage, (0, 0))


if __name__ == "__main__":
    global SCREEN
    pg.init()

    SCREEN = pg.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    SCREEN.fill(BLACK)
    test = Board()

    run = True
    while run:
        test.draw_grid()
        # test.draw_board()
        test.draw_bishop(0, 0)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        pg.display.update()
