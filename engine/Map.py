import pygame
import random
from Grid import Grid
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
        self.tiles = []
        self.map_width = 20
        self.map_height = 20
        grid = Grid(self.map_width, self.map_height, 0)
        grid.generate_grid()
        grid.grid[1][5] = 1
        for y in range(0, self.map_height):
            for x in range(0, self.map_width):
                tile_image = pygame.surface.Surface((self.block_width, self.block_height))
                if grid.grid[x][y] == 0:
                    maptile=MapTile(BLACK, x*self.block_width, y*self.block_height, self.block_width, self.block_height, 0)
                elif grid.grid[x][y] == 1:
                    maptile=MapTile(RED, x* self.block_width, y* self.block_height, self.block_width, self.block_height, "Titanic")
                else:
                    maptile=MapTile(WHITE, x* self.block_width, y* self.block_height, self.block_width, self.block_height, 0)
                self.tiles.append(maptile)       

    def draw(self, surface):
        #self.keyboard_scrolling()
        for tile in self.tiles:
            if self.camera.colliderect(tile):
                surface.blit(tile.image, (tile.rect.x - self.camera.x, tile.rect.y - self.camera.y), (0, 0, self.block_width, self.block_height))
