from TileType import TileType
from GameStatus import GameStatus
import pygame
import random
import utils

class Tile:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.tile_type = TileType.EMPTY
        self.is_hidden = True
        self.is_flagged = False

class Counter():
    def __init__(self):
        self.count = 0

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

class UI():
    def __init__(self, surface, width, height, global_x, global_y, border_padding_x, border_padding_y, counter_padding, counter_sprite_height, counter_sprite_width, counter_sprites, status_sprite_size, status_sprites, mine_count):
        self.surface = surface
        self.global_x = global_x
        self.global_y = global_y
        self.height = height
        self.width = width
        self.border_padding_x = self.width * border_padding_x
        self.border_padding_y = self.height * border_padding_y
        self.counter_padding = self.width * counter_padding
        self.counter_sprite_height = counter_sprite_height
        self.counter_sprite_width = counter_sprite_width
        self.counter_sprites = counter_sprites
        self.status_sprite_size = status_sprite_size
        self.status_sprites = status_sprites

        self.game_status = GameStatus.PLAYING
        self.flag_counter = Counter()
        self.flag_counter.count = mine_count

    def draw(self):
        ui_top_left = (self.global_x + self.border_padding_x, self.global_y + self.border_padding_y)
        ui_top_right = (self.global_x + self.width - self.border_padding_x, self.global_y + self.border_padding_y)
        ui_bottom_left = (self.global_x + self.border_padding_x, self.global_y + self.height - self.border_padding_y)
        ui_bottom_right = (self.global_x + self.width - self.border_padding_x, self.global_y + self.height - self.border_padding_y)

        # Draw UI background
        pygame.draw.rect(self.surface, (192, 192, 192), (self.global_x, self.global_y, self.width, self.height))
        pygame.draw.line(self.surface, (128, 128, 128), ui_top_left, ui_top_right, 6)
        pygame.draw.line(self.surface, (128, 128, 128), ui_top_left, ui_bottom_left, 6)
        pygame.draw.line(self.surface, (255, 255, 255), ui_bottom_right, ui_bottom_left, 6)
        pygame.draw.line(self.surface, (255, 255, 255), ui_top_right, ui_bottom_right, 6)

        # Draw counter
        counter_x = self.global_x + self.counter_padding
        counter_y = self.global_y + (self.height/2 - self.counter_sprite_height/2)
        for i, digit in enumerate(utils.get_digits(self.flag_counter.count)):
            self.surface.blit(self.counter_sprites[digit], (counter_x + self.counter_sprite_width * i, counter_y + self.global_y))

        # Draw status
        status_x = self.global_x + (self.width/2 - self.status_sprite_size/2)
        status_y = self.global_y + (self.height/2 - self.status_sprite_size/2)
        self.surface.blit(self.status_sprites[self.game_status.value], (status_x, status_y))
        

    def update_counter(self, val):
        self.flag_counter.count += val
        self.draw()

    def update_status(self, status):
        self.game_status = status
        self.draw()