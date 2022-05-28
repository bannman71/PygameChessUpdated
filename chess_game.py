import string
import pygame as pg
import numpy as np

BLACK = (118, 150, 86)
WHITE = (238, 238, 210)
BOARD_SIZE = 8
# makes window size a mulitple of board size (8)
WINDOW_SIZE = (800 // BOARD_SIZE) * BOARD_SIZE
IMAGES = [0]*12

FEN_STARTING_BOARD = str("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")


class Player:
    _player1 = "white"
    _player2 = "black"
    empty = -1
    Pieces = ['b_bishop', 'b_king', 'b_knight', 'b_pawn', 'b_queen', 'b_rook',
              'w_bishop', 'w_king', 'w_knight', 'w_pawn', 'w_queen', 'w_rook']


class Position:

    _returned_position = [[0]*8]*8

    # //////
    # if constructor is empty then the starting position is made
    # otherwise, the custom position that has been inputted will be returned
    # //////

    def __init__(self, FEN_string: string):
        self._returned_position = FEN_STARTING_BOARD

    def __init__(self):  # if no constructor
        self._returned_position = Position.FEN_to_board(
            'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR/')

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

    _board = [[0]*8]*8

    def __init__(self, Position: Position):
        self._board = Position

    def square_location(self):
        print(self._board)


class Graphics:

    def __init__(self):
        pass

    def load_images():
        index = 0
        for im in Player.Pieces:
            IMAGES[index] = pg.transform.smoothscale(
                pg.image.load("/Users/maxscullion/Projects/PygameChess/classic_hq/" + im + ".png"), (100, 100))
            index += 1

    def draw_grid():
        blocksize = WINDOW_SIZE / BOARD_SIZE
        for y in range(0, BOARD_SIZE):
            for x in range(0, BOARD_SIZE//2):
                rect = pg.Rect(
                    (x*2 + ((y + 1) % 2)) * blocksize, y*blocksize, blocksize, blocksize)
                pg.draw.rect(SCREEN, WHITE, rect, 64)

    # draw_piece('r',x,y)

    def draw_piece(self, colour, piece_type, ):
        if colour == 'b':
            pass

# is lower case so b_
# search for


if __name__ == "__main__":
    global SCREEN
    pg.init()

    SCREEN = pg.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    SCREEN.fill(BLACK)

    print(Position()._returned_position[2][2])

    for x in range(1, 9):
        for y in range(1, 9):
            print(Position()._returned_position[x][y], end=' ')
        print()

    run = True
    while run:
        Graphics.draw_grid()
        Graphics.load_images()
        #help = Graphics.test()
        Board(0).square_location

        SCREEN.blit(IMAGES[2], (25, 25))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        pg.display.update()
