import sys 
import pygame
from pygame.sprite import Sprite 
import math
class Bullet(Sprite):
    def __init__(self,game,x_dis,y_dis,tower_rect,speed,type):
        super().__init__()
        self.screen = game.screen
        self.speed = speed
        self.speed_x = self.speed/(abs(x_dis)+abs(y_dis))*x_dis 
        self.speed_y = self.speed/(abs(x_dis)+abs(y_dis))*y_dis 
        
        self.type = type
        if self.type ==1:
            self.width = 5
            self.height = 5
            self.bullet_color = (25, 227, 35)

        elif self.type ==2:
            self.width = 6
            self.height = 6
            self.bullet_color = (36, 156, 54)

        elif self.type ==3:
            self.width = 8
            self.height = 8
            self.bullet_color = (46, 99, 33)
        
        elif self.type ==4:
            self.width = 10
            self.height = 10
            self.bullet_color = (28, 132, 145)
        
        elif self.type ==5:
            self.width = 10
            self.height = 10
            self.bullet_color = (38, 120, 130)

        elif self.type ==6:
            self.width = 12
            self.height = 12
            self.bullet_color = (250, 10, 36)

        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = tower_rect.center
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        self.x-=self.speed_x
        self.y-=self.speed_y 
        self.rect.x=int(self.x)
        self.rect.y=int(self.y)
        
        self.screen.fill(self.bullet_color,self.rect)

        