import pygame as pg


def get_piece_at_clicked_location(clicked_coords, position):
    Col, Row = clicked_coords

    return position[Col][Row]
