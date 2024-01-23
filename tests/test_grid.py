from minesweeper.settings.Config import Config
from minesweeper.game_objects.Grid import Grid
from minesweeper.utils import load_tile_sprites
import pygame
import unittest

class TestGrid(unittest.TestCase):
    def test_create_grid_rows(self):
        config = Config(COLUMNS=20, ROWS=20, MINE_COUNT=10)

        pygame.init()
        screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

        TILE_SPRITES = load_tile_sprites(config)

        grid = Grid(screen, config.ROWS, config.COLUMNS, config.GRID_WIDTH, config.GRID_HEIGHT, config.GRID_POS_X, config.GRID_POS_Y, config.SCALED_TILE_SPRITE_SIZE, TILE_SPRITES)
        grid.create_grid(config.MINE_COUNT)

        self.assertEqual(len(grid.grid), config.ROWS)
    
    def test_create_grid_columns(self):
        config = Config(COLUMNS=20, ROWS=20, MINE_COUNT=10)

        pygame.init()
        screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

        TILE_SPRITES = load_tile_sprites(config)
        
        grid = Grid(screen, config.ROWS, config.COLUMNS, config.GRID_WIDTH, config.GRID_HEIGHT, config.GRID_POS_X, config.GRID_POS_Y, config.SCALED_TILE_SPRITE_SIZE, TILE_SPRITES)
        grid.create_grid(config.MINE_COUNT)

        for row in range(config.ROWS):
            self.assertEqual(len(grid.grid[row]), config.COLUMNS)