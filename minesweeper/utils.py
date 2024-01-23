import pygame

def get_digits(number):
    units = number % 10
    tens = (number // 10) % 10
    hundreds = number // 100

    return hundreds, tens, units

def load_tile_sprites(config):
    return {
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

def load_counter_sprites(config):
    return {
        1: pygame.transform.scale_by(pygame.image.load("minesweeper/resources/sprites/one_counter.png").convert_alpha(), config.COUNTER_SPRITE_SCALE),
        2: pygame.transform.scale_by(pygame.image.load("minesweeper/resources/sprites/two_counter.png").convert_alpha(), config.COUNTER_SPRITE_SCALE),
        3: pygame.transform.scale_by(pygame.image.load("minesweeper/resources/sprites/three_counter.png").convert_alpha(), config.COUNTER_SPRITE_SCALE),
        4: pygame.transform.scale_by(pygame.image.load("minesweeper/resources/sprites/four_counter.png").convert_alpha(), config.COUNTER_SPRITE_SCALE),
        5: pygame.transform.scale_by(pygame.image.load("minesweeper/resources/sprites/five_counter.png").convert_alpha(), config.COUNTER_SPRITE_SCALE),
        6: pygame.transform.scale_by(pygame.image.load("minesweeper/resources/sprites/six_counter.png").convert_alpha(), config.COUNTER_SPRITE_SCALE),
        7: pygame.transform.scale_by(pygame.image.load("minesweeper/resources/sprites/seven_counter.png").convert_alpha(), config.COUNTER_SPRITE_SCALE),
        8: pygame.transform.scale_by(pygame.image.load("minesweeper/resources/sprites/eight_counter.png").convert_alpha(), config.COUNTER_SPRITE_SCALE),
        9: pygame.transform.scale_by(pygame.image.load("minesweeper/resources/sprites/nine_counter.png").convert_alpha(), config.COUNTER_SPRITE_SCALE),
        0: pygame.transform.scale_by(pygame.image.load("minesweeper/resources/sprites/zero_counter.png").convert_alpha(), config.COUNTER_SPRITE_SCALE)
    }

def load_status_sprites(config):
    return {
        "PLAYING": pygame.transform.scale_by(pygame.image.load("minesweeper/resources/sprites/status_playing.png").convert_alpha(), config.STATUS_SPRITE_SCALE),
        "WIN": pygame.transform.scale_by(pygame.image.load("minesweeper/resources/sprites/status_win.png").convert_alpha(), config.STATUS_SPRITE_SCALE),
        "DEAD": pygame.transform.scale_by(pygame.image.load("minesweeper/resources/sprites/status_dead.png").convert_alpha(), config.STATUS_SPRITE_SCALE)
    }

def load_menu_sprites(config):
    return {
        "BEGINNER": pygame.transform.scale_by(pygame.image.load("minesweeper/resources/sprites/menu_beginner.png").convert_alpha(), config.MENU_SPRITE_SCALE),
        "INTERMEDIATE": pygame.transform.scale_by(pygame.image.load("minesweeper/resources/sprites/menu_intermediate.png").convert_alpha(), config.MENU_SPRITE_SCALE),
        "EXPERT": pygame.transform.scale_by(pygame.image.load("minesweeper/resources/sprites/menu_expert.png").convert_alpha(), config.MENU_SPRITE_SCALE)
    }