import pygame

class Menu():
    def __init__(self, surface, global_x, global_y, width, height, bg_color, sprite_size, sprites):
        self.surface = surface
        self.global_x = global_x
        self.global_y = global_y
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.sprite_size = sprite_size
        self.sprites = sprites

    def draw(self):
        pygame.draw.rect(self.surface, self.bg_color, (self.global_x, self.global_y, self.width, self.height))

        for i,difficulty in enumerate(self.sprites.keys()):
            self.surface.blit(self.sprites[difficulty], (self.global_x+i*self.sprite_size, self.global_y))
