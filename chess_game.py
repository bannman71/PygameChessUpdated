import cPlayer
import pygame as pg

BLACK = (118, 150, 86)
WHITE = (238, 238, 210)
BOARD_SIZE = 8
# must be muklitple of boardisez
WINDOW_SIZE = (800 // BOARD_SIZE) * BOARD_SIZE


class Player:
    _player1 = "white"
    _player2 = "black"
    empty = -1
    Pieces = ['b_bishop', 'b_king', 'b_knight', 'b_pawn', 'b_queen', 'b_rook',
              'w_bishop', 'w_king', 'w_knight', 'w_pawn', 'w_queen', 'w_rook']


class Graphics:

    def draw_grid():
        blocksize = WINDOW_SIZE / BOARD_SIZE
        for y in range(0, BOARD_SIZE):
            for x in range(0, BOARD_SIZE//2):
                rect = pg.Rect(
                    (x*2 + ((y + 1) % 2)) * blocksize, y*blocksize, blocksize, blocksize)
                pg.draw.rect(SCREEN, WHITE, rect, 64)


if __name__ == "__main__":
    global SCREEN
    pg.init()

    SCREEN = pg.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    SCREEN.fill(BLACK)

    run = True
    while run:
        Graphics.draw_grid()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        pg.display.update()
