import pygame as pg
import numpy as np

IMAGES = {}

BLACK = (140, 162, 173)
WHITE = (222, 227, 230)
BOARD_SIZE = 8
# makes window size a mulitple of board size (8)
WINDOW_SIZE = (600 // BOARD_SIZE) * BOARD_SIZE
BLOCK_SIZE = WINDOW_SIZE / BOARD_SIZE

PIECE_SYMBOL_TO_TYPE = {
    'b': 'b_bishop', 'k': 'b_king', 'n': 'b_knight', 'p': 'b_pawn', 'q': 'b_queen', 'r': 'b_rook',
    'B': 'w_bishop', 'K': 'w_king', 'N': 'w_knight', 'P': 'w_pawn', 'Q': 'w_queen', 'R': 'w_rook'}

PIECES = ['b_bishop', 'b_king', 'b_knight', 'b_pawn', 'b_queen', 'b_rook',
          'w_bishop', 'w_king', 'w_knight', 'w_pawn', 'w_queen', 'w_rook']


def load_images():
    for im in PIECES:
        IMAGES[im] = (pg.transform.smoothscale(
            pg.image.load("../classic_hq/" + im + ".png"), (BLOCK_SIZE * 0.75, BLOCK_SIZE * 0.75)))


def draw_piece(surface, piece_symbol, Coordinates):
    x, y = Coordinates

    if float.is_integer((x+66) / 75) == False or float.is_integer((y + 65) / 75) == False:
        raise Exception('Must be a valid coordinate')

    piece_details = PIECE_SYMBOL_TO_TYPE[piece_symbol]

    surface.blit(IMAGES[piece_details], (x, y))


def draw_grid(surface):
   for y in range(0, BOARD_SIZE):
       for x in range(0, BOARD_SIZE//2):
            pg.draw.rect(surface, WHITE, pg.Rect(
                (x*2 + ((y + 1) % 2)) * BLOCK_SIZE, y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))


def draw_piece_at_mousepos(surface, piece_symbol, coords):
    x, y = coords
    x -= BLOCK_SIZE * 0.375 # centers piece
    y -= BLOCK_SIZE * 0.375
    surface.blit(IMAGES['b_bishop'], (min(WINDOW_SIZE - BLOCK_SIZE + 10, max(9, x)), min(WINDOW_SIZE - BLOCK_SIZE + 10, max(9, y))))


