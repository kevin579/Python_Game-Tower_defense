import pygame
from enemy import Enemy 
from tower import Tower
from settings import Settings

class Background:
    def __init__(self,game):
        self.screen = game.screen 
        self.screen_rect = self.screen.get_rect()
        self.width_block_num = game.settings.num_block_width
        self.height_block_num = game.settings.num_block_height
        self.block_width = game.settings.block_width
        self.block_height = game.settings.block_height
        self.line_color = (135, 131, 130)
        self.lowest = game.settings.lowest
        self.settings = Settings(game)

        self.bg_image = pygame.image.load("images\\bg_img.jpg").convert_alpha()

        self.bg_image = pygame.transform.scale(self.bg_image,(game.screen_width,game.screen_height))
        self.bg_rect = self.bg_image.get_rect()

        self.start_image = pygame.image.load("images\\start.png").convert_alpha()
        self.start_image = pygame.transform.scale(self.start_image,(game.settings.block_width,game.settings.block_height))
        self.start_rect = self.start_image.get_rect()

        self.end_image = pygame.image.load("images\\end.png").convert_alpha()
        self.end_image = pygame.transform.scale(self.end_image,(game.settings.block_width,game.settings.block_height))
        self.end_rect = self.end_image.get_rect()
        self.end_rect.x = game.settings.block_width*(self.width_block_num-1)
        self.end_rect.y = game.settings.block_height*(self.height_block_num-1)

        self.block_image = pygame.image.load("images\\block.png").convert_alpha()
        self.block_image = pygame.transform.scale(self.block_image,(game.settings.block_width,game.settings.block_height))
        self.block_rect = self.block_image.get_rect()
        self.block_rect.x = self.screen_rect.width//10
        self.block_rect.y = game.settings.lowest+self.screen_rect.height//55

        self.tower_image = pygame.image.load("images\\tower_1.png").convert_alpha()
        self.tower_image = pygame.transform.scale(self.tower_image,(game.settings.block_width,game.settings.block_height))
        self.tower_rect = self.tower_image.get_rect()
        self.tower_rect.x = self.screen_rect.width//10*2
        self.tower_rect.y = game.settings.lowest+self.screen_rect.height//55

        self.tower2_image = pygame.image.load("images\\tower_2.png").convert_alpha()
        self.tower2_image = pygame.transform.scale(self.tower2_image,(game.settings.block_width,game.settings.block_height))
        self.tower2_rect = self.tower2_image.get_rect()
        self.tower2_rect.x = self.screen_rect.width//10*3
        self.tower2_rect.y = game.settings.lowest+self.screen_rect.height//55

        self.tower3_image = pygame.image.load("images\\tower_3.png").convert_alpha()
        self.tower3_image = pygame.transform.scale(self.tower3_image,(game.settings.block_width,game.settings.block_height))
        self.tower3_rect = self.tower3_image.get_rect()
        self.tower3_rect.x = self.screen_rect.width//10*4
        self.tower3_rect.y = game.settings.lowest+self.screen_rect.height//55

        self.tower4_image = pygame.image.load("images\\tower_4.png").convert_alpha()
        self.tower4_image = pygame.transform.scale(self.tower4_image,(game.settings.block_width,game.settings.block_height))
        self.tower4_rect = self.tower4_image.get_rect()
        self.tower4_rect.x = self.screen_rect.width//10*5
        self.tower4_rect.y = game.settings.lowest+self.screen_rect.height//55

        self.tower5_image = pygame.image.load("images\\tower_5.png").convert_alpha()
        self.tower5_image = pygame.transform.scale(self.tower5_image,(game.settings.block_width,game.settings.block_height))
        self.tower5_rect = self.tower5_image.get_rect()
        self.tower5_rect.x = self.screen_rect.width//10*6
        self.tower5_rect.y = game.settings.lowest+self.screen_rect.height//55

        self.tower6_image = pygame.image.load("images\\tower_6.png").convert_alpha()
        self.tower6_image = pygame.transform.scale(self.tower6_image,(game.settings.block_width,game.settings.block_height))
        self.tower6_rect = self.tower6_image.get_rect()
        self.tower6_rect.x = self.screen_rect.width//10*7
        self.tower6_rect.y = game.settings.lowest+self.screen_rect.height//55

        self.t1_intro = pygame.image.load("images\\t1_intro.jpg").convert_alpha()
        self.t1_intro = pygame.transform.scale(self.t1_intro,(game.settings.block_width*10,game.settings.block_height*6))
        self.t1_rect = self.t1_intro.get_rect()
        self.t1_rect.x = self.screen_rect.width//10
        self.t1_rect.y = game.settings.lowest-self.screen_rect.height//10*3

        self.t2_intro = pygame.image.load("images\\t2_intro.jpg").convert_alpha()
        self.t2_intro = pygame.transform.scale(self.t2_intro,(game.settings.block_width*10,game.settings.block_height*6))
        self.t2_rect = self.t2_intro.get_rect()
        self.t2_rect.x = self.screen_rect.width//10*2
        self.t2_rect.y = game.settings.lowest-self.screen_rect.height//10*3

        self.t3_intro = pygame.image.load("images\\t3_intro.jpg").convert_alpha()
        self.t3_intro = pygame.transform.scale(self.t3_intro,(game.settings.block_width*10,game.settings.block_height*6))
        self.t3_rect = self.t3_intro.get_rect()
        self.t3_rect.x = self.screen_rect.width//10*3
        self.t3_rect.y = game.settings.lowest-self.screen_rect.height//10*3

        self.t4_intro = pygame.image.load("images\\t4_intro.jpg").convert_alpha()
        self.t4_intro = pygame.transform.scale(self.t4_intro,(game.settings.block_width*10,game.settings.block_height*6))
        self.t4_rect = self.t4_intro.get_rect()
        self.t4_rect.x = self.screen_rect.width//10*4
        self.t4_rect.y = game.settings.lowest-self.screen_rect.height//10*3

        self.t5_intro = pygame.image.load("images\\t5_intro.jpg").convert_alpha()
        self.t5_intro = pygame.transform.scale(self.t5_intro,(game.settings.block_width*10,game.settings.block_height*6))
        self.t5_rect = self.t5_intro.get_rect()
        self.t5_rect.x = self.screen_rect.width//10*5
        self.t5_rect.y = game.settings.lowest-self.screen_rect.height//10*3

        self.t6_intro = pygame.image.load("images\\t6_intro.jpg").convert_alpha()
        self.t6_intro = pygame.transform.scale(self.t6_intro,(game.settings.block_width*10,game.settings.block_height*6))
        self.t6_rect = self.t6_intro.get_rect()
        self.t6_rect.x = self.screen_rect.width//10*6
        self.t6_rect.y = game.settings.lowest-self.screen_rect.height//10*3

        self.t7_intro = pygame.image.load("images\\t7_intro.jpg").convert_alpha()
        self.t7_intro = pygame.transform.scale(self.t7_intro,(game.settings.block_width*10,game.settings.block_height*6))
        self.t7_rect = self.t7_intro.get_rect()
        self.t7_rect.x = self.screen_rect.width//10*7
        self.t7_rect.y = game.settings.lowest-self.screen_rect.height//10*3


        self.bar = pygame.Rect(0,game.settings.lowest,self.screen_rect.width,self.screen_rect.height-game.settings.lowest)
        self.bar_color = (54, 138, 150)
        self.highlight_color = (250,250,250,100)
        self.update_highlight(game,0)

    def update_background(self,game):
        self.cash = game.cash
        self.life = game.life

        self.tp = game.t_type

        self.screen.blit(self.bg_image,self.bg_rect)
        self.draw_rect_alpha(self.screen,self.highlight_color,self.highlight)

        self.text_to_screen(self.screen,"Cash: " + str(self.cash),self.screen_rect.width//10*8,game.settings.lowest+self.screen_rect.height//50,40)
        self.text_to_screen(self.screen,"Life: " + str(self.life),self.screen_rect.width//10*8,game.settings.lowest+self.screen_rect.height//15,40)
        
    def update_intro(self,game):
        mouse_pos = pygame.mouse.get_pos()
        if not game.enemy_move:
            self.update_graph()

        if self.block_rect.collidepoint(mouse_pos):
            self.screen.blit(self.t1_intro,self.t1_rect)
            return 

        if self.tower_rect.collidepoint(mouse_pos):
            self.screen.blit(self.t2_intro,self.t2_rect)
            return 

        if self.tower2_rect.collidepoint(mouse_pos):
            self.screen.blit(self.t3_intro,self.t3_rect)
            return 

        if self.tower3_rect.collidepoint(mouse_pos):
            self.screen.blit(self.t4_intro,self.t4_rect)
            return 

        if self.tower4_rect.collidepoint(mouse_pos):
            self.screen.blit(self.t5_intro,self.t5_rect)
            return 

        if self.tower5_rect.collidepoint(mouse_pos):
            self.screen.blit(self.t6_intro,self.t6_rect)
            return 

        if self.tower6_rect.collidepoint(mouse_pos):
            self.screen.blit(self.t7_intro,self.t7_rect)
            return 
        
    def draw_rect_alpha(self,surface, color, rect):
        shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
        pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
        surface.blit(shape_surf, rect)

    def update_highlight(self,game,tp):
        self.highlight = pygame.Rect((tp+1)*self.screen_rect.width//10-5,game.settings.lowest+self.screen_rect.height//60,self.block_width+10,self.block_height*2-10)

        
    def update_graph(self):
        for i in range(0,self.width_block_num+1):
            pygame.draw.line(self.screen,self.line_color,(i*self.block_width,0),(i*self.block_width,self.lowest))

        for i in range(0,self.height_block_num+1):
            pygame.draw.line(self.screen,self.line_color,(0,i*self.block_height),(self.screen.get_rect().width-4,i*self.block_height))

    def text_to_screen(self,screen, text, x, y, size = 50,color = (0, 0, 0), font_type = 'data/fonts/orecrusherexpand.ttf'):

        text = str(text)
        font = pygame.font.SysFont(font_type, size)
        text = font.render(text, True, color)
        screen.blit(text, (x, y))

