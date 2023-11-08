import pygame
from pygame.sprite import Sprite
from settings import Settings

class Enemy(Sprite):
    def __init__(self,game,type,factor):
        super().__init__()
        self.screen = game.screen 
        self.block_width = game.settings.block_width
        self.block_height = game.settings.block_height
        self.settings = Settings(game)
        self.type = type
        self.dispath = game.dispath
        self.dis = 0
        self.factor = factor
        

        if self.type == "a":
            self.image = pygame.image.load("images//enemy_2.png").convert_alpha()
            self.hp = int(5*factor)
            self.speed = 0.5

        elif self.type == "b":
            self.image = pygame.image.load("images//enemy_3.png").convert_alpha()
            self.hp = int(10*factor)
            self.speed = 0.6

        elif self.type == "c":
            self.image = pygame.image.load("images//enemy_4.png").convert_alpha()
            self.hp = int(45*factor)
            self.speed = 0.6

        elif self.type == "d":
            self.image = pygame.image.load("images//enemy_5.png").convert_alpha()
            self.hp = int(60*factor)
            self.speed = 0.6

        elif self.type == "e":
            self.image = pygame.image.load("images//enemy_6.png").convert_alpha()
            self.hp = int(200*factor)
            self.speed = 0.4

        elif self.type == "f":
            self.image = pygame.image.load("images//enemy_7.png").convert_alpha()
            self.hp = int(250*factor)
            self.speed = 0.4
        
        elif self.type == "g":
            self.image = pygame.image.load("images//enemy_8.png").convert_alpha()
            self.hp = int(100*factor)
            self.speed = 1.2
        
        elif self.type == "h":
            self.image = pygame.image.load("images//enemy_9.png").convert_alpha()
            self.hp = int(115*factor)
            self.speed = 1.5

        elif self.type == "j":
            self.image = pygame.image.load("images//enemy_10.png").convert_alpha()
            self.hp = 5000*factor
            self.speed = 0.5

        elif self.type =="k":
            self.image = pygame.image.load("images//path.png").convert_alpha()
            self.hp = 50000*factor
            self.speed = self.settings.block_height
        self.max_hp = self.hp
       


        self.image = pygame.transform.scale(self.image,(self.block_width,self.block_height))
        self.rect = self.image.get_rect()
        
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.speed_x = 0
        self.speed_y = 0
        self.red = (255, 0, 0)
        self.green = (0,255,0)
        self.hp_bar = pygame.Rect(0,0,self.block_height*0.6,5)
        self.update_hp()


    def update_enemy(self,path):
        self.path = path
        if self.x%self.block_width<=2 and self.y%self.block_height<=2:
            self.x_place = int(self.x//self.block_width)
            self.y_place = int(self.y//self.block_height)
            self.x_place = min(self.settings.num_block_width-1,self.x_place)
            self.y_place = min(self.settings.num_block_height-1,self.y_place)
            if self.x_place ==self.settings.num_block_width-1 and self.y_place ==self.settings.num_block_height-1:
                return
            
            self.dis = self.dispath[self.y_place][self.x_place]*self.block_width

            if self.path[self.y_place][self.x_place] == "<":
                self.speed_x = -self.speed
                self.speed_y = 0
                self.dis+=(self.x%self.block_width)

            elif self.path[self.y_place][self.x_place] == ">":
                self.speed_x = self.speed
                self.speed_y = 0
                self.dis+=(self.block_width-self.x%self.block_width)

            elif self.path[self.y_place][self.x_place] == "I":
                self.speed_y=-self.speed
                self.speed_x = 0
                self.dis+=(self.y%self.block_height)

            elif self.path[self.y_place][self.x_place] == "V":
                self.speed_y = self.speed
                self.speed_x = 0
                self.dis+=(self.block_height-self.y%self.block_height)

        self.x+=self.speed_x
        self.y+=self.speed_y
        self.rect.x=int(self.x)
        self.rect.y=int(self.y)
        self.hp_bar.midbottom = self.rect.midbottom
        

    def update_hp(self):
        self.hp_now = pygame.Rect(0,0,self.block_height*0.6*(self.hp/self.max_hp),5)

    def draw_enemy(self):
        self.hp_now.x = self.hp_bar.x
        self.hp_now.y = self.hp_bar.y

        self.screen.blit(self.image,self.rect)
        if self.type !="k":
            self.screen.fill(self.green,self.hp_bar)
            self.screen.fill(self.red,self.hp_now)
