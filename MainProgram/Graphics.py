import pygame as pg
import numpy as np

IMAGES = {}

BLACK = (118, 150, 86)
WHITE = (238, 238, 210)
BOARD_SIZE = 8
# makes window size a mulitple of board size (8)
WINDOW_SIZE = (600 // BOARD_SIZE) * BOARD_SIZE
BLOCK_SIZE = WINDOW_SIZE / BOARD_SIZE

PIECES =  {
    'b': 'b_bishop', 'k': 'b_king', 'n': 'b_knight', 'p': 'b_pawn', 'q': 'b_queen', 'r': 'b_rook',
    'B': 'w_bishop', 'K': 'w_king', 'N': 'w_knight', 'P': 'w_pawn', 'Q': 'w_queen', 'R': 'w_rook'}


def load_images():
    for im in PIECES:
        IMAGES[im] = (pg.transform.smoothscale(
            pg.image.load("/Users/maxscullion/Projects/PygameChess/classic_hq/" + PIECES[im] + ".png"), (BLOCK_SIZE * 0.75, BLOCK_SIZE * 0.75)))


def draw_piece(surface, piece_symbol, Coordinates):
    x, y = Coordinates

    if float.is_integer((x+66) / 75) == False or float.is_integer((y + 65) / 75) == False:
        raise Exception('Must be a valid coordinate')

    surface.blit(IMAGES[piece_symbol], (x, y))


def draw_grid(surface):
    for y in range(0, BOARD_SIZE):
        for x in range(0, BOARD_SIZE//2):
            rect = pg.Rect(
                (x*2 + ((y + 1) % 2)) * BLOCK_SIZE, y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            pg.draw.rect(surface, WHITE, rect)


def draw_piece_at_mousepos(surface, piece_symbol, coords):
    x, y = coords

    x -= (BLOCK_SIZE) * 0.375
    y -= (BLOCK_SIZE) * 0.375

    # # Draw rectangle around the image
    # rect = img.get_rect()
    # rect.center = 50, 50
    surface.blit(IMAGES[piece_symbol], (x, y))


