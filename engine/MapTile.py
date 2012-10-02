import pygame
from Constants import WHITE, BLACK, BLUE, BRIGHTBLUE
from string import Template
from engine.Wrap import render_textrect

# This class represents each individual tile
# It derives from the "Sprite" class in Pygame
class MapTile(pygame.sprite.Sprite):
 
    # Constructor. Pass in the color of the block, it's x/y values, block dimensions, and text
    def __init__(self, color, x, y, block_width, block_height, text=0):

        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        BASICFONT = pygame.font.Font('freesansbold.ttf', 12)

        # Create the image of the block of appropriate size
        # The width and height are sent as a list for the first parameter.
        self.image = pygame.Surface([block_width, block_height])

        # self.image.fill(white)
        # Fill the image with the appropriate color
        #self.image.fill(WHITE)
        #self.image.set_colorkey(WHITE)
        
        pygame.draw.rect(self.image,color,[0,0,block_width,block_height])

        # Fetch the rectangle object that has the dimensions of the image

        self.rect = self.image.get_rect()
        self.txt_pos = self.rect.topleft
        if text == 0:
            self.msg_box = BASICFONT.render('%d, %d' %(x/block_width,y/block_height), True, BLACK)
        else:
            self.msg_box = render_textrect(text, BASICFONT, self.rect, BLACK, WHITE, 0)
            #self.msg_box = BASICFONT.render('%s' % text, True, BLACK)
        self.image.blit(self.msg_box, self.txt_pos)

        # Move the top left of the rectangle to x,y.
        # This is where our block will appear..

        self.rect.topleft = (x, y)

        #self.rect.x = x
        #self.rect.y = y

    def setCords(self,x,y):
        self.rect.topleft = x, y

    def pressed(self,mouse):
        if mouse[0] > self.rect.topleft[0]:
            if mouse[1] > self.rect.topleft[1]:
                if mouse[0] < self.rect.bottomright[0]:
                    if mouse[1] < self.rect.bottomright[1]:
                        return True
                    else: return False
                else: return False
            else: return False
        else: return False