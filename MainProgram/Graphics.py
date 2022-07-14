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

# PIECES = {
#    'b': 'b_bishop', 'k': 'b_king', 'n': 'b_knight', 'p': 'b_pawn', 'q': 'b_queen', 'r': 'b_rook',
#     'B': 'w_bishop', 'K': 'w_king', 'N': 'w_knight', 'P': 'w_pawn', 'Q': 'w_queen', 'R': 'w_rook'}

BIN_PIECES =  {
    20: 'b_bishop', 17: 'b_king', 19: 'b_knight', 18: 'b_pawn', 22: 'b_queen', 21: 'b_rook',
    12: 'w_bishop', 9: 'w_king', 11: 'w_knight', 10: 'w_pawn', 14: 'w_queen', 13: 'w_rook'}

# BIN_PIECES =  {
#     20: 'b', 17: 'k', 19: 'n', 18: 'p', 22: 'q', 21: 'r',
#     12: 'B', 9: 'K', 11: 'N', 10: 'P', 14: 'Q', 13: 'R'}


def load_images():
    for im in BIN_PIECES:
        IMAGES[im] = (pg.transform.smoothscale(
            pg.image.load("./classic_hq/" + BIN_PIECES[im] + ".png").convert_alpha(), (BLOCK_SIZE * PIECE_SCALE, BLOCK_SIZE * PIECE_SCALE)))


def draw_piece(surface, piece_number, Coordinates):
    x, y = Coordinates

    x = SPACING + x * BLOCK_SIZE
    y = SPACING + y * BLOCK_SIZE

    surface.blit(IMAGES[piece_number], (x, y))


def draw_grid(surface):
    for y in range(0, BOARD_SIZE):
        for x in range(0, BOARD_SIZE//2):
            pg.draw.rect(surface, WHITE, pg.Rect(
                (x*2 + ((y + 1) % 2)) * BLOCK_SIZE, y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))


def draw_piece_at_mousepos(surface, piece_number, coords):
    x, y = coords
    x -= BLOCK_SIZE * PIECE_SCALE / 2  # centers piece
    y -= BLOCK_SIZE * PIECE_SCALE / 2
    surface.blit(IMAGES[piece_number], 
        (min(WINDOW_SIZE - BLOCK_SIZE +SPACING, max(SPACING, x)), min(WINDOW_SIZE - BLOCK_SIZE + SPACING, max(SPACING, y))))
