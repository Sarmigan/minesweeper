from enum import Enum
from tkinter import *
import time
import random

W_WIDTH = 1280
W_HEIGHT = 720

G_LENGTH = 600

COL_SIZE = 10
ROW_SIZE = 10

BOMB_COUNT = 5

class TileType(Enum):
    EMPTY = "0"
    ONE = "1"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    BOMB = "x"

class Tile:
    def __init__(self, frame) -> None:
        self.btn = Button(frame, width=int(G_LENGTH/COL_SIZE), height=int(G_LENGTH/ROW_SIZE), command=lambda : self.click_tile())
        self.tile_type = TileType.EMPTY
        self.is_hidden = True

    def click_tile(self):
        self.is_hidden = False
        
        self.btn.config(text=f"{self.tile_type.value}")
        self.btn["state"] = DISABLED

class Grid():
    def __init__(self, col_size, row_size, grid_frame) -> None:
        self.col_size = col_size
        self.row_size = row_size
        self.grid_frame = grid_frame
        self.grid = []
        
        for i in range(row_size):
            grid_frame.grid_rowconfigure(i, weight=1)
        
        for i in range(row_size):
            grid_frame.grid_columnconfigure(i, weight=1)

    def create_grid(self):

        self.grid = []

        for i in range(self.row_size):
            temp_row = []
            for j in range(self.col_size):
                temp_tile = Tile(self.grid_frame) 
                temp_row.append(temp_tile)
                temp_tile.btn.grid(row=i, column=j, sticky="nsew")
            self.grid.append(temp_row)

if __name__ == "__main__":
    root =  Tk()
    root.geometry(f"{W_WIDTH}x{W_HEIGHT}")
    root.title("Minesweeper")
    root.resizable(False, False)

    grid_frame = Frame(root, height=G_LENGTH, width=G_LENGTH, background="black")
    grid_frame.place(relx=0.5, rely=0.5, anchor="center")
    grid_frame.grid_propagate(False)

    grid = Grid(COL_SIZE, ROW_SIZE, grid_frame)
    grid.create_grid()

    root.mainloop()