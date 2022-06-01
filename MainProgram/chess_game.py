import string
import pygame as pg
import numpy as np
import Graphics


# makes window size a mulitple of board size (8)
FEN_STARTING_BOARD = str("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")


clock = pg.time.Clock()
# (9,10) is the center of square 1 with the blocksize being 75


def coords(Coordinates):
    file = ((ord(Coordinates[0].upper()) - 64) * 75) - 66
    rank = ((9-int(Coordinates[1])) * 75) - 65

    if ord(Coordinates[0].upper()) - 64 < 1 or ord(Coordinates[0].upper()) - 64 > 8:
        raise Exception('Invalid rank')
    elif int(Coordinates[1]) < 1 or int(Coordinates[1]) > 8:
        raise Exception('Invalid file')

    return file, rank

class Position:

    returned_position = np.array([9, 9], dtype='S1')

    # //////
    # if constructor is empty then the starting position is made
    # otherwise, the custom position that has been inputted will be returned
    # //////

    def __init__(self, arg=None):
        if isinstance(arg, str):  # if there is a fen string
            self.returned_position = Position.FEN_to_board(arg)
        else:
            self.returned_position = Position.FEN_to_board(
                FEN_STARTING_BOARD)  # if parameter has been left empty

    def FEN_to_board(FEN: string):
        temp_board = np.zeros([9, 9], dtype='S1')
        Xcount = 1
        Ycount = 1
        i = 0
        final_rank = False
        finished_iterating = False

        while not finished_iterating:

            if ord(FEN[i]) - 48 > 0 and ord(FEN[i]) - 48 <= 8:  # if is a number between 1 and 8
                for j in range(0, ord(FEN[i]) - 48):
                    temp_board[Ycount, Xcount+j] = 'e'
                Xcount += ord(FEN[i]) - 49
            elif not FEN[i] == '/':
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


class Board:

    _board = np.zeros([8, 8], dtype='S1')

    def __init__(self, Position):  # pass in a 2d array for position
        self._board = Position

    def square_location(self):
        print(self._board)

    def get_clicked_square(event_coords):
        x, y = event_coords
        file = (x + 66) / 75
        rank = (y + 65) / 75


# //////
# HOW TO DETECT MOUSE POSITION AND WHAT COORDINATE ITS IN
# when clicked, divide coords by boardsize and always round down
# //////

if __name__ == "__main__":
    global SCREEN
    pg.init()
    mouse_down = False

    font = pg.font.SysFont("Arial", 18)

    SCREEN = pg.display.set_mode((Graphics.WINDOWS_SIZE, Graphics.WINDOWS_SIZE))
    SCREEN.fill(Graphics.BLACK)

    position = Position().returned_position

    Graphics.load_images()

    Graphics.draw_grid(SCREEN)

    Graphics.draw_piece(SCREEN, 'Q', coords('b2'))

    testarr = SCREEN.copy()
    
    run = True
    testarr.convert()
    pg.transform.scale(testarr, (Graphics.WINDOWS_SIZE, Graphics.WINDOWS_SIZE))
    
    while run:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_down = True
            elif event.type == pg.MOUSEBUTTONUP:
                mouse_down = False

        if mouse_down:
            SCREEN.blit(testarr, (0, 0))
            Graphics.draw_piece_at_mousepos(SCREEN, 'r', pg.mouse.get_pos())

        # fps = font.render(str(int(clock.get_fps())), True, pg.Color('white'))
        # SCREEN.blit(fps, (50, 50))

        pg.display.flip()
    pg.quit()
