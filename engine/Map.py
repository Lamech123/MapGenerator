#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pygame
import random
from Grid import Grid
from Data import Data
from MapTile import MapTile
from Constants import *

class Map:
    def __init__(self, resolution):
        self.tiles = []
        self.block_list = pygame.sprite.RenderPlain()
        self.camera = pygame.Rect((0, 0), resolution)
        self.map_width, self.map_height = 0, 0
        self.block_width, self.block_height = 140, 140

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
                
    def generate_field(self, width, height):
        self.gridmatch = {}
        self.map_width = width
        self.map_height = height

        # Create a 2 dimensional list that will act as a data grid for the Map
        grid = Grid(self.map_height, self.map_width, 0)
        grid.load_grid()

        self.gridmatch = {
        "a1" :"Jane is living with her Aunt Reed and cousins at Gateshead, being bullied and tormented by John Reed in particular.",
        "a2" :"Jane finally can't take it anymore and fights back against John.",
        "a3" :"Jane is locked in the 'red-room,' the bedchamber in which her uncle died, as a punishment, and has a traumatic, eerie experience.",
        "a4" :"Jane is sent to Lowood Institute, a religious school for orphan girls.",
        "a5" :"Jane studies hard and eventually becomes a teacher at Lowood.",
        "a6" :"Jane gets a spot of wanderlust and applies to be a governess.",
        "a7" :"Jane gets a job at Thornfield as the governess to a little French girl named Adèle Varens.",
        "a8" :"Jane meets the master of Thornfield, Mr. Rochester, and quickly falls in love with him.",
        "a9" :"Jane has a series of eerie experiences related to a mysterious locked room on the third floor of Thornfield and a creepy woman’s laugh that she hears coming from behind the door.",
        "a10" :"Mr. Rochester teases Jane by pretending to be interested in a local debutante, Blanche Ingram.",
        "a11" :"Jane goes back to Gateshead to tend Mrs. Reed on her deathbed.",
        "a12" :"Jane returns to Thornfield and eventually becomes engaged to Mr. Rochester.",
        "a13" :"Jane and Rochester’s wedding is interrupted by two men who reveal that Rochester is already married.",
        "a14" :"Jane leaves Thornfield and wanders alone on the moors, friendless and starving.",
        "a15" :"Arriving at Moor House, Jane is taken in by Diana, Mary, and St. John Rivers.",
        "a16" :"After regaining her strength, with St. John’s help, Jane gets a job as a teacher in a village school in Morton and moves to her own cottage.",
        "a17" :"Jane discovers that she and the Rivers siblings are cousins and that she has inherited £20,000.",
        "a18" :"St. John Rivers asks Jane to marry him and go with him to India on a missionary trip.",
        "a19" :"Jane mysteriously hears Rochester calling her from a great distance.",
        "a20" :"Jane returns to Thornfield and marries Mr. Rochester.",
        "a21" :"Jane and Rochester have a son.",
        "b1" : "Rochester",
        "c1" :"Bertha Mason"}

        for y in range(0, self.map_height):
            for x in range(0, self.map_width):
                tile_image = pygame.surface.Surface((self.block_width, self.block_height))
                if grid.grid[x][y] == 0:
                    maptile=MapTile(BLACK, x*self.block_width, y*self.block_height, self.block_width, self.block_height, 0)
                #elif self.gridmatch.has_key(grid.grid[x][y]):
                elif grid.grid[x]
                    maptile=MapTile(WHITE, x* self.block_width, y* self.block_height, self.block_width, self.block_height, self.gridmatch.get(grid.grid[x][y]))
                #self.tiles.append(maptile)
                self.block_list.add(maptile)

    def draw(self, surface):
        #self.keyboard_scrolling()
        for tile in self.block_list:
            if self.camera.colliderect(tile):
                surface.blit(tile.image, (tile.rect.x - self.camera.x, tile.rect.y - self.camera.y), (0, 0, self.block_width, self.block_height))
