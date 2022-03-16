import pygame as pg

WHITE = (200, 200, 200)
BLACK = (0, 0, 0)
BOARD_SIZE = 8
# must be muklitple of boardisez
WINDOW_SIZE = (1000 // BOARD_SIZE) * BOARD_SIZE


def fill(surface, colour):
    w, h = pg.Surface.get_size(surface)

    r, g, b = colour
    for x in range(w):
        for y in range(h):
            if pg.Surface.get_at(surface, (x, y)) == (0, 0, 0):
                pg.Surface.set_at(surface, (x, y), pg.Color(r, g, b))
            elif pg.Surface.get_at(surface, (x, y)) == (255, 255, 255):
                pg.Surface.set_at(surface, (x, y), pg.Color(0, 0, 0))


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Board():

    def __init__(self):
        pass

    def create_grid(self):
        pass

    def draw_grid(self):
        blocksize = WINDOW_SIZE / BOARD_SIZE
        for y in range(0, BOARD_SIZE):
            for x in range(0, BOARD_SIZE//2):
                rect = pg.Rect(
                    (x*2 + ((y + 1) % 2)) * blocksize, y*blocksize, blocksize, blocksize)
                pg.draw.rect(SCREEN, WHITE, rect, 100)

    def draw_bishop(self, x, y):
        bishopImage = pg.image.load(
            r'/Users/maxscullion/Projects/pgChess/bishop.png')
        fill(bishopImage, (255, 255, 255))
        bishopImage = pg.transform.scale(bishopImage, (94, 94))
        SCREEN.blit(bishopImage, (x, y))

#blocksize = 20


if __name__ == "__main__":
    global SCREEN
    pg.init()
    SCREEN = pg.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    SCREEN.fill(BLACK)
    test = Board()

    run = True
    while run:
        test.draw_grid()
        test.draw_bishop(1, 1)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        pg.display.update()
