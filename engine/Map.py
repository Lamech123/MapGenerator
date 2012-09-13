import pygame
import random
from MapTile import MapTile
from Constants import *

class Map:
    def __init__(self, resolution):
        self.tiles = []
        self.grid = []
        self.camera = pygame.Rect((0, 0), resolution)
        self.map_width, self.map_height = 0, 0

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
        if self.camera.x + self.camera.w >= self.map_width*32:
            self.camera.x = (self.map_width*32) - self.camera.w
        if self.camera.y <= 0:
            self.camera.y = 0
        if self.camera.y + self.camera.h >= self.map_height*32:
            self.camera.y = (self.map_height*32) - self.camera.h
   
    def generate_grid(self):
        for row in range(50):
            self.grid.append([])
            for column in range(40):
                self.grid[row].append(2)
                
    def generate_field(self):
        self.tiles = []
        self.map_width = 50 
        self.map_height = 40 
        self.generate_grid()
        self.grid[1][5] = 1
        for y in range(0, self.map_height):
            for x in range(0, self.map_width):
                tile_image = pygame.surface.Surface((32, 32))
                if self.grid[x][y] == 0:
                    maptile=MapTile(BLUE, x*32, y*32, 32, 32, 0)
                elif self.grid[x][y] == 1:
                    maptile=MapTile(RED, x*32, y*32, 32, 32, "Titanic")
                else:
                    maptile=MapTile(WHITE, x*32, y*32, 32, 32, 0)
                self.tiles.append(maptile)       

    def draw(self, surface):
        #self.keyboard_scrolling()
        for tile in self.tiles:
            if self.camera.colliderect(tile):
                surface.blit(tile.image, (tile.rect.x - self.camera.x, tile.rect.y - self.camera.y), (0, 0, 32, 32))
