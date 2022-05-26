import chess
import chess.svg

# makes a board using FEN String as input

board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")

# calls the SVG render fuction, passes the above board and specifies the size in pixels.

boardsvg = chess.svg.board(board, size=350)


# creates a file with proper permissions

outputfile = open('board.svg', "w")
outputfile.write(boardsvg)
outputfile.close()

# prints the board in ASCII to the terminal just for fun.


print(board)
