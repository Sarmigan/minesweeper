from minesweeper.Config import Config
from minesweeper.game_objects.Grid import Grid
import pygame
import unittest

class TestGrid(unittest.TestCase):
    def test_create_grid_rows(self):
        config = Config(ROWS=20)

        pygame.init()
        screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

        TILE_SPRITES = {
            "MINE_TILE": pygame.transform.scale_by(pygame.image.load("minesweeper/resources/sprites/mine_tile.png").convert_alpha(), config.TILE_SPRITE_SCALE),
            "FLAG_TILE": pygame.transform.scale_by(pygame.image.load("minesweeper/resources/sprites/flag_tile.png").convert_alpha(), config.TILE_SPRITE_SCALE),
            "HIDDEN_TILE": pygame.transform.scale_by(pygame.image.load("minesweeper/resources/sprites/hidden_tile.png").convert_alpha(), config.TILE_SPRITE_SCALE),
            "EMPTY_TILE": pygame.transform.scale_by(pygame.image.load("minesweeper/resources/sprites/empty_tile.png").convert_alpha(), config.TILE_SPRITE_SCALE),
            "ONE_TILE": pygame.transform.scale_by(pygame.image.load("minesweeper/resources/sprites/one_tile.png").convert_alpha(), config.TILE_SPRITE_SCALE),
            "TWO_TILE": pygame.transform.scale_by(pygame.image.load("minesweeper/resources/sprites/two_tile.png").convert_alpha(), config.TILE_SPRITE_SCALE),
            "THREE_TILE": pygame.transform.scale_by(pygame.image.load("minesweeper/resources/sprites/three_tile.png").convert_alpha(), config.TILE_SPRITE_SCALE),
            "FOUR_TILE": pygame.transform.scale_by(pygame.image.load("minesweeper/resources/sprites/four_tile.png").convert_alpha(), config.TILE_SPRITE_SCALE),
            "FIVE_TILE": pygame.transform.scale_by(pygame.image.load("minesweeper/resources/sprites/five_tile.png").convert_alpha(), config.TILE_SPRITE_SCALE),
            "SIX_TILE": pygame.transform.scale_by(pygame.image.load("minesweeper/resources/sprites/six_tile.png").convert_alpha(), config.TILE_SPRITE_SCALE),
            "SEVEN_TILE": pygame.transform.scale_by(pygame.image.load("minesweeper/resources/sprites/seven_tile.png").convert_alpha(), config.TILE_SPRITE_SCALE),
            "EIGHT_TILE": pygame.transform.scale_by(pygame.image.load("minesweeper/resources/sprites/eight_tile.png").convert_alpha(), config.TILE_SPRITE_SCALE)
        }

        grid = Grid(screen, config.ROWS, config.COLUMNS, config.GRID_WIDTH, config.GRID_HEIGHT, config.GRID_POS_X, config.GRID_POS_Y, config.SCALED_TILE_SPRITE_SIZE, TILE_SPRITES)
        grid.create_grid(config.MINE_COUNT)

        self.assertEqual(len(grid.grid), config.ROWS)
    
    def test_create_grid_columns(self):
        config = Config(COLUMNS=20)

        pygame.init()
        screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

        TILE_SPRITES = {
            "MINE_TILE": pygame.transform.scale_by(pygame.image.load("minesweeper/resources/sprites/mine_tile.png").convert_alpha(), config.TILE_SPRITE_SCALE),
            "FLAG_TILE": pygame.transform.scale_by(pygame.image.load("minesweeper/resources/sprites/flag_tile.png").convert_alpha(), config.TILE_SPRITE_SCALE),
            "HIDDEN_TILE": pygame.transform.scale_by(pygame.image.load("minesweeper/resources/sprites/hidden_tile.png").convert_alpha(), config.TILE_SPRITE_SCALE),
            "EMPTY_TILE": pygame.transform.scale_by(pygame.image.load("minesweeper/resources/sprites/empty_tile.png").convert_alpha(), config.TILE_SPRITE_SCALE),
            "ONE_TILE": pygame.transform.scale_by(pygame.image.load("minesweeper/resources/sprites/one_tile.png").convert_alpha(), config.TILE_SPRITE_SCALE),
            "TWO_TILE": pygame.transform.scale_by(pygame.image.load("minesweeper/resources/sprites/two_tile.png").convert_alpha(), config.TILE_SPRITE_SCALE),
            "THREE_TILE": pygame.transform.scale_by(pygame.image.load("minesweeper/resources/sprites/three_tile.png").convert_alpha(), config.TILE_SPRITE_SCALE),
            "FOUR_TILE": pygame.transform.scale_by(pygame.image.load("minesweeper/resources/sprites/four_tile.png").convert_alpha(), config.TILE_SPRITE_SCALE),
            "FIVE_TILE": pygame.transform.scale_by(pygame.image.load("minesweeper/resources/sprites/five_tile.png").convert_alpha(), config.TILE_SPRITE_SCALE),
            "SIX_TILE": pygame.transform.scale_by(pygame.image.load("minesweeper/resources/sprites/six_tile.png").convert_alpha(), config.TILE_SPRITE_SCALE),
            "SEVEN_TILE": pygame.transform.scale_by(pygame.image.load("minesweeper/resources/sprites/seven_tile.png").convert_alpha(), config.TILE_SPRITE_SCALE),
            "EIGHT_TILE": pygame.transform.scale_by(pygame.image.load("minesweeper/resources/sprites/eight_tile.png").convert_alpha(), config.TILE_SPRITE_SCALE)
        }
        
        grid = Grid(screen, config.ROWS, config.COLUMNS, config.GRID_WIDTH, config.GRID_HEIGHT, config.GRID_POS_X, config.GRID_POS_Y, config.SCALED_TILE_SPRITE_SIZE, TILE_SPRITES)
        grid.create_grid(config.MINE_COUNT)

        for row in range(config.ROWS):
            self.assertEqual(len(grid.grid[row]), config.COLUMNS)