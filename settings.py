import pygame

class Settings:
    def __init__(self,game):
        
        self.num_block_width = 29
        self.block_width = game.screen_width//self.num_block_width
        # self.block_height = game.screen_height//self.num_block_height
        self.block_height = self.block_width
        self.num_block_height = game.screen_height//self.block_height-2
        self.lowest = self.num_block_height*self.block_height

        self.enemy_speed = 1
        self.price = [10,20,80,300,200,1000,1500]