import string
import pygame as pg
import numpy as np
import Graphics
import Board

# makes window size a mulitple of board size (8)
FEN_STARTING_BOARD = str("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")

clock = pg.time.Clock()
# (9,10) is the center of square 1 with the blocksize being 75


class Position:

    pos = np.array([8, 8], dtype='S1')

    # //////
    # if constructor is empty then the starting position is made
    # otherwise, the custom position that has been inputted will be returned
    # //////

    def __init__(self, arg=None):
        if isinstance(arg, str):  # if there is a fen string
            self.pos = Position.FEN_to_board(arg)
        else:
            self.pos = Position.FEN_to_board(
                FEN_STARTING_BOARD)  # if parameter has been left empty

    def FEN_to_board(FEN: string):
        temp_board = np.zeros([8, 8], dtype='S1')
        Row = 0
        Col = 0
        i = 0
        final_rank = False
        finished_iterating = False

        while not finished_iterating:
            if ord(FEN[i]) - 48 > 0 and ord(FEN[i]) - 48 <= 8:  # if is a number between 0 and 8
                for j in range(0, ord(FEN[i]) - 48):  # 0->7 maximum
                    temp_board[Row, Col + j] = 'e'
                Col += ord(FEN[i]) - 49
            elif not FEN[i] == '/':
                temp_board[Row, Col] = FEN[i]

            if Col == 8:  # if at the end of the rank
                Row += 1  # go to next one
                Col = 0
            else:
                Col += 1

            if final_rank == True and Col == 8:  # has finished the entire board
                finished_iterating = True

            if Row == 7:
                final_rank = True

            i += 1
        return temp_board


if __name__ == "__main__":
    global SCREEN
    pg.init()
    mouse_down = False

    font = pg.font.SysFont("Arial", 18)

    SCREEN = pg.display.set_mode(
        (Graphics.WINDOW_SIZE, Graphics.WINDOW_SIZE))
    SCREEN.fill(Graphics.BLACK)

    position = Position()
    print(position.pos)

    Graphics.load_images()
    Graphics.draw_grid(SCREEN)

    testarr = SCREEN.copy()

    run = True
    testarr.convert()
    pg.transform.scale(testarr, (Graphics.WINDOW_SIZE, Graphics.WINDOW_SIZE))

    while run:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_down = True
            elif event.type == pg.MOUSEBUTTONUP:
                mouse_down = False

        if mouse_down:

            clicked_piece = Board.get_piece_at_clicked_location(
                position, pg.mouse.get_pos())
            print(clicked_piece)
            Graphics.draw_piece_at_mousepos(SCREEN, 'r', pg.mouse.get_pos())

        # fps = font.render(str(int(clock.get_fps())), True, pg.Color('white'))
        # SCREEN.blit(fps, (50, 50))

        pg.display.flip()
    pg.quit()
