import pygame
from engine.Map import Map
from engine.Constants import *
from engine.button import Button
WINDOWWIDTH = 640 
WINDOWHEIGHT = 640
EXTRAW = 200

def main():

    pygame.init()
    resolution = (640, 640)
    screen = pygame.display.set_mode((WINDOWWIDTH + EXTRAW, WINDOWHEIGHT))
    #screen.set_clip(0,0, resolution)
    running = True

    map1 = Map(resolution)
    map1.generate_field()

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_r:
                    map1.block_height += 4
                    map1.block_width += 4
                elif event.key == pygame.K_f:
                    map1.block_height -= 4
                    map1.block_width -= 4
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()

                #Change the x/y screen coordinates to grid coordinates
                column=pos[0] // (map1.map_width)
                row=pos[1] // (map1.map_height)
                print("Click ",pos,"Grid coordinates: ",column, row)

        map1.keyboard_scrolling()
        map1.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()
    pygame.quit()
