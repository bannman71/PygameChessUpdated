import pygame as pg


def get_piece_at_clicked_location(position, clicked_coords):
    Col, Row = clicked_coords

    Col = Col // 75
    Row = Row // 75

    return position[Row][Col]
