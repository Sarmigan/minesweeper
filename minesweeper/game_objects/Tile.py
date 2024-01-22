from minesweeper.custom_enums.TileType import TileType

class Tile:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.tile_type = TileType.EMPTY
        self.is_hidden = True
        self.is_flagged = False