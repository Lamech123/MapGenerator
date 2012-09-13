FPS = 30 # frames per second to update the screen
WINDOWWIDTH = 480 # width of the program's window, in pixels
WINDOWHEIGHT = 480 # height in pixels
HALF_WINWIDTH = int(WINDOWWIDTH / 2)
HALF_WINHEIGHT = int(WINDOWHEIGHT / 2)
LEFT = 'left'
RIGHT = 'right'
left = 30
top = 40
RECT_WIDTH = 50
RECT_HEIGHT = 60
EXTRAW = 300
CELLSIZE = 20
assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)

# set up the colors

#                 R    G    B
BLACK =         (  0,   0,   0)
WHITE =         (255, 255, 255)
BRIGHTBLUE =    (  0,  50, 255)
DARKTURQUOISE = (  3,  54,  73)
GREEN =         (  0, 204,   0)
RED   =         (255,   0,   0)
GREEN =         (  0, 255,   0)
BLUE  =         (  0,   0, 255)
DARKGREEN =     (  0, 155,   0)
DARKGRAY  =     ( 40,  40,  40)



BGCOLOR = WHITE
TITLECOLOR = BLACK
TEXTCOLOR = WHITE
BASICFONTSIZE = 20

# This sets the width and height of each grid location
TILE_WIDTH=65
TILE_HEIGHT=65

XMARGIN = int((WINDOWWIDTH - (2 * TILE_WIDTH) - 1) / 2)
YMARGIN = int((WINDOWHEIGHT - (2 * TILE_WIDTH) - 1) / 2)

# This sets the margin between each cell
MARGIN=1

# Create a 2 dimensional array. A two dimesional
# array is simply a list of lists.
GRID = [    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] ]
