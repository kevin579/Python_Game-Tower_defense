import pygame
from pygame.sprite import Sprite
from settings import Settings
from bullet import Bullet
import math
import random
import sys
class Tower(Sprite):
    def __init__(self,game,type):
        super().__init__()
        self.screen = game.screen 
        self.block_width = game.settings.block_width
        self.block_height = game.settings.block_height
        self.settings = Settings(game)
        self.bullets = pygame.sprite.Group()
        self.type = type
        

        if self.type == 2:
            self.image = pygame.image.load("images//tower_1.png").convert_alpha()
            self.range = 5
            self.damage = 4
            self.freq = 8
            self.speed = 3
            self.type = 1

        elif self.type == 3:
            self.image = pygame.image.load("images//tower_2.png").convert_alpha()
            self.range = 6
            self.damage = 5
            self.freq = 2
            self.speed = 4
            self.type = 2
            
        elif self.type == 4:
            self.image = pygame.image.load("images//tower_3.png").convert_alpha()
            self.range = 7
            self.damage = 6
            self.freq = 1
            self.speed = 5
            self.type = 3

        elif self.type == 5:
            self.image = pygame.image.load("images//tower_4.png").convert_alpha()
            self.range = 8
            self.damage = 5
            self.freq = 10
            self.speed = 6
            self.type = 4

        elif self.type == 6:
            self.image = pygame.image.load("images//tower_5.png").convert_alpha()
            self.range = 8
            self.damage = 15
            self.freq = 4
            self.speed = 8
            self.type = 5

        elif self.type == 7:
            self.image = pygame.image.load("images//tower_6.png").convert_alpha()
            self.range = 10
            self.damage = 30
            self.freq = 1
            self.speed = 10
            self.type = 6

        self.image = pygame.transform.scale(self.image,(self.block_width,self.block_height))

        self.rect = self.image.get_rect()
        # self.image = pygame.transform.rotate(self.image,180)
        self.new_image = self.image

        
    def update(self,enemys,time,game):
        target  = 0
        target_dis = 1000000000000
        
        for enemy in enemys.sprites():
            if enemy.dis<target_dis:
                x_dis = self.rect.x-enemy.x
                y_dis = self.rect.y-enemy.y
                if (x_dis**2+y_dis**2<(self.range*self.block_height)**2):
                    target_dis = enemy.dis 
                    target = enemy

        if isinstance(target,int):
            return

        x_dis = self.rect.x-target.x
        y_dis = self.rect.y-target.y
        if (x_dis**2+y_dis**2>(self.range*self.block_height)**2):
            return
        if y_dis ==0:
            rad =1000
        else:
            rad = x_dis/y_dis
        tan = math.atan(rad)
        ang = tan*180/3.14
        if x_dis <0 and y_dis <0:
            ang+=180
        elif x_dis >0 and y_dis<0:
            ang+=180
        if time%self.freq==0:
            self.fire(game,x_dis,y_dis,self.rect)
        
        self.new_image = self.rot_center(self.image,ang)
        # collision = pygame.sprite.groupcollide(self.bullets,enemys,True,True)
    def shoot(self,enemys):
        # for enemy in enemys:
        #     for bullet in self.bullets.copy():
        #         if bullet.rect.x+bullet.rect.width>enemy.rect.x and bullet.rect.x<enemy.rect.x+enemy.rect.width and \
        #         bullet.rect.y+bullet.rect.height>enemy.rect.y and bullet.rect.y<enemy.rect.y+enemy.rect.height:
        #             enemy.hp-=self.damage
        #             if self.type!=4:
        #                 if self.type !=5:
        #                     self.bullets.remove(bullet)

        #         if bullet.rect.x<0 or bullet.rect.x>self.screen.get_rect().width or bullet.rect.y<0 or bullet.rect.y>self.screen.get_rect().height:
        #             self.bullets.remove(bullet)
        #         enemy.update_hp()


        for bullet in self.bullets.copy():
            for enemy in enemys:
                if bullet.rect.x+bullet.rect.width>enemy.rect.x and bullet.rect.x<enemy.rect.x+enemy.rect.width and \
                bullet.rect.y+bullet.rect.height>enemy.rect.y and bullet.rect.y<enemy.rect.y+enemy.rect.height:
                    enemy.hp-=self.damage
                    if self.type!=4:
                        if self.type !=5:
                            self.bullets.remove(bullet)

                    enemy.update_hp()

            if bullet.rect.x<0 or bullet.rect.x>self.screen.get_rect().width or bullet.rect.y<0 or bullet.rect.y>self.screen.get_rect().height:
                self.bullets.remove(bullet)
            
                    
           


        

    def fire(self,game,x_dis,y_dis,rect):   
        new_bullet = Bullet(game,x_dis,y_dis,rect,self.speed,self.type)
        self.bullets.add(new_bullet)
        

    def draw_tower(self):
        self.screen.blit(self.new_image,self.rect)
        for bullet in self.bullets.sprites():
            bullet.update()
        


    def rot_center(self,image, angle):
        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image
     