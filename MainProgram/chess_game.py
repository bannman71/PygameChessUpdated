from pydoc import Helper
import string
import pygame as pg
import Graphics
import Board

# makes window size a mulitple of board size (8)
FEN_STARTING_BOARD = str("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")

# (9,10) is the center of square 1 with the blocksize being 75


class Position:
    pos = [[' '] * 8 for i in range(8)]

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

    def draw(self):
        for row in range(8):
            for col in range(8):
                if self.pos[row][col] != "e":
                    # notice row column is flipped for the graphical position because x = col and y = row
                    Graphics.draw_piece(SCREEN, self.pos[row][col], (col, row))

    def update(self, clicked_piece, sCoords, dCoords):
        sCol, sRow = sCoords
        dCol, dRow = dCoords

        self.pos[sRow][sCol] = 'e'
        self.pos[dRow][dCol] = clicked_piece

    def FEN_to_board(FEN: string):
        temp_board = [[' '] * 8 for i in range(8)]
        col = 0
        row = 0
        i = 0
        final_rank = False
        finished_iterating = False

        while not finished_iterating:
            if ord(FEN[i]) - 48 > 0 and ord(FEN[i]) - 48 <= 8:  # if is a number between 0 and 8
                for j in range(0, ord(FEN[i]) - 48):  # 0->7 maximum
                    temp_board[row][col + j] = 'e'
                col += ord(FEN[i]) - 49
            elif not FEN[i] == '/':
                temp_board[row][col] = FEN[i]

            if col == 8:  # if at the end of the rank
                row += 1  # go to next one
                col = 0
            else:
                col += 1

            if final_rank == True and col == 8:  # has finished the entire board
                finished_iterating = True

            if row == 7:
                final_rank = True

            i += 1
        return temp_board


if __name__ == "__main__":
    global SCREEN
    pg.init()
    mouse_down = False
    start_clicked_square = 0
    destination_clicked_square = 0

    SCREEN = pg.display.set_mode((Graphics.WINDOW_SIZE, Graphics.WINDOW_SIZE))
    SCREEN.fill(Graphics.BLACK)

    Graphics.draw_grid(SCREEN)
    empty_board = SCREEN.copy()

    position = Position()

    Graphics.load_images()

    position.draw()
    current_pos = SCREEN.copy()

    run = True

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_down = True

                clicked_piece = Board.get_piece_at_clicked_location(
                    position.pos, pg.mouse.get_pos())

                start_clicked_square = Board.get_coord_at_click_location(
                    pg.mouse.get_pos())

            elif event.type == pg.MOUSEBUTTONUP:
                mouse_down = False
                destination_clicked_square = Board.get_coord_at_click_location(
                    pg.mouse.get_pos())

                if Board.legal_moves(clicked_piece).is_legal(start_clicked_square, destination_clicked_square) == True:
                    position.update(
                        clicked_piece, start_clicked_square, destination_clicked_square)

                SCREEN.blit(empty_board, (0, 0))
                position.draw()
                current_pos = SCREEN.copy()

        if mouse_down and clicked_piece != 'e':
            SCREEN.blit(current_pos, (0, 0))
            Graphics.draw_piece_at_mousepos(
                SCREEN, clicked_piece, pg.mouse.get_pos())

        pg.display.flip()
    pg.quit()
