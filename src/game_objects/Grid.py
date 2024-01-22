from TileType import TileType
from game_objects.Tile import Tile
import random

class Grid():
    def __init__(self, surface, rows, columns, width, height, global_x, global_y, sprite_size, sprites) -> None:
        self.surface = surface
        self.global_x = global_x
        self.global_y = global_y
        self.columns = columns
        self.rows = rows
        self.width = width
        self.height = height
        self.sprite_size = sprite_size
        self.sprites = sprites
        self.grid = []
        self.unhidden_tiles = 0

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

        return neighbors

    def create_grid(self, mine_count):
        self.grid = [[Tile(i, j) for j in range(self.columns)] for i in range(self.rows)]

        mines = []
        while len(mines) < mine_count:
            rand_row = random.randrange(0, self.rows)
            rand_column = random.randrange(0, self.columns)
            rand_pos = rand_row, rand_column

            if rand_pos in mines:
                continue
            else:
                mines.append(rand_pos)
                self.grid[rand_row][rand_column].tile_type = TileType.MINE

        for mine in mines:
            neighbors = self.get_neighbor_tiles(mine[0], mine[1])
            for neighbor in neighbors:
                if neighbor.tile_type.value >= 0:
                    neighbor.tile_type = TileType(neighbor.tile_type.value + 1)

    def draw_grid(self):
        for row in range(self.rows):
            for column in range(self.columns):
                self.draw_tile(row, column)

    def draw_tile(self, row, column):
        x = self.global_x + column * self.sprite_size
        y = self.global_y + row * self.sprite_size

        if not self.grid[row][column].is_hidden:
            match self.grid[row][column].tile_type:
                case TileType.MINE:
                    self.surface.blit(self.sprites["MINE_TILE"], (x, y))
                case TileType.EMPTY:
                    self.surface.blit(self.sprites["EMPTY_TILE"], (x, y))
                case TileType.ONE:
                    self.surface.blit(self.sprites["ONE_TILE"], (x, y))
                case TileType.TWO:
                    self.surface.blit(self.sprites["TWO_TILE"], (x, y))
                case TileType.THREE:
                    self.surface.blit(self.sprites["THREE_TILE"], (x, y))
                case TileType.FOUR:
                    self.surface.blit(self.sprites["FOUR_TILE"], (x, y))
                case TileType.FIVE:
                    self.surface.blit(self.sprites["FIVE_TILE"], (x, y))
                case TileType.SIX:
                    self.surface.blit(self.sprites["SIX_TILE"], (x, y))
                case TileType.SEVEN:
                    self.surface.blit(self.sprites["SEVEN_TILE"], (x, y))
                case TileType.EIGHT:
                    self.surface.blit(self.sprites["EIGHT_TILE"], (x, y))
        else:
            if self.grid[row][column].is_flagged:
                self.surface.blit(self.sprites["FLAG_TILE"], (x, y))
            else:
                self.surface.blit(self.sprites["HIDDEN_TILE"], (x, y))

    def reveal_all_tiles(self):
        for row in range(self.rows):
            for column in range(self.columns):
                self.grid[row][column].is_hidden = False
                self.grid[row][column].is_flagged = False
                self.draw_tile(row, column)

    def click_tile(self, row, column):
        self.unhidden_tiles += 1
        self.grid[row][column].is_hidden = False
        self.draw_tile(row, column)

        if self.grid[row][column].tile_type == TileType.MINE:
            return self.grid[row][column].tile_type
        elif self.grid[row][column].tile_type == TileType.EMPTY:
            neighbors = self.get_neighbor_tiles(row, column)
            for neighbor in neighbors:
                if neighbor.is_hidden and not neighbor.is_flagged:
                    if neighbor.tile_type == TileType.EMPTY and neighbor.is_hidden:
                        self.click_tile(neighbor.row, neighbor.column)
                    else:
                        self.unhidden_tiles += 1
                        neighbor.is_hidden = False
                        self.draw_tile(neighbor.row, neighbor.column)
        
        return self.grid[row][column].tile_type

    def flag_tile(self, row, column):
        self.grid[row][column].is_flagged = not self.grid[row][column].is_flagged
        self.draw_tile(row, column)