import pygame as pg
import Graphics

FEN_STARTING_BOARD = str("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")


def get_piece_at_clicked_location(position, clicked_coords):
    Col, Row = clicked_coords

    return position[Row // 75][Col // 75]


def get_coord_at_click_location(clicked_coords):
    Col, Row = clicked_coords

    return Col//75, Row//75

class Piece:
    pieces = {
            'k': 1, 'p' : 2, 'n' : 3, 'b': 4, 'r': 5, 'q': 6,
            'K': 1, 'P' : 2, 'N' : 3, 'B': 4, 'R': 5, 'Q': 6 }

    none = 0
    king = 1
    pawn = 2
    knight = 3
    bishop = 4
    rook = 5
    queen = 6
    
    white = 8
    black = 16



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
                if self.pos[row][col] != 0:
                    # notice row column is flipped for the graphical position because x = col and y = row
                    Graphics.draw_piece(surface, self.pos[row][col], (col, row))

    def update(self, clicked_piece, sCoords, dCoords):
        sCol, sRow = sCoords
        dCol, dRow = dCoords

        self.pos[sRow][sCol] = 0
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
                    temp_board[row][col + j] = 0
                col += ord(FEN[up_iterator]) - 49
            elif not FEN[up_iterator] == '/':
                if FEN[up_iterator].islower():
                    temp_board[row][col] = 16 #if black
                else: temp_board[row][col] = 8
                temp_board[row][col] = temp_board[row][col] ^ Piece.pieces[FEN[up_iterator]] 

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
    _piece_to_move = 0

    def __init__(self, piece_to_move,position) -> None:
        self._piece_to_move = piece_to_move
        self._position = position

    # start_coords is tuple (x,y) from pygame event so flip sRow/sCol, same with dest_coords
    def is_legal(self, start_coords, dest_coords):
        sCol, sRow = start_coords
        dCol, dRow = dest_coords
        uncoloured_piece = self._piece_to_move & 7

        if start_coords == dest_coords:
            return False

        if uncoloured_piece == 5:  # rook
            if (sCol == dCol or sRow == dRow) and dRow in self.legal_file_squares(start_coords,self._position):
                return True
        elif uncoloured_piece == 4:  # bishop
            if abs(dCol-sCol) == abs(dRow-sRow):
                return True
        elif uncoloured_piece == 3:  # knight
            if abs(dCol - sCol) == 2 and abs(dRow-sRow) == 1:
                return True
            elif abs(dRow - sRow) == 2 and abs(dCol-sCol) == 1:
                return True
        elif uncoloured_piece == 6:  # queen
            if abs(dCol-sCol) == abs(dRow-sRow) or (sCol == dCol or sRow == dRow):
                return True
        elif uncoloured_piece == 1:  # king
            if not abs(dRow - sRow) > 1 and not abs(dCol - sCol) > 1:
                return True

        # /////
        # Still needs diagonal case for pawn captures
        # /////
        if self._piece_to_move == 10:  # both pawns move differently as black pawns move 'down the board'
            if sCol == dCol:
                if sRow == 6:  # if white pawn on starting square
                    if (sRow-dRow == 2 or sRow-dRow == 1):
                        return True
                else:
                    if sRow-dRow == 1:
                        return True
        elif self._piece_to_move == 18:
            if sCol == dCol:
                if sRow == 1:  # if black pawn on starting square
                    if dRow-sRow == 2 or dRow-sRow == 1:
                        return True
                    else:
                        if dRow-sRow == 1:
                            return True

        return False

    def check_rank(start_coords, position):
        left_finished = False
        right_finished = False
        while left_finished == False or right_finished == False:
            pass

    def check_diagonal(start_coords, position):
        pass

    def legal_file_squares(self,start_coords,position):
        
        Col, Row = start_coords
        legal_file_coords = []

        for i in range(Row - 1, -1, -1):
            if position[i][Col] == 0: #if an empty square
                legal_file_coords.append(i)
            else: #if a piece is on the square
                if (position[Row][Col] & 24) & (position[i][Col] & 24) == 0: #if they're opposite colours
                    legal_file_coords.append(i)
                break
        
        for j in range(Row + 1,8):
            if position[j][Col] == 0:
                legal_file_coords.append(j)
            elif position[j][Col] != 0:
                if (position[Row][Col] & 24) & (position[j][Col] & 24) == 0: #if they're opposite colours
                    legal_file_coords.append(j)
                break

        legal_file_coords.sort()
        return legal_file_coords
        
    def legal_rank_squares():
        pass

