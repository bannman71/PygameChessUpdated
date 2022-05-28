import string
from tkinter.tix import IMAGE
import pygame as pg
import numpy as np
import random

BLACK = (118, 150, 86)
WHITE = (238, 238, 210)
BOARD_SIZE = 8
# makes window size a mulitple of board size (8)
WINDOW_SIZE = (600 // BOARD_SIZE) * BOARD_SIZE
BLOCK_SIZE = WINDOW_SIZE / BOARD_SIZE
FEN_STARTING_BOARD = str("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")
IMAGES = {}

# (9,10) is the center of square 1 with the blocksize being 75
#9 , 84, 157.5
#10, 85,


class Player:
    _player1 = "white"
    _player2 = "black"
    empty = -1
    Pieces = ['b_bishop', 'b_king', 'b_knight', 'b_pawn', 'b_queen', 'b_rook',
              'w_bishop', 'w_king', 'w_knight', 'w_pawn', 'w_queen', 'w_rook']


class Position:

    _returned_position = np.array([9, 9], dtype='S1')

    # //////
    # if constructor is empty then the starting position is made
    # otherwise, the custom position that has been inputted will be returned
    # //////

    def __init__(self, FEN_string: string):
        self._returned_position = Position.FEN_to_board(FEN_string)

    def __init__(self):  # if no constructor
        self._returned_position = Position.FEN_to_board(
            FEN_STARTING_BOARD)

    def FEN_to_board(FEN: string):
        temp_board = np.zeros([9, 9], dtype='S1')
        Xcount = 1
        Ycount = 1
        i = 0
        final_rank = False
        finished_iterating = False

        while not finished_iterating:
            is_num = False

            if ord(FEN[i]) - 48 > 0 and ord(FEN[i]) - 48 <= 8:
                is_num = True
                for j in range(0, ord(FEN[i]) - 48):
                    temp_board[Ycount, Xcount+j] = 'e'
                Xcount += ord(FEN[i]) - 49

            if not FEN[i] == '/' and not is_num:
                # print("fen is {} at {}".format(FEN[i], i))
                # print("X: {}  ||  Y: {}".format(Xcount, Ycount))
                temp_board[Ycount, Xcount] = FEN[i]

            if Xcount == 9:  # if at the end of the rank
                Ycount += 1  # go to next one
                Xcount = 1
            else:
                Xcount += 1

            if final_rank == True and Xcount == 9:  # has finished the entire board
                finished_iterating = True

            if Ycount == 8:
                final_rank = True

            i += 1
        return temp_board

    def starting_position(self):
        return "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'"


class Board:

    _board = np.zeros([9, 9], dtype='S1')

    def __init__(self, Position):  # pass in a 2d array for position
        self._board = Position

    def square_location(self):
        print(self._board)


class Graphics:

    def __init__(self):
        pass

    def load_images():
       # index = 0
        for im in Player.Pieces:
            IMAGES[im] = (pg.transform.smoothscale(
                pg.image.load("/Users/maxscullion/Projects/PygameChess/classic_hq/" + im + ".png"), (BLOCK_SIZE * 0.75, BLOCK_SIZE * 0.75)))
            #index += 1

    def draw_grid():
        for y in range(0, BOARD_SIZE):
            for x in range(0, BOARD_SIZE//2):
                rect = pg.Rect(
                    (x*2 + ((y + 1) % 2)) * BLOCK_SIZE, y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                pg.draw.rect(SCREEN, WHITE, rect, 64)

    # draw_piece('r',x,y)

    def draw_piece(colour, piece_name, xytuple):
        x, y = xytuple

        if float.is_integer((x+66) / 75) == False or float.is_integer((y + 65) / 75) == False:
            raise Exception('Must be a valid coordinate')

        SCREEN.blit(IMAGES[colour[0] + '_' + piece_name], (x, y))


if __name__ == "__main__":
    global SCREEN
    pg.init()

    SCREEN = pg.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    SCREEN.fill(BLACK)

    run = True

    Graphics.draw_grid()
    Graphics.load_images()

    Graphics.draw_piece('b', 'queen', (9, 160))

    while run:

        #help = Graphics.test()
        # Board(0).square_locatio

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            if event.type == pg.MOUSEBUTTONDOWN:
                x, y = event.pos

        pg.display.update()
