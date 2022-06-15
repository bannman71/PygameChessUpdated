import pygame as pg
import Graphics
import Board


if __name__ == "__main__":
    global SCREEN
    pg.init()
    mouse_down = False
    start_clicked_square = 0
    destination_clicked_square = 0

    SCREEN = pg.display.set_mode((Graphics.WINDOW_SIZE, Graphics.WINDOW_SIZE))
    SCREEN.fill(Graphics.BLACK)
    Graphics.load_images()


    Graphics.draw_grid(SCREEN)
    empty_board = SCREEN.copy()

    position = Board.Position()

    position.draw(SCREEN)
    current_pos = SCREEN.copy()

    
    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_down = True

                clicked_piece = Board.get_piece_at_clicked_location(position.pos, pg.mouse.get_pos())

                start_clicked_square = Board.get_coord_at_click_location(pg.mouse.get_pos())

                print(Board.legal_moves(clicked_piece).legal_squares(start_clicked_square,position.pos))

            elif event.type == pg.MOUSEBUTTONUP:
                mouse_down = False
                destination_clicked_square = Board.get_coord_at_click_location(pg.mouse.get_pos())

                if Board.legal_moves(clicked_piece).is_legal(start_clicked_square, destination_clicked_square) == True:
                    position.update(clicked_piece, start_clicked_square, destination_clicked_square)


                SCREEN.blit(empty_board, (0, 0))
                position.draw(SCREEN)
                current_pos = SCREEN.copy()

        if mouse_down and clicked_piece != 'e':
            SCREEN.blit(current_pos, (0, 0))
            Graphics.draw_piece_at_mousepos(SCREEN, clicked_piece, pg.mouse.get_pos())

        pg.display.update()
    pg.quit()
