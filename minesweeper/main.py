from minesweeper.custom_enums.TileType import TileType
from minesweeper.custom_enums.GameStatus import GameStatus
from minesweeper.game_objects.Grid import Grid
from minesweeper.game_objects.UI import UI
from minesweeper.utils import load_tile_sprites, load_counter_sprites, load_status_sprites
from Config import Config
import pygame

config = Config()
pygame.init()
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption("Minesweeper")

TILE_SPRITES = load_tile_sprites(config)

COUNTER_SPRITES = load_counter_sprites(config)

STATUS_SPRITES = load_status_sprites(config)

def is_click_status(mouse_x, mouse_y):
    if mouse_x > config.UI_POS_X + (config.UI_WIDTH/2 - config.SCALED_STATUS_SPRITE_SIZE/2) and mouse_y > config.UI_POS_Y + (config.UI_HEIGHT/2 - config.SCALED_STATUS_SPRITE_SIZE/2):
        if mouse_x < config.UI_POS_X + (config.UI_WIDTH/2 - config.SCALED_STATUS_SPRITE_SIZE/2) + config.SCALED_STATUS_SPRITE_SIZE and mouse_y < config.UI_POS_Y + (config.UI_HEIGHT/2 - config.SCALED_STATUS_SPRITE_SIZE/2) + config.SCALED_STATUS_SPRITE_SIZE:
            return True
        
    return False

def is_click_grid(mouse_x, mouse_y):
    if mouse_x > config.GRID_POS_X and mouse_y > config.GRID_POS_Y:
        if mouse_x < config.GRID_POS_X + config.GRID_WIDTH and mouse_y < config.GRID_POS_Y + config.GRID_HEIGHT:
            return True
        
    return False

def get_clicked_tile(mouse_x, mouse_y):
    row = (mouse_y - config.GRID_POS_Y) // (config.GRID_HEIGHT / config.ROWS)
    column = (mouse_x - config.GRID_POS_X) // (config.GRID_WIDTH / config.COLUMNS)

    return int(row), int(column)

def create_new_game():
    game_status = GameStatus.PLAYING

    grid = Grid(screen,
                config.ROWS,
                config.COLUMNS,
                config.GRID_WIDTH,
                config.GRID_HEIGHT,
                config.GRID_POS_X,
                config.GRID_POS_Y,
                config.SCALED_TILE_SPRITE_SIZE,
                TILE_SPRITES)
    grid.create_grid(config.MINE_COUNT)
    grid.draw_grid()

    ui = UI(screen,
            config.UI_WIDTH,
            config.UI_HEIGHT,
            config.UI_POS_X,
            config.UI_POS_Y,
            config.UI_BORDER_PADDING_X,
            config.UI_BORDER_PADDING_Y,
            config.UI_COUNTER_PADDING,
            config.SCALED_COUNTER_SPRITE_HEIGHT,
            config.SCALED_COUNTER_SPRITE_WIDTH,
            COUNTER_SPRITES,
            config.SCALED_STATUS_SPRITE_SIZE,
            STATUS_SPRITES,
            config.MINE_COUNT)
    ui.draw()

    return game_status, grid, ui

if __name__ == "__main__":
    is_running = True

    game_status, grid, ui = create_new_game()

    while is_running:
        if grid.unhidden_tiles == (config.COLUMNS * config.ROWS) - config.MINE_COUNT:
            game_status = GameStatus.WIN
            ui.update_status(game_status)
            grid.reveal_all_tiles()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            if event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                if is_click_status(mouse_x, mouse_y):
                    game_status, grid, ui = create_new_game()

                if is_click_grid(mouse_x, mouse_y):
                    if event.button == 1:
                        row, column = get_clicked_tile(mouse_x, mouse_y)
                        
                        if grid.grid[row][column].is_hidden: 
                            clicked_tile = grid.click_tile(row, column)

                            if clicked_tile == TileType.MINE:
                                game_status = GameStatus.DEAD
                                ui.update_status(game_status)
                                grid.reveal_all_tiles()
                    elif event.button == 3:
                        row, column = get_clicked_tile(mouse_x, mouse_y)

                        if grid.grid[row][column].is_hidden:
                            if grid.grid[row][column].is_flagged:
                                grid.flag_tile(row, column)
                                ui.update_counter(+1)
                            elif ui.flag_counter.count > 0:
                                grid.flag_tile(row, column)
                                ui.update_counter(-1)

        pygame.display.update()

    pygame.quit()