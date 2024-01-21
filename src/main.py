from enum import Enum
import pygame
import random

pygame.init()

SPRITE_SIZE = 16

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

GRID_POS_X, GRID_POS_Y = 10,10
GRID_LENGTH = 945
GRID_COLOR = (128, 128, 128)
TILE_PADDING = 5

COLUMNS, ROWS = 9, 9
MINE_COUNT = 10

HIDDEN_TILE_COLOR = (220, 220, 220)
UNHIDDEN_TILE_COLOR = (192, 192, 192)
TILE_TEXT_FONT = pygame.font.SysFont("arial", 20)
TILE_TEXT_COLORS = {
    -1: "red",
    1: "blue",
    2: "chartreuse4",
    3: "firebrick1",
    4: "blue4",
    5: "firebrick4",
    6: "mediumaquamarine",
    7: "black",
    8: "seashell3"
} 

class TileType(Enum):
    MINE = -1
    EMPTY = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8

class Tile:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.tile_type = TileType.EMPTY
        self.is_hidden = True
        self.is_flagged = False

class Grid():
    def __init__(self, surface, rows, columns, length, global_x, global_y) -> None:
        self.surface = surface
        self.global_x = global_x
        self.global_y = global_y
        self.columns = columns
        self.rows = rows
        self.length = length
        self.tile_length = min((length-((self.rows+1)*TILE_PADDING))//self.rows, (length-((self.columns+1)*TILE_PADDING))//self.columns)
        self.grid = []

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

    def draw_grid(self, length):
        pygame.draw.rect(self.surface, GRID_COLOR, (self.global_x, self.global_y, length, length))

        for row in range(self.rows):
            tile_y = self.global_y + TILE_PADDING + row * (self.tile_length + TILE_PADDING)

            for column in range(self.columns):
                tile_x = self.global_x + TILE_PADDING + column * (self.tile_length + TILE_PADDING)

                pygame.draw.rect(self.surface, HIDDEN_TILE_COLOR, (tile_x, tile_y, self.tile_length, self.tile_length))

    def click_tile(self, row, column):
        self.grid[row][column].is_hidden = False
        self.draw_unhidden_tile(row, column)

        if self.grid[row][column].tile_type.value == 0:
            neighbors = self.get_neighbor_tiles(row, column)
            for neighbor in neighbors:
                if neighbor.is_hidden and not neighbor.is_flagged:
                    if neighbor.tile_type.value == 0 and neighbor:
                        self.click_tile(neighbor.row, neighbor.column)
                    else:
                        neighbor.is_hidden = False
                        self.draw_unhidden_tile(neighbor.row, neighbor.column)

    def flag_tile(self, row, column):
        if self.grid[row][column].is_flagged:
            self.grid[row][column].is_flagged = not self.grid[row][column].is_flagged
            self.draw_unflagged_tile(row, column)
        else:
            self.grid[row][column].is_flagged = not self.grid[row][column].is_flagged
            self.draw_flagged_tile(row, column)

    def draw_unhidden_tile(self, row, column):
        tile_x = self.global_x + TILE_PADDING + column * (self.tile_length + TILE_PADDING)
        tile_y = self.global_y + TILE_PADDING + row * (self.tile_length + TILE_PADDING)

        pygame.draw.rect(self.surface, UNHIDDEN_TILE_COLOR, (tile_x, tile_y, self.tile_length, self.tile_length))
        
        if self.grid[row][column].tile_type.value > 0:
            tile_text = TILE_TEXT_FONT.render(str(self.grid[row][column].tile_type.value), 1, TILE_TEXT_COLORS[self.grid[row][column].tile_type.value])
            self.surface.blit(tile_text, (tile_x + (self.tile_length/2 - tile_text.get_width()/2), tile_y + (self.tile_length/2 - tile_text.get_height()/2)))
        elif self.grid[row][column].tile_type == TileType.MINE:
            tile_text = TILE_TEXT_FONT.render(str(self.grid[row][column].tile_type.value), 1, TILE_TEXT_COLORS[self.grid[row][column].tile_type.value])
            self.surface.blit(tile_text, (tile_x + (self.tile_length/2 - tile_text.get_width()/2), tile_y + (self.tile_length/2 - tile_text.get_height()/2)))
            
    def draw_flagged_tile(self, row, column):
        tile_x = self.global_x + TILE_PADDING + column * (self.tile_length + TILE_PADDING)
        tile_y = self.global_y + TILE_PADDING + row * (self.tile_length + TILE_PADDING)

        pygame.draw.rect(self.surface, HIDDEN_TILE_COLOR, (tile_x, tile_y, self.tile_length, self.tile_length))
        tile_text = TILE_TEXT_FONT.render("?", 1, "orange")
        self.surface.blit(tile_text, (tile_x + (self.tile_length/2 - tile_text.get_width()/2), tile_y + (self.tile_length/2 - tile_text.get_height()/2)))

    def draw_unflagged_tile(self, row, column):
        tile_x = self.global_x + TILE_PADDING + column * (self.tile_length + TILE_PADDING)
        tile_y = self.global_y + TILE_PADDING + row * (self.tile_length + TILE_PADDING)

        pygame.draw.rect(self.surface, HIDDEN_TILE_COLOR, (tile_x, tile_y, self.tile_length, self.tile_length))

def get_clicked_tile(mouse_x, mouse_y):
    row = (mouse_y - GRID_POS_Y) // (GRID_LENGTH / ROWS)
    column = (mouse_x - GRID_POS_X) // (GRID_LENGTH / COLUMNS)

    return int(row), int(column)

if __name__ == "__main__":
    is_game_over = False

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    grid = Grid(screen, ROWS, COLUMNS, GRID_LENGTH, GRID_POS_X, GRID_POS_Y)
    grid.create_grid(MINE_COUNT)

    grid.draw_grid(GRID_LENGTH)

    is_running = True
    while is_running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                if mouse_x > GRID_POS_X and mouse_y > GRID_POS_Y:
                    if mouse_x < GRID_POS_X + GRID_LENGTH and mouse_y < GRID_POS_Y + GRID_LENGTH:
                        if event.button == 1:
                            row, column = get_clicked_tile(mouse_x, mouse_y)
                            if grid.grid[row][column].is_hidden: grid.click_tile(row, column)
                        elif event.button == 3:
                            row, column = get_clicked_tile(mouse_x, mouse_y)
                            if grid.grid[row][column].is_hidden: grid.flag_tile(row, column)

        pygame.display.update()

    pygame.quit()