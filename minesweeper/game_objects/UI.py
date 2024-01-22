from minesweeper.custom_enums.GameStatus import GameStatus
from minesweeper.game_objects.Counter import Counter
from minesweeper.utils import get_digits
import pygame

class UI():
    def __init__(self, surface, width, height, global_x, global_y, border_padding_x, border_padding_y, counter_padding, counter_sprite_height, counter_sprite_width, counter_sprites, status_sprite_size, status_sprites, mine_count):
        self.surface = surface
        self.global_x = global_x
        self.global_y = global_y
        self.height = height
        self.width = width
        self.border_padding_x = self.width * border_padding_x
        self.border_padding_y = self.height * border_padding_y
        self.counter_padding = self.width * counter_padding
        self.counter_sprite_height = counter_sprite_height
        self.counter_sprite_width = counter_sprite_width
        self.counter_sprites = counter_sprites
        self.status_sprite_size = status_sprite_size
        self.status_sprites = status_sprites

        self.game_status = GameStatus.PLAYING
        self.flag_counter = Counter()
        self.flag_counter.count = mine_count

    def draw(self):
        ui_border_top_left = (self.global_x + self.border_padding_x, self.global_y + self.border_padding_y)
        ui_border_top_right = (self.global_x + self.width - self.border_padding_x, self.global_y + self.border_padding_y)
        ui_border_bottom_left = (self.global_x + self.border_padding_x, self.global_y + self.height - self.border_padding_y)
        ui_border_bottom_right = (self.global_x + self.width - self.border_padding_x, self.global_y + self.height - self.border_padding_y)

        counter_top_left = (self.global_x + self.counter_padding-1, self.global_y + (self.height/2 - self.counter_sprite_height/2)-1)
        counter_bottom_left = (self.global_x + self.counter_padding-1, self.global_y + (self.height/2 - self.counter_sprite_height/2)+self.counter_sprite_height+1)
        counter_top_right = (self.global_x + self.counter_padding+self.counter_sprite_width*3+1, self.global_y + (self.height/2 - self.counter_sprite_height/2)-1)
        counter_bottom_right = (self.global_x + self.counter_padding+self.counter_sprite_width*3+1, self.global_y + (self.height/2 - self.counter_sprite_height/2)+self.counter_sprite_height+1)

        # Draw UI background
        pygame.draw.rect(self.surface, (192, 192, 192), (self.global_x, self.global_y, self.width, self.height))
        pygame.draw.line(self.surface, (128, 128, 128), ui_border_top_left, ui_border_top_right, 6)
        pygame.draw.line(self.surface, (128, 128, 128), ui_border_top_left, ui_border_bottom_left, 6)
        pygame.draw.line(self.surface, (255, 255, 255), ui_border_bottom_right, ui_border_bottom_left, 6)
        pygame.draw.line(self.surface, (255, 255, 255), ui_border_top_right, ui_border_bottom_right, 6)

        # Draw counter
        counter_x = self.global_x + self.counter_padding
        counter_y = self.global_y + (self.height/2 - self.counter_sprite_height/2)
        for i, digit in enumerate(get_digits(self.flag_counter.count)):
            self.surface.blit(self.counter_sprites[digit], (counter_x + self.counter_sprite_width * i, counter_y))
        pygame.draw.line(self.surface, (128, 128, 128), counter_top_left, counter_top_right, 3)
        pygame.draw.line(self.surface, (128, 128, 128), counter_top_left, counter_bottom_left, 3)
        pygame.draw.line(self.surface, (255, 255, 255), counter_bottom_right, counter_bottom_left, 3)
        pygame.draw.line(self.surface, (255, 255, 255), counter_top_right, counter_bottom_right, 3)

        # Draw status
        status_x = self.global_x + (self.width/2 - self.status_sprite_size/2)
        status_y = self.global_y + (self.height/2 - self.status_sprite_size/2)
        self.surface.blit(self.status_sprites[self.game_status.value], (status_x, status_y))
        
    def update_counter(self, val):
        self.flag_counter.count += val
        self.draw()

    def update_status(self, status):
        self.game_status = status
        self.draw()