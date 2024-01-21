from enum import Enum
import pygame
import random

SPRITE_SIZE = 64

COLUMNS, ROWS = 9, 9
MINE_COUNT = 10

SCREEN_WIDTH = SPRITE_SIZE * COLUMNS
SCREEN_HEIGHT = SPRITE_SIZE * ROWS

GRID_POS_X, GRID_POS_Y = 0,0
GRID_WIDTH, GRID_HEIGHT = SPRITE_SIZE * COLUMNS, SPRITE_SIZE * ROWS
GRID_COLOR = (128, 128, 128)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Minesweeper")

SPRITE = {
    "MINE_TILE": pygame.transform.scale_by(pygame.image.load("./sprites/mine_tile.png").convert_alpha(), SPRITE_SIZE/16),
    "FLAG_TILE": pygame.transform.scale_by(pygame.image.load("./sprites/flag_tile.png").convert_alpha(), SPRITE_SIZE/16),
    "HIDDEN_TILE": pygame.transform.scale_by(pygame.image.load("./sprites/hidden_tile.png").convert_alpha(), SPRITE_SIZE/16),
    "EMPTY_TILE": pygame.transform.scale_by(pygame.image.load("./sprites/empty_tile.png").convert_alpha(), SPRITE_SIZE/16),
    "ONE_TILE": pygame.transform.scale_by(pygame.image.load("./sprites/one_tile.png").convert_alpha(), SPRITE_SIZE/16),
    "TWO_TILE": pygame.transform.scale_by(pygame.image.load("./sprites/two_tile.png").convert_alpha(), SPRITE_SIZE/16),
    "THREE_TILE": pygame.transform.scale_by(pygame.image.load("./sprites/three_tile.png").convert_alpha(), SPRITE_SIZE/16),
    "FOUR_TILE": pygame.transform.scale_by(pygame.image.load("./sprites/four_tile.png").convert_alpha(), SPRITE_SIZE/16),
    "FIVE_TILE": pygame.transform.scale_by(pygame.image.load("./sprites/five_tile.png").convert_alpha(), SPRITE_SIZE/16),
    "SIX_TILE": pygame.transform.scale_by(pygame.image.load("./sprites/six_tile.png").convert_alpha(), SPRITE_SIZE/16),
    "SEVEN_TILE": pygame.transform.scale_by(pygame.image.load("./sprites/seven_tile.png").convert_alpha(), SPRITE_SIZE/16),
    "EIGHT_TILE": pygame.transform.scale_by(pygame.image.load("./sprites/eight_tile.png").convert_alpha(), SPRITE_SIZE/16)
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
    def __init__(self, surface, rows, columns, width, height, global_x, global_y) -> None:
        self.surface = surface
        self.global_x = global_x
        self.global_y = global_y
        self.columns = columns
        self.rows = rows
        self.width = width
        self.height = height
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

    def draw_grid(self):
        for row in range(self.rows):
            for column in range(self.columns):
                self.draw_tile(row, column)

    def draw_tile(self, row, column):
        x = self.global_x + column * SPRITE_SIZE
        y = self.global_y + row * SPRITE_SIZE

        if not self.grid[row][column].is_hidden:
            match self.grid[row][column].tile_type:
                case TileType.MINE:
                    self.surface.blit(SPRITE["MINE_TILE"], (x, y))
                case TileType.EMPTY:
                    self.surface.blit(SPRITE["EMPTY_TILE"], (x, y))
                case TileType.ONE:
                    self.surface.blit(SPRITE["ONE_TILE"], (x, y))
                case TileType.TWO:
                    self.surface.blit(SPRITE["TWO_TILE"], (x, y))
                case TileType.THREE:
                    self.surface.blit(SPRITE["THREE_TILE"], (x, y))
                case TileType.FOUR:
                    self.surface.blit(SPRITE["FOUR_TILE"], (x, y))
                case TileType.FIVE:
                    self.surface.blit(SPRITE["FIVE_TILE"], (x, y))
                case TileType.SIX:
                    self.surface.blit(SPRITE["SIX_TILE"], (x, y))
                case TileType.SEVEN:
                    self.surface.blit(SPRITE["SEVEN_TILE"], (x, y))
                case TileType.EIGHT:
                    self.surface.blit(SPRITE["EIGHT_TILE"], (x, y))
        else:
            if self.grid[row][column].is_flagged:
                self.surface.blit(SPRITE["FLAG_TILE"], (x, y))
            else:
                self.surface.blit(SPRITE["HIDDEN_TILE"], (x, y))

    def reveal_all_tiles(self):
        for row in range(self.rows):
            for column in range(self.columns):
                self.grid[row][column].is_hidden = False
                self.grid[row][column].is_flagged = False
                self.draw_tile(row, column)

    def click_tile(self, row, column):
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
                        neighbor.is_hidden = False
                        self.draw_tile(neighbor.row, neighbor.column)
        
        return self.grid[row][column].tile_type

    def flag_tile(self, row, column):
        self.grid[row][column].is_flagged = not self.grid[row][column].is_flagged
        self.draw_tile(row, column)

def get_clicked_tile(mouse_x, mouse_y):
    row = (mouse_y - GRID_POS_Y) // (GRID_HEIGHT / ROWS)
    column = (mouse_x - GRID_POS_X) // (GRID_WIDTH / COLUMNS)

    return int(row), int(column)

if __name__ == "__main__":
    is_game_over = False

    grid = Grid(screen, ROWS, COLUMNS, GRID_WIDTH, GRID_HEIGHT, GRID_POS_X, GRID_POS_Y)
    grid.create_grid(MINE_COUNT)
    grid.draw_grid()

    is_running = True
    while is_running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                if mouse_x > GRID_POS_X and mouse_y > GRID_POS_Y:
                    if mouse_x < GRID_POS_X + GRID_WIDTH and mouse_y < GRID_POS_Y + GRID_HEIGHT:
                        if event.button == 1:
                            row, column = get_clicked_tile(mouse_x, mouse_y)
                            
                            if grid.grid[row][column].is_hidden: 
                                clicked_tile = grid.click_tile(row, column)
                                if clicked_tile == TileType.MINE:
                                    grid.reveal_all_tiles()

                        elif event.button == 3:
                            row, column = get_clicked_tile(mouse_x, mouse_y)
                            if grid.grid[row][column].is_hidden: grid.flag_tile(row, column)

        pygame.display.update()

    pygame.quit()