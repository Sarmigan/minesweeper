from TileType import TileType
from GameStatus import GameStatus
from GameObjects import Grid, UI
import pygame

# GAME SETTINGS
COLUMNS, ROWS = 9, 9
MINE_COUNT = 10

# TILE SPRITE SETTINGS
ORIGINAL_TILE_SPRITE_SIZE = 16
TILE_SPRITE_SCALE = 4 if max(COLUMNS, ROWS) < 20 else 2 
SCALED_TILE_SPRITE_SIZE = ORIGINAL_TILE_SPRITE_SIZE * TILE_SPRITE_SCALE

# COUNTER SPRITE SETTINGS
ORIGINAL_COUNTER_SPRITE_WIDTH, ORIGINAL_COUNTER_SPRITE_HEIGHT = 13, 23
COUNTER_SPRITE_SCALE = 2 if max(COLUMNS, ROWS) < 20 else 3
SCALED_COUNTER_SPRITE_WIDTH, SCALED_COUNTER_SPRITE_HEIGHT = ORIGINAL_COUNTER_SPRITE_WIDTH * COUNTER_SPRITE_SCALE, ORIGINAL_COUNTER_SPRITE_HEIGHT * COUNTER_SPRITE_SCALE 

# STATUS SPRITE SETTINGS
ORIGINAL_STATUS_SPRITE_SIZE = 24
STATUS_SPRITE_SCALE = 2 if max(COLUMNS, ROWS) < 20 else 3
SCALED_STATUS_SPRITE_SIZE = ORIGINAL_STATUS_SPRITE_SIZE * STATUS_SPRITE_SCALE

# GRID DIMENSION SETTINGS
GRID_WIDTH, GRID_HEIGHT = SCALED_TILE_SPRITE_SIZE * COLUMNS, SCALED_TILE_SPRITE_SIZE * ROWS

# UI DIMENSION SETTINGS
UI_WIDTH, UI_HEIGHT = GRID_WIDTH, SCALED_COUNTER_SPRITE_HEIGHT * 3 if max(COLUMNS, ROWS) < 20 else SCALED_COUNTER_SPRITE_HEIGHT * 2
UI_BORDER_PADDING_X = 0.0125
UI_BORDER_PADDING_Y = 0.125
UI_COUNTER_PADDING = 0.05

# GRID POSITION SETTINGS
GRID_POS_X, GRID_POS_Y = 0,UI_HEIGHT
GRID_COLOR = (128, 128, 128)

# UI POSITION SETTINGS
UI_POS_X, UI_POS_Y = 0,0

# SCREEN SETTINGS
SCREEN_WIDTH = SCALED_TILE_SPRITE_SIZE * COLUMNS
SCREEN_HEIGHT = SCALED_TILE_SPRITE_SIZE * ROWS + UI_HEIGHT

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Minesweeper")

UI_FONT = pygame.font.SysFont('Arial', 20)

TILE_SPRITES = {
    "MINE_TILE": pygame.transform.scale_by(pygame.image.load("./sprites/mine_tile.png").convert_alpha(), TILE_SPRITE_SCALE),
    "FLAG_TILE": pygame.transform.scale_by(pygame.image.load("./sprites/flag_tile.png").convert_alpha(), TILE_SPRITE_SCALE),
    "HIDDEN_TILE": pygame.transform.scale_by(pygame.image.load("./sprites/hidden_tile.png").convert_alpha(), TILE_SPRITE_SCALE),
    "EMPTY_TILE": pygame.transform.scale_by(pygame.image.load("./sprites/empty_tile.png").convert_alpha(), TILE_SPRITE_SCALE),
    "ONE_TILE": pygame.transform.scale_by(pygame.image.load("./sprites/one_tile.png").convert_alpha(), TILE_SPRITE_SCALE),
    "TWO_TILE": pygame.transform.scale_by(pygame.image.load("./sprites/two_tile.png").convert_alpha(), TILE_SPRITE_SCALE),
    "THREE_TILE": pygame.transform.scale_by(pygame.image.load("./sprites/three_tile.png").convert_alpha(), TILE_SPRITE_SCALE),
    "FOUR_TILE": pygame.transform.scale_by(pygame.image.load("./sprites/four_tile.png").convert_alpha(), TILE_SPRITE_SCALE),
    "FIVE_TILE": pygame.transform.scale_by(pygame.image.load("./sprites/five_tile.png").convert_alpha(), TILE_SPRITE_SCALE),
    "SIX_TILE": pygame.transform.scale_by(pygame.image.load("./sprites/six_tile.png").convert_alpha(), TILE_SPRITE_SCALE),
    "SEVEN_TILE": pygame.transform.scale_by(pygame.image.load("./sprites/seven_tile.png").convert_alpha(), TILE_SPRITE_SCALE),
    "EIGHT_TILE": pygame.transform.scale_by(pygame.image.load("./sprites/eight_tile.png").convert_alpha(), TILE_SPRITE_SCALE)
}

