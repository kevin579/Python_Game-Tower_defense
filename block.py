import pygame
from pygame.sprite import Sprite 
from settings import Settings

class Block(Sprite):
    def __init__(self,game):
        super().__init__()
        self.screen = game.screen 
        self.screen_rect = game.screen_rect
        # self.height = game.screen_width//10
        # self.weight = game.screen_height//6

        self.image = pygame.image.load("images//block.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(game.settings.block_width,game.settings.block_height))
        self.rect = self.image.get_rect()

    def draw_block(self):
        self.screen.blit(self.image,self.rect)