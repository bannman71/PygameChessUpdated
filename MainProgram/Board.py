import pygame as pg
from sqlalchemy import true


def get_piece_at_clicked_location(position, clicked_coords):
    Col, Row = clicked_coords

    return position[Row // 75][Col // 75]


def get_coord_at_click_location(clicked_coords):
    Col, Row = clicked_coords

    return Col//75, Row//75

#legal_moves('r').is_legal(start_coords, dest_coords)


# rook can only move along same file or rank so:
# dest coords must have same x OR y as start coords

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

# for pawns:
# if its on startin square (white row = 1)(black row = 2) and its destination square is 2 forward then
# elif its not on starting square and it moves on forward then yup

# 0,0
#1,1 | 2,2


#8,8 | 7,7 | 6,6
