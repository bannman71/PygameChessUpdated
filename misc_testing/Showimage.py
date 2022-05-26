import pygame
from os import walk


pygame.init()

white = (255, 255, 255)
X = 1000
Y = 1000


image = pygame.image.load(
    r'/Users/maxscullion/Projects/PygameChess/classic_hq/b_bishop.png')
display_surface = pygame.display.set_mode((X, Y))

k = pygame.Surface.get_at(image, (620, 636))
print(k)


# while True:

#     # completely fill the surface object
#     # with white colour
#     display_surface.fill(white)

#     # copying the image surface object
#     # to the display surface object at
#     # (0, 0) coordinate.
#     display_surface.blit(image, (0, 0))


#     # iterate over the list of Event objects
#     # that was returned by pygame.event.get() method.
#     for event in pygame.event.get():

#         # if event object type is QUIT
#         # then quitting the pygame
#         # and program both.
#         if event.type == pygame.QUIT:

#             # deactivates the pygame library
#             pygame.quit()

#             # quit the program.
#             quit()

#         # Draws the surface object to the screen.
#         pygame.display.update()
