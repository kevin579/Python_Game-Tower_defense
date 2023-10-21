import sys
import os
import pygame
from background import Background
from block import Block
from settings import Settings
from enemy import Enemy
from tower import Tower
from multiprocessing.sharedctypes import Value
from pygame.locals import *
from pygame import mixer
# from methods import Methods

class Main:
    def __init__(self):

        pygame.init()
        f = open("waves\progress.txt","r")
        self.life =int(f.readline())
        self.cash = int(f.readline())
        self.wave_num = int(f.readline())
        # self.graph = list(f.readline())
        # print(self.graph)
        f.close()

        # self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.screen = pygame.display.set_mode((int(1366),int(768)))

        self.screen_rect = self.screen.get_rect()
        self.screen_width = self.screen_rect.width
        self.screen_height = self.screen_rect.height 

        self.bg_color = (255,255,0)
        self.t_type = 0
        


        self.settings = Settings(self)
        self.background = Background(self)
        # self.methods = Methods(self)
        self.directory = "waves"
        self.waves = []
        self.load_wave()
        # if not self.graph:
        #     self.graph = [[0 for u in range(self.settings.num_block_width)] for i in range(self.settings.num_block_height)]
        #     f=open("waves\progress.txt","a")
        #     f.write(str(self.graph))
        #     f.close()
        self.graph = [[0 for u in range(self.settings.num_block_width)] for i in range(self.settings.num_block_height)]
        self.path = [[0 for u in range(self.settings.num_block_width)] for i in range(self.settings.num_block_height)]
        self.dispath = [[0 for u in range(self.settings.num_block_width)] for i in range(self.settings.num_block_height)]
        
        self.wave = []
        

        self.blocks = pygame.sprite.Group()
        self.enemys = pygame.sprite.Group()
        self.towers = pygame.sprite.Group()
        
        self.update_path(1,1,0)
        self.enemy_move = 0
        self.timer = 0
        self.tower_time =0
        self.end = 0

        mixer.init()
        mixer.music.load('music\\bensound-summer_ogg_music.ogg')
        mixer.music.play(100)

        pygame.display.set_caption("td")

    def run(self):

        for time in range(10000000):
            if self.life <=0:
                 sys.exit()

            self.background.update_background(self)
            self.update_tower(time)
            self.check_event()

            if self.enemy_move:
                self.run_wave()

            else:               
                self.background.update_intro(self)

            pygame.display.flip()

    def run_wave(self):
        self.update_enemy()
        self.timer+=1
        self.create_enemy()
        self.end_wave()

    def end_wave(self):
         if self.end==1 and len(self.enemys)<1:
            self.cash+=self.wave_num*20+50
            self.end =0
            self.timer = 0
            self.enemy_move = 0
            self.wave_num +=1
            self.wave = [2]
            for tower in self.towers.sprites():
                tower.bullets.empty()

            self.update_progress()

    def update_progress(self):
         tempcash = self.cash
         for xx in self.graph:
              for x in xx:
                   if x!=0:
                        
                        tempcash+=self.settings.price[0]
                        if x !=1:
                             tempcash+=self.settings.price[x-1]
         f = open("waves\progress.txt","w")
         f.write(f"{self.life}\n{tempcash}\n{self.wave_num}\n")
         f.close()


    def update_enemy(self):
         for enemy in self.enemys.copy():
            if enemy.hp<=0:
                self.enemys.remove(enemy)
                if enemy.type == 'a':
                    self.cash+=20
                elif enemy.type == 'b':
                    self.cash+=15
                elif enemy.type == 'c':
                    self.cash+=25
                elif enemy.type == 'd':
                    self.cash+=30
                if enemy.type == 'e':
                    self.cash+=35
                elif enemy.type == 'f':
                    self.cash+=40
                elif enemy.type == 'g':
                    self.cash+=55
                elif enemy.type == 'h':
                    self.cash+=60
            if enemy.rect.x>=self.screen_width-self.settings.block_width-4:
                if enemy.rect.y>=self.settings.lowest-self.settings.block_height-4:
                    self.life-=1
                    self.enemys.remove(enemy)
            
            enemy.update_enemy(self.path)
            enemy.draw_enemy() 

    def update_tower(self,time):
        for block in self.blocks.sprites():
                block.draw_block()
        if time%25==1:
            self.tower_time+=1
            if len(self.enemys.sprites())>0:
                for tower in self.towers.sprites():
                    tower.update(self.enemys,self.tower_time,self)
                    tower.draw_tower()
                    tower.shoot(self.enemys)
            
        for tower in self.towers.sprites():
                    tower.draw_tower()
        if time %3==1:
            for tower in self.towers.sprites():
                tower.shoot(self.enemys)

    def check_event(self):
         for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key ==pygame.K_ESCAPE:
                        sys.exit()

                    elif event.key ==pygame.K_RETURN and self.enemy_move ==0:
                        self.create_fleet(self.wave_num)
                        self.enemy_move = 1

                    elif event.key ==pygame.K_1:
                         self.t_type =0
                    elif event.key ==pygame.K_2:
                        self.t_type =1
                    elif event.key ==pygame.K_3:
                        self.t_type =2
                    elif event.key ==pygame.K_4:
                        self.t_type =3
                    elif event.key ==pygame.K_5:
                        self.t_type =4
                    elif event.key ==pygame.K_6:
                        self.t_type =5
                    elif event.key ==pygame.K_7:
                        self.t_type =6

                    self.background.update_highlight(self,self.t_type)
                
                if self.enemy_move ==0:
                    if event.type ==pygame.MOUSEBUTTONDOWN :
                        mouse_pos = pygame.mouse.get_pos()
                        mouse_x = mouse_pos[0]
                        mouse_y = mouse_pos[1]
                        if mouse_x<self.screen_width-2 and mouse_y<self.settings.lowest-2:
                            graph_x = mouse_x//self.settings.block_width
                            graph_y = mouse_y//self.settings.block_height

                                
                            if self.t_type == 0:
                                self.try_add_block(mouse_pos,graph_x,graph_y)

                            else:
                                    
                                if self.graph[graph_y][graph_x] == 1:
                                    if self.cash>=self.settings.price[self.t_type]:
                                        self.add_tower(graph_x,graph_y)
                                        self.cash-=self.settings.price[self.t_type]
                                else:
                                    if self.graph[graph_y][graph_x] != 0:
                                        self.graph[graph_y][graph_x] = 1
                                        for tower in self.towers.copy():
                                            if tower.rect.collidepoint(mouse_pos):
                                                self.towers.remove(tower) 
                                                self.cash+=self.settings.price[tower.type]
                                                break
            

    def add_tower(self,graph_x,graph_y):
        self.graph[graph_y][graph_x] = self.t_type+1
        new_tower = Tower(self,self.t_type+1)
        new_tower.rect.x = graph_x*self.settings.block_width
        new_tower.rect.y = graph_y*self.settings.block_height
        # new_tower.rect.y-=int(new_tower.rect.height/10)

        self.towers.add(new_tower)
        
        

    def load_wave(self):
        f = open("waves\\l.txt","r")
        tx = f.readlines()
        

        for i in range(len(tx)):
            t = tx[i].split(" ") 
            self.waves.append(t)   


    def create_fleet(self,wave_num):
        tx = self.waves[wave_num]

        for i in tx:
            if i =='\n':
                 break
            elif i.isdigit():
                for j in range(int(i)*5):
                    self.wave.append(0)
            else:
                    self.wave.append(i)
                    blank = 1
                    if i == 'a':
                        blank = 3
                    elif i == 'b':
                        blank = 1
                    elif i == 'c':
                        blank = 3
                    elif i == 'd':
                         blank = 4
                    elif i == 'e':
                         blank = 5
                    elif i == 'f':
                         blank = 2
                    elif i == 'g':
                         blank = 4
                    elif i == 'h':
                         blank = 6
                    elif i == 'j':
                         blank = 1
                    for u in range(blank):
                        self.wave.append(0)


    def create_enemy(self):
        if self.timer%20==0:
            place = self.timer//20
            if place <len(self.wave):

                if self.wave[place]:
                    new_enemy = Enemy(self,self.wave[place],1+self.wave_num*1.25)
                    self.enemys.add(new_enemy)

            else:
                 self.end = 1

    def try_add_block(self,mouse_pos,graph_x,graph_y):
            if not self.graph[graph_y][graph_x] and (graph_x!=self.settings.num_block_width-1 or graph_y!=self.settings.num_block_height-1):
                if self.cash>=self.settings.price[self.t_type]:
                    self.graph[graph_y][graph_x] = 1
                    self.update_path(graph_x,graph_y)
                return
            
            elif self.graph[graph_y][graph_x] == 1:
                self.graph[graph_y][graph_x] = 0
                self.cash+=self.settings.price[self.t_type]
                # sys.exit()
                for block in self.blocks.copy():
                    if block.rect.collidepoint(mouse_pos):
                        self.blocks.remove(block)  
                         

                self.update_path(graph_x,graph_y,0)


    def update_path(self,graph_x,graph_y,add = 1):
        rows = self.settings.num_block_height
        cols = self.settings.num_block_width
        self.path = [[0 for u in range(self.settings.num_block_width)] for i in range(self.settings.num_block_height)]
        self.dispath = [[0 for u in range(self.settings.num_block_width)] for i in range(self.settings.num_block_height)]

        past = [[rows-1,cols-1]]
        start = [[rows-1,cols-1]]
        queque = []
        for j in range(1,2000):
            for point in start:
                if point[0]>0:
                        if self.graph[point[0]-1][point[1]]==0 and [point[0]-1,point[1]]not in past:
                            past.append([point[0]-1,point[1]])
                            queque.append([point[0]-1,point[1]])
                            self.path[point[0]-1][point[1]] = ("V")
                            self.dispath[point[0]-1][point[1]] = j
                    
                if point[0]<rows-1:
                        if self.graph[point[0]+1][point[1]]==0 and [point[0]+1,point[1]]not in past:
                            past.append([point[0]+1,point[1]])
                            queque.append([point[0]+1,point[1]])
                            self.path[point[0]+1][point[1]] = ("I")
                            self.dispath[point[0]+1][point[1]] = j
                            
                            

                if point[1]>0:
                    if self.graph[point[0]][point[1]-1]==0 and [point[0],point[1]-1]not in past:
                            past.append([point[0],point[1]-1])
                            queque.append([point[0],point[1]-1])
                            self.path[point[0]][point[1]-1] = (">")
                            self.dispath[point[0]][point[1]-1] = j

                if point[1]<cols-1:
                    if self.graph[point[0]][point[1]+1]==0 and [point[0],point[1]+1]not in past:
                            past.append([point[0],point[1]+1])
                            queque.append([point[0],point[1]+1])
                            self.path[point[0]][point[1]+1] = ("<")
                            self.dispath[point[0]][point[1]+1] = j
                
            if queque ==[]:
                self.graph[graph_y][graph_x] = 0
                add = 0
                break
            
            start = list(queque)
            queque.clear()
            
            if [0,0] in start:
                 break
        if add:
            self.cash-=self.settings.price[self.t_type]
            new_block = Block(self)
            new_block.rect.x = graph_x*self.settings.block_width
            new_block.rect.y = graph_y*self.settings.block_height
            self.blocks.add(new_block)

  


if __name__ == '__main__':
    game = Main()
    game.run()