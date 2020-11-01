import pygame


def draw_grid(cols, rows, surface):
    pass


def redraw_window(surface):
    # win.fill((0,0,0))
    # draw_grid(surface)
    # pygame.display.update()
    pass


pygame.init()
win = pygame.display
win = win.set_mode((600, 600))

# speed management piece 1
# clock = pygame.time.Clock()

while True:
    # speed management piece 2
    # pygame.time.delay(50)
    # clock.tick(10)

    win.fill((0,0,0))
    sizeBtwn = 1
    x = 0
    y = 0
    for line in range(600):
        x = x + sizeBtwn
        y = y +sizeBtwn
        pygame.draw.line(win, (255,255,255), (x,0), (x,600))
        pygame.draw.line(win, (255,255,255), (0,y), (600,y))

    pygame.display.update()
    pygame.event.get()
    # redrawWindow(win)