COUNTER_SPRITES = {
    1: pygame.transform.scale_by(pygame.image.load("./sprites/one_counter.png").convert_alpha(), COUNTER_SPRITE_SCALE),
    2: pygame.transform.scale_by(pygame.image.load("./sprites/two_counter.png").convert_alpha(), COUNTER_SPRITE_SCALE),
    3: pygame.transform.scale_by(pygame.image.load("./sprites/three_counter.png").convert_alpha(), COUNTER_SPRITE_SCALE),
    4: pygame.transform.scale_by(pygame.image.load("./sprites/four_counter.png").convert_alpha(), COUNTER_SPRITE_SCALE),
    5: pygame.transform.scale_by(pygame.image.load("./sprites/five_counter.png").convert_alpha(), COUNTER_SPRITE_SCALE),
    6: pygame.transform.scale_by(pygame.image.load("./sprites/six_counter.png").convert_alpha(), COUNTER_SPRITE_SCALE),
    7: pygame.transform.scale_by(pygame.image.load("./sprites/seven_counter.png").convert_alpha(), COUNTER_SPRITE_SCALE),
    8: pygame.transform.scale_by(pygame.image.load("./sprites/eight_counter.png").convert_alpha(), COUNTER_SPRITE_SCALE),
    9: pygame.transform.scale_by(pygame.image.load("./sprites/nine_counter.png").convert_alpha(), COUNTER_SPRITE_SCALE),
    0: pygame.transform.scale_by(pygame.image.load("./sprites/zero_counter.png").convert_alpha(), COUNTER_SPRITE_SCALE)
}

STATUS_SPRITES = {
    "PLAYING": pygame.transform.scale_by(pygame.image.load("./sprites/status_playing.png").convert_alpha(), STATUS_SPRITE_SCALE),
    "WIN": pygame.transform.scale_by(pygame.image.load("./sprites/status_win.png").convert_alpha(), STATUS_SPRITE_SCALE),
    "DEAD": pygame.transform.scale_by(pygame.image.load("./sprites/status_dead.png").convert_alpha(), STATUS_SPRITE_SCALE)
}

def get_clicked_tile(mouse_x, mouse_y):
    row = (mouse_y - GRID_POS_Y) // (GRID_HEIGHT / ROWS)
    column = (mouse_x - GRID_POS_X) // (GRID_WIDTH / COLUMNS)

    return int(row), int(column)

def create_new_game():
    game_status = GameStatus.PLAYING
    grid = Grid(screen, ROWS, COLUMNS, GRID_WIDTH, GRID_HEIGHT, GRID_POS_X, GRID_POS_Y, SCALED_TILE_SPRITE_SIZE, TILE_SPRITES)
    grid.create_grid(MINE_COUNT)
    grid.draw_grid()

    ui = UI(screen, UI_WIDTH, UI_HEIGHT, UI_POS_X, UI_POS_Y, UI_BORDER_PADDING_X, UI_BORDER_PADDING_Y, UI_COUNTER_PADDING, SCALED_COUNTER_SPRITE_HEIGHT, SCALED_COUNTER_SPRITE_WIDTH, COUNTER_SPRITES, SCALED_STATUS_SPRITE_SIZE, STATUS_SPRITES, MINE_COUNT)
    ui.draw()

    return game_status, grid, ui

if __name__ == "__main__":
    is_running = True

    game_status, grid, ui = create_new_game()
    
    while is_running:
        if grid.unhidden_tiles == (COLUMNS * ROWS) - MINE_COUNT:
            game_status = GameStatus.WIN
            ui.update_status(game_status)
            grid.reveal_all_tiles()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            if event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                if mouse_x > UI_POS_X + (UI_WIDTH/2 - SCALED_STATUS_SPRITE_SIZE/2) and mouse_y > UI_POS_Y + (UI_HEIGHT/2 - SCALED_STATUS_SPRITE_SIZE/2):
                    if mouse_x < UI_POS_X + (UI_WIDTH/2 - SCALED_STATUS_SPRITE_SIZE/2) + SCALED_STATUS_SPRITE_SIZE and mouse_y < UI_POS_Y + (UI_HEIGHT/2 - SCALED_STATUS_SPRITE_SIZE/2) + SCALED_STATUS_SPRITE_SIZE:
                        game_status, grid, ui = create_new_game()

                if mouse_x > GRID_POS_X and mouse_y > GRID_POS_Y:
                    if mouse_x < GRID_POS_X + GRID_WIDTH and mouse_y < GRID_POS_Y + GRID_HEIGHT:
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