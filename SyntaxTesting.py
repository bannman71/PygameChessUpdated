import string
_board = [[0]*8]*8
print(_board)


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
            'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR/')

    def FEN_to_board(FEN: string):
        temp_board = [[0] * 9] * 9
        Xcount = 1
        Ycount = 1
        i = 0

        while Ycount != 9:
            if not FEN[i] == '/':
                temp_board[Ycount][Xcount] = FEN[i]

            if ord(FEN[i]) - 48 > 0 and ord(FEN[i]) - 48 <= 8:
                for j in range(0, ord(FEN[i]) - 48):
                    temp_board[Ycount][Xcount+j] = 'e'
                Xcount += ord(FEN[i]) - 48

            if FEN[i] == '/':
                Ycount += 1
                Xcount = 1
            else:
                Xcount += 1
            i += 1
        return temp_board


position = Position()._returned_position


for x in range(1, 9):
    for y in range(1, 9):
        print(Position()._returned_position[x][y], end=' ')
    print()
