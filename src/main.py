from enum import Enum
from tkinter import *
import pygame
import time
import random

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

G_LENGTH = 600

COLUMNS, ROWS = 10, 10

BOMB_COUNT = 5

class TileType(Enum):
    BOMB = "x"
    EMPTY = "0"
    ONE = "1"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"

class Tile:
    def __init__(self):
        self.tile_type = TileType.EMPTY
        self.is_hidden = True

class Grid():
    def __init__(self, columns, rows) -> None:
        self.columns = columns
        self.rows = rows
        self.grid = []

    def create_grid(self, mines):
        self.grid = [[Tile() for i in range(self.columns)] for i in range(self.rows)]

        mine_pos = []
        while len(mine_pos) < mines:
            rand_row = random.randrange(0, self.rows)
            rand_column = random.randrange(0, self.columns)
            rand_pos = rand_row, rand_column

            if rand_pos in mines:
                continue
            else:
                mine_pos.append(rand_pos)
                self.grid[rand_row][rand_column] = TileType.BOMB

    def get_neighbor_tiles(self, row, column):
        neighbors = []
        
        if row > 0:                                                     # UP
            neighbors.append(self.grid[row-1][column])
        if row < self.rows-1:                                           # DOWN
            neighbors.append(self.grid[row+1][column])
        if column > 0:                                                  # LEFT
            neighbors.append(self.grid[row][column-1])
        if column < self.columns-1:                                     # RIGHT
            neighbors.append(self.grid[row][column+1])
        if row > 0 and column > 0:                                      # TOP LEFT
            neighbors.append(self.grid[row-1][column-1])
        if row < self.rows-1 and column < self.columns-1:               # TOP RIGHT
            neighbors.append(self.grid[row+1][column+1])
        if row < self.rows-1 and column > 0:                            # BOTTOM LEFT
            neighbors.append(self.grid[row+1][column-1])
        if row > 0 and column < self.columns-1:                         # BOTTOM RIGHT
            neighbors.append(self.grid[row-1][column+1])

if __name__ == "__main__":

    pygame.init()

    root_window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
    
    pygame.quit()