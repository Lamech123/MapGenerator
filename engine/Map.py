import pygame
import random
from Grid import Grid
from Data import Data
from MapTile import MapTile
from Constants import *

class Map:
    def __init__(self, resolution):
        self.tiles = []
        self.grid = []
        self.camera = pygame.Rect((0, 0), resolution)
        self.map_width, self.map_height = 0, 0
        self.block_width, self.block_height = 64, 64

    def keyboard_scrolling(self):
        scroll_speed = 1
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_a]:
            self.camera.x -= scroll_speed
        elif key_pressed[pygame.K_d]:
            self.camera.x += scroll_speed
        elif key_pressed[pygame.K_w]:
            self.camera.y -= scroll_speed
        elif key_pressed[pygame.K_s]:
            self.camera.y += scroll_speed

        if self.camera.x <= 0:
            self.camera.x = 0
        if self.camera.x + self.camera.w >= self.map_width*self.block_width:
            self.camera.x = (self.map_width*self.block_width) - self.camera.w
        if self.camera.y <= 0:
            self.camera.y = 0
        if self.camera.y + self.camera.h >= self.map_height*self.block_height:
            self.camera.y = (self.map_height*self.block_height) - self.camera.h
                
    def generate_field(self):
        self.gridmatch = {}
        self.datum = []
        self.tiles = []
        self.map_width = 20
        self.map_height = 21

        # Create a 2 dimensional list that will act as a data grid for the Map
        grid = Grid(self.map_height, self.map_width, 0)
        grid.generate_grid()

        grid.grid[0][19] = "a1"
        grid.grid[0][18] = "a2"
        grid.grid[0][17] = "a3"
        grid.grid[0][16] = "a4"
        grid.grid[0][15] = "a5"
        grid.grid[0][14] = "a6"
        grid.grid[0][13] = "a7"
        grid.grid[0][12] = "a8"
        grid.grid[0][11] = "a9"
        grid.grid[0][10] = "a10"
        grid.grid[0][9] = "a11"
        grid.grid[0][8] = "a12"
        grid.grid[0][7] = "a13"
        grid.grid[0][6] = "a14"
        grid.grid[0][5] = "a15"
        grid.grid[0][4] = "a16"
        grid.grid[0][3] = "a17"
        grid.grid[0][2] = "a18"
        grid.grid[0][1] = "a19"


        self.gridmatch = { "a1":"1977", "a2": "1978", "a3": "1979","a4":"1980", "a5": "1981", "a6": "1982","a7":"1983", "a8": "1984", "a9": "1985","a10":"1986", "a11": "1987", "a12": "1988","a10":"1989", "a11": "1990", "a12": "1991","a13":"1992", "a14": "1993", "a15": "1994","a16":"1995", "a17": "1996", "a18": "1997", "a19":"1998"}

        for y in range(0, self.map_height):
            for x in range(0, self.map_width):
                tile_image = pygame.surface.Surface((self.block_width, self.block_height))
                if grid.grid[x][y] == 0:
                    maptile=MapTile(BLACK, x*self.block_width, y*self.block_height, self.block_width, self.block_height, 0)
                elif self.gridmatch.has_key(grid.grid[x][y]):
                    maptile=MapTile(WHITE, x* self.block_width, y* self.block_height, self.block_width, self.block_height, self.gridmatch.get(grid.grid[x][y]))
                self.tiles.append(maptile)

    def draw(self, surface):
        #self.keyboard_scrolling()
        for tile in self.tiles:
            if self.camera.colliderect(tile):
                surface.blit(tile.image, (tile.rect.x - self.camera.x, tile.rect.y - self.camera.y), (0, 0, self.block_width, self.block_height))
