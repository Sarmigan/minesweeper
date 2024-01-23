class Config():
    def __init__(self,
                 COLUMNS=9,
                 ROWS=9,
                 MINE_COUNT=10,
                 ORIGINAL_TILE_SPRITE_SIZE=16,
                 ORIGINAL_COUNTER_SPRITE_WIDTH=13,
                 ORIGINAL_COUNTER_SPRITE_HEIGHT=23,
                 ORIGINAL_STATUS_SPRITE_SIZE=24,
                 ORIGINAL_MENU_SPRITE_SIZE=30,
                 UI_BORDER_PADDING_X=0.0125,
                 UI_BORDER_PADDING_Y=0.125,
                 UI_COUNTER_PADDING=0.05,
                 MENU_HEIGHT=30,
                 GRID_POS_X=0,
                 UI_POS_X=0,
                 MENU_POS_X=0,
                 MENU_POS_Y=0,
                 MENU_COLOR=(236, 233, 216),
                 DIFFICULTIES=[
                                {
                                    "rows": 9,
                                    "columns": 9,
                                    "mine_count": 10
                                },
                                {
                                    "rows": 16,
                                    "columns": 16,
                                    "mine_count": 40
                                },
                                {
                                    "rows": 16,
                                    "columns": 30,
                                    "mine_count": 99
                                }]):
        
        # GAME SETTINGS
        self.COLUMNS, self.ROWS = COLUMNS, ROWS
        self.MINE_COUNT = MINE_COUNT

        # TILE SPRITE SETTINGS
        self.ORIGINAL_TILE_SPRITE_SIZE = ORIGINAL_TILE_SPRITE_SIZE
        self.TILE_SPRITE_SCALE = 4 if max(self.COLUMNS, self.ROWS) < 20 else 2 
        self.SCALED_TILE_SPRITE_SIZE = self.ORIGINAL_TILE_SPRITE_SIZE * self.TILE_SPRITE_SCALE

        # COUNTER SPRITE SETTINGS
        self.ORIGINAL_COUNTER_SPRITE_WIDTH, self.ORIGINAL_COUNTER_SPRITE_HEIGHT = ORIGINAL_COUNTER_SPRITE_WIDTH, ORIGINAL_COUNTER_SPRITE_HEIGHT
        self.COUNTER_SPRITE_SCALE = 2
        self.SCALED_COUNTER_SPRITE_WIDTH, self.SCALED_COUNTER_SPRITE_HEIGHT = self.ORIGINAL_COUNTER_SPRITE_WIDTH * self.COUNTER_SPRITE_SCALE, self.ORIGINAL_COUNTER_SPRITE_HEIGHT * self.COUNTER_SPRITE_SCALE 

        # STATUS SPRITE SETTINGS
        self.ORIGINAL_STATUS_SPRITE_SIZE = ORIGINAL_STATUS_SPRITE_SIZE
        self.STATUS_SPRITE_SCALE = 2
        self.SCALED_STATUS_SPRITE_SIZE = self.ORIGINAL_STATUS_SPRITE_SIZE * self.STATUS_SPRITE_SCALE

        # MENU SPRITE SETTINGS
        self.ORIGINAL_MENU_SPRITE_SIZE = ORIGINAL_MENU_SPRITE_SIZE
        self.MENU_SPRITE_SCALE = 1
        self.SCALED_MENU_SPRITE_SIZE = self.ORIGINAL_MENU_SPRITE_SIZE * self.MENU_SPRITE_SCALE

        # GRID DIMENSION SETTINGS
        self.GRID_WIDTH, self.GRID_HEIGHT = self.SCALED_TILE_SPRITE_SIZE * self.COLUMNS, self.SCALED_TILE_SPRITE_SIZE * self.ROWS

        # UI DIMENSION SETTINGS
        self.UI_WIDTH, self.UI_HEIGHT = self.GRID_WIDTH, self.SCALED_COUNTER_SPRITE_HEIGHT * 3 if max(self.COLUMNS, self.ROWS) < 20 else self.SCALED_COUNTER_SPRITE_HEIGHT * 2
        self.UI_BORDER_PADDING_X = UI_BORDER_PADDING_X
        self.UI_BORDER_PADDING_Y = UI_BORDER_PADDING_Y
        self.UI_COUNTER_PADDING = UI_COUNTER_PADDING

        # MENU SETTINGS
        self.MENU_COLOR = MENU_COLOR

        #MENU DIMENSION SETTINGS
        self.MENU_WIDTH, self.MENU_HEIGHT = self.GRID_WIDTH, MENU_HEIGHT

        # MENU POSITION SETTINGS
        self.MENU_POS_X, self.MENU_POS_Y = MENU_POS_X,MENU_POS_Y

        # UI POSITION SETTINGS
        self.UI_POS_X, self.UI_POS_Y = UI_POS_X,self.MENU_HEIGHT

        # GRID POSITION SETTINGS
        self.GRID_POS_X, self.GRID_POS_Y = GRID_POS_X, self.UI_HEIGHT + self.UI_POS_Y

        # SCREEN SETTINGS
        self.SCREEN_WIDTH = self.GRID_WIDTH
        self.SCREEN_HEIGHT = self.GRID_HEIGHT + self.UI_HEIGHT + self.MENU_HEIGHT

        # DIFFICULTY SETTINGS
        self.DIFFICULTIES = DIFFICULTIES