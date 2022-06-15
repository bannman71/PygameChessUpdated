import pygame as pg
from pyparsing import col
import Graphics

FEN_STARTING_BOARD = str("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")


def get_piece_at_clicked_location(position, clicked_coords):
    Col, Row = clicked_coords

    return position[Row // 75][Col // 75]


def get_coord_at_click_location(clicked_coords):
    Col, Row = clicked_coords

    return Col//75, Row//75

class Position:
    pos = [[' '] * 8 for up_iterator in range(8)]

    # //////
    # if constructor is empty then the starting position is made
    # otherwise, the custom position that has been inputted will be returned
    # //////

    def __init__(self, arg=None):
        if isinstance(arg, str):  # if there is a fen string
            self.pos = Position.FEN_to_board(arg)
        else:
            self.pos = Position.FEN_to_board(FEN_STARTING_BOARD)  # if parameter has been left empty

    def draw(self,surface):
        for row in range(8):
            for col in range(8):
                if self.pos[row][col] != "e":
                    # notice row column is flipped for the graphical position because x = col and y = row
                    Graphics.draw_piece(surface, self.pos[row][col], (col, row))

    def update(self, clicked_piece, sCoords, dCoords):
        sCol, sRow = sCoords
        dCol, dRow = dCoords

        self.pos[sRow][sCol] = 'e'
        self.pos[dRow][dCol] = clicked_piece

    def FEN_to_board(FEN):
        temp_board = [[' '] * 8 for up_iterator in range(8)]
        col = 0
        row = 0
        up_iterator = 0
        final_rank = False
        finished_iterating = False

        while not finished_iterating:
            if ord(FEN[up_iterator]) - 48 > 0 and ord(FEN[up_iterator]) - 48 <= 8:  # if is a number between 0 and 8
                for j in range(0, ord(FEN[up_iterator]) - 48):  # 0->7 maximum
                    temp_board[row][col + j] = 'e'
                col += ord(FEN[up_iterator]) - 49
            elif not FEN[up_iterator] == '/':
                temp_board[row][col] = FEN[up_iterator]

            if col == 8:  # if at the end of the rank
                row += 1  # go to next one
                col = 0
            else:
                col += 1

            if final_rank == True and col == 8:  # has finished the entire board
                finished_iterating = True

            if row == 7:
                final_rank = True

            up_iterator += 1
        return temp_board

class legal_moves():
    _piece_to_move = ''

    def __init__(self, piece_to_move) -> None:
        self._piece_to_move = piece_to_move

    # start_coords is tuple (x,y) from pygame event so flip sRow/sCol, same with dest_coords
    def is_legal(self, start_coords, dest_coords):
        sCol, sRow = start_coords
        dCol, dRow = dest_coords

        if start_coords == dest_coords:
            return False

        if self._piece_to_move.lower() == 'r':  # rook
            if (sCol == dCol or sRow == dRow):
                return True
        elif self._piece_to_move.lower() == 'b':  # bishop
            if abs(dCol-sCol) == abs(dRow-sRow):
                return True
        elif self._piece_to_move.lower() == 'n':  # knight
            if abs(dCol - sCol) == 2 and abs(dRow-sRow) == 1:
                return True
            elif abs(dRow - sRow) == 2 and abs(dCol-sCol) == 1:
                return True
        elif self._piece_to_move.lower() == 'q':  # queen
            if abs(dCol-sCol) == abs(dRow-sRow) or (sCol == dCol or sRow == dRow):
                return True
        elif self._piece_to_move.lower() == 'k':  # king
            if not abs(dRow - sRow) > 1 and not abs(dCol - sCol) > 1:
                return True

        # /////
        # Still needs diagonal case for pawn captures
        # /////
        if self._piece_to_move == 'P':  # both pawns move differently as black pawns move 'down the board'
            if sCol == dCol:
                if sRow == 6:  # if white pawn on starting square
                    if (sRow-dRow == 2 or sRow-dRow == 1):
                        return True
                else:
                    if sRow-dRow == 1:
                        return True
        elif self._piece_to_move == 'p':
            if sCol == dCol:
                if sRow == 1:  # if black pawn on starting square
                    if dRow-sRow == 2 or dRow-sRow == 1:
                        return True
                    else:
                        if dRow-sRow == 1:
                            return True

        return False

    def legal_squares(self,start_coords,position):
        Col,Row = start_coords
        forwards_iterator = 0 #will go up or right
        #this is the column so checks for example A1 -> A8
        legal_file_coords = [] 
        

        #2,3,4,5,6
        #2,1,0

        #redo this
        #have 2 booleans which check if its finished its iteration or not 
        

        if self._piece_to_move.lower() == 'r':
            down_finished = False
            up_finished = False
            up_iterator = Row
            down_iterator = Row


            # check the file
            while down_finished == False or up_finished == False:
                #down is essentially adding one to the row -> [0,1] [1,1] [2,1] etc.
                #up is essentially subtracting one from the row [7,1] [6,1] [5,1] etc.
                up_iterator -= 1
                down_iterator += 1
            
                if down_iterator == 8:
                    down_finished = True
                elif up_iterator == -1:
                    up_finished = True

                if up_finished == False:
                    if position[up_iterator][Col] == 'e' and up_finished == False: #if an empty square
                        legal_file_coords.append(up_iterator)
                    elif position[up_iterator][Col] != 'e' and up_finished == False: #if a piece is on the square
                        if (position[Row][Col].isupper() and position[up_iterator][Col].islower()) or (position[Row][Col].islower() and position[up_iterator][Col].isupper()): #if they're opposite colours
                            legal_file_coords.append(up_iterator)
                        up_finished = True

                if down_finished == False:
                    if position[min(down_iterator,7)][Col] == 'e':
                        legal_file_coords.append(min(down_iterator,7))
                    elif position[min(down_iterator,7)][Col] != 'e':
                        if (position[Row][Col].isupper() and position[min(down_iterator,7)][Col].islower()) or (position[Row][Col].islower() and position[down_iterator][Col].isupper()): #if they're opposite colours
                            legal_file_coords.append(min(down_iterator,7))
                        down_finished = True

            #check the rank
            left_finished = False
            right_finished = False
            while left_finished == False or right_finished == False:
                pass


        legal_file_coords.sort()
        return legal_file_coords

