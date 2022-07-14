import pygame as pg
from sqlalchemy import true
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
                if self.pos[row][col] != Piece.none:
                    # notice row column is flipped for the graphical position because x = col and y = row
                    Graphics.draw_piece(surface, self.pos[row][col], (col, row))

    def update(self, clicked_piece, sCoords, dCoords):
        sCol, sRow = sCoords
        dCol, dRow = dCoords

        self.pos[sRow][sCol] = Piece.none
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

        if uncoloured_piece == Piece.rook: 
            return (sCol == dCol or sRow == dRow) and (dRow in self.legal_file_squares(start_coords) or dCol in self.legal_rank_squares(start_coords))
        elif uncoloured_piece == Piece.bishop:  
            if abs(dCol-sCol) == abs(dRow-sRow):
                return True
        elif uncoloured_piece == Piece.knight:  
            if abs(dCol - sCol) == 2 and abs(dRow-sRow) == 1:
                return True
            elif abs(dRow - sRow) == 2 and abs(dCol-sCol) == 1:
                return True
        elif uncoloured_piece == Piece.queen:  # queen
            if abs(dCol-sCol) == abs(dRow-sRow) or (sCol == dCol or sRow == dRow):
                return True
        elif uncoloured_piece == Piece.king:  
            if not abs(dRow - sRow) > 1 and not abs(dCol - sCol) > 1:
                return True

        # /////
        # Still needs diagonal case for pawn captures
        # /////
        if self._piece_to_move == Piece.pawn ^ Piece.white:  # both pawns move differently as black pawns move 'down the board'
            if sCol == dCol:
                if sRow == 6:  # if white pawn on starting square
                    if (sRow-dRow == 2 or sRow-dRow == 1):
                        return True
                else:
                    if sRow-dRow == 1:
                        return True
        elif self._piece_to_move == Piece.pawn ^ Piece.black:
            if sCol == dCol:
                if sRow == 1:  # if black pawn on starting square
                    if dRow-sRow == 2 or dRow-sRow == 1:
                        return True
                    else:
                        if dRow-sRow == 1:
                            return True

        return False

    def is_on_board(self,Row,Col):
        if Row >= 0 and Row < 8 and Col >= 0 and Col < 8:
            return True
        return False

    def legal_diagonal_squares(self,start_coords):
        Col,Row = start_coords
        legal_diagonal_coords = []
        intervals = [(1,1),(-1,1),(1,-1),(-1,-1)]

        for row_int, col_int in intervals:
            row_temp,col_temp = row_int + Row, col_int + Col #makes sure it doesnt start on the piece

            while self.is_on_board(row_temp,col_temp): #while hasn't gone outside of the array
                if self._position[row_temp][col_temp] == Piece.none:
                    legal_diagonal_coords.append((row_temp,col_temp))
                else:
                    if (self._position[Row][Col] & 24) & (self._position[row_temp][col_temp] & 24) == 0: #if opposite colours
                        legal_diagonal_coords.append((row_temp,col_temp))
                    break
                row_temp,col_temp = row_temp + row_int, col_temp + col_int

        legal_diagonal_coords.sort()
        return legal_diagonal_coords
    
    def legal_file_squares(self,start_coords):
        
        Col, Row = start_coords
        legal_file_coords = []

        for i in range(Row - 1, -1, -1):
            if self._position[i][Col] == Piece.none: #if an empty square
                legal_file_coords.append(i)
            else: #if a piece is on the square
                if (self._position[Row][Col] & 24) & (self._position[i][Col] & 24) == 0: #if they're opposite colours
                    legal_file_coords.append(i)
                break
        
        for j in range(Row + 1,8):
            if self._position[j][Col] == Piece.none:
                legal_file_coords.append(j)
            elif self._position[j][Col] != 0:
                if (self._position[Row][Col] & 24) & (self._position[j][Col] & 24) == 0: #if they're opposite colours
                    legal_file_coords.append(j)
                break

        legal_file_coords.sort()
        return legal_file_coords
        
    def legal_rank_squares(self,start_coords):
        
        Col, Row = start_coords
        legal_rank_coords = []

        for i in range(Col - 1, -1, -1):
            if self._position[Row][i] == Piece.none: #if an empty square
                legal_rank_coords.append(i)
            else: #if a piece is on the square
                if (self._position[Row][Col] & 24) & (self._position[Row][i] & 24) == 0: #if they're opposite colours
                    legal_rank_coords.append(i)
                break
        
        for j in range(Col + 1,8):
            if self._position[Row][j] == Piece.none:
                legal_rank_coords.append(j)
            else:
                if (self._position[Row][Col] & 24) & (self._position[Row][j] & 24) == 0: #if they're opposite colours
                    legal_rank_coords.append(j)
                break

        legal_rank_coords.sort()
        return legal_rank_coords

        # 1,Col 2,Col etc
        # Row,1 Row,2 etc
