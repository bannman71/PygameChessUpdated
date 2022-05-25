from turtle import screensize
import pygame as pg
import chess

BLACK = (118, 150, 86)
WHITE = (238, 238, 210)
BOARD_SIZE = 8
# must be muklitple of boardisez
WINDOW_SIZE = (800 // BOARD_SIZE) * BOARD_SIZE
IMAGES = [0]*11


class Player:
    _player1 = "white"
    _player2 = "black"
    empty = -1
    Pieces = ['b_bishop', 'b_king', 'b_knight', 'b_pawn', 'b_queen', 'b_rook',
              'w_bishop', 'w_king', 'w_knight', 'w_pawn', 'w_queen', 'w_rook']


class Graphics:

    def __init__(self):
        pass

    def load_images():
        index = 0
        for im in Player.Pieces:
            IMAGES[index] = pg.transform.smoothscale(
                pg.image.load("/Users/maxscullion/Projects/PygameChess/classic_hq/" + im + ".png"), (50, 50))
            index += 1

    def test():
        IMAGES[0] = pg.transform.smoothscale(pg.image.load(
            r'/Users/maxscullion/Projects/PygameChess/classic_hq/b_bishop.png'), (100, 100))

    def draw_grid():
        blocksize = WINDOW_SIZE / BOARD_SIZE
        for y in range(0, BOARD_SIZE):
            for x in range(0, BOARD_SIZE//2):
                rect = pg.Rect(
                    (x*2 + ((y + 1) % 2)) * blocksize, y*blocksize, blocksize, blocksize)
                pg.draw.rect(SCREEN, WHITE, rect, 64)

    def draw_piece(self, x, y):
        pass


if __name__ == "__main__":
    global SCREEN
    pg.init()

    SCREEN = pg.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    SCREEN.fill(BLACK)

    run = True
    while run:
        Graphics.draw_grid()
        Graphics.load_images()
        #help = Graphics.test()

        SCREEN.blit(IMAGES[2], (25, 25))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        pg.display.update()
