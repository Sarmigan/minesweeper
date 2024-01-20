from enum import Enum
import pygame
import random

pygame.init()

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

GRID_POS_X, GRID_POS_Y = 10,10
GRID_LENGTH = 945
GRID_COLOR = (128, 128, 128)
TILE_PADDING = 5

COLUMNS, ROWS = 9, 9
MINE_COUNT = 10

TILE_COLOR = (192, 192, 192)
TILE_TEXT_FONT = pygame.font.SysFont("arial", 20)
TILE_TEXT_COLORS = {
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
    def __init__(self):
        self.tile_type = TileType.EMPTY
        self.is_hidden = True

class Grid():
    def __init__(self, rows, columns) -> None:
        self.columns = columns
        self.rows = rows
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
        self.grid = [[Tile() for i in range(self.columns)] for i in range(self.rows)]

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

    def draw_grid(self, surface, x, y, length):
        tile_length = min((length-((self.rows+1)*TILE_PADDING))//self.rows, (length-((self.columns+1)*TILE_PADDING))//self.columns)

        pygame.draw.rect(surface, GRID_COLOR, (x, y, length, length))
        for row in range(self.rows):
            tile_y = y + TILE_PADDING + row * (tile_length + TILE_PADDING)

            for column in range(self.columns):
                tile_x = x + TILE_PADDING + column * (tile_length + TILE_PADDING)

                pygame.draw.rect(surface, TILE_COLOR, (tile_x, tile_y, tile_length, tile_length))
                
                if self.grid[row][column].tile_type.value > 0:
                    tile_text = TILE_TEXT_FONT.render(str(self.grid[row][column].tile_type.value), 1, TILE_TEXT_COLORS[self.grid[row][column].tile_type.value])
                    surface.blit(tile_text, (tile_x + (tile_length/2 - tile_text.get_width()/2), tile_y + (tile_length/2 - tile_text.get_height()/2)))
                
if __name__ == "__main__":
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    grid = Grid(ROWS, COLUMNS)
    grid.create_grid(MINE_COUNT)

    grid.draw_grid(screen, GRID_POS_X, GRID_POS_Y, GRID_LENGTH)

    is_running = True
    while is_running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
        
        pygame.display.update()

    pygame.quit()