import pygame as pg
import numpy as np

IMAGES = {}
BLACK = (140, 162, 173)
WHITE = (222, 227, 230)
BOARD_SIZE = 8
# makes window size a mulitple of board size (8)
WINDOW_SIZE = (600 // BOARD_SIZE) * BOARD_SIZE
BLOCK_SIZE = WINDOW_SIZE / BOARD_SIZE
PIECE_SCALE = 0.75
SPACING = (BLOCK_SIZE * (1 - PIECE_SCALE)) // 2

PIECES = {
    'b': 'b_bishop', 'k': 'b_king', 'n': 'b_knight', 'p': 'b_pawn', 'q': 'b_queen', 'r': 'b_rook',
    'B': 'w_bishop', 'K': 'w_king', 'N': 'w_knight', 'P': 'w_pawn', 'Q': 'w_queen', 'R': 'w_rook'}


def load_images():
    for im in PIECES:
        IMAGES[im] = (pg.transform.smoothscale(
            pg.image.load("../classic_hq/" + PIECES[im] + ".png").convert_alpha(), (BLOCK_SIZE * PIECE_SCALE, BLOCK_SIZE * PIECE_SCALE)))

def draw_piece(surface, piece_symbol, Coordinates):
    x, y = Coordinates

    x = SPACING + x * BLOCK_SIZE
    y = SPACING + y * BLOCK_SIZE

    surface.blit(IMAGES[piece_symbol], (x, y))


def draw_grid(surface):
    for y in range(0, BOARD_SIZE):
        for x in range(0, BOARD_SIZE//2):
            pg.draw.rect(surface, WHITE, pg.Rect(
                (x*2 + ((y + 1) % 2)) * BLOCK_SIZE, y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))


def draw_piece_at_mousepos(surface, piece_symbol, coords):
    x, y = coords
    x -= BLOCK_SIZE * PIECE_SCALE / 2  # centers piece
    y -= BLOCK_SIZE * PIECE_SCALE / 2
    surface.blit(IMAGES[piece_symbol], (min(WINDOW_SIZE - BLOCK_SIZE +
                 SPACING, max(SPACING, x)), min(WINDOW_SIZE - BLOCK_SIZE + SPACING, max(SPACING, y))))
