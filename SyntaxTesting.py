import string
import numpy as np
# _board = [[0]*8]*8
# print(_board)


class Position:

    _returned_position = [[0]*8]*8

    # //////
    # if constructor is empty then the starting position is made
    # otherwise, the custom position that has been inputted will be returned
    # //////

    # def __init__(self, FEN_string: string):
    #     self._returned_position = FEN_STARTING_BOARD

    def __init__(self):  # if no constructor
        self._returned_position = Position.FEN_to_board(
            'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR')

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

# if 7 slashes have been counted then
# loop once more


position = Position()._returned_position


for x in range(1, 9):
    for y in range(1, 9):
        print(position[x][y], end=' ')
    print()
