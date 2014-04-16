
import pygame 

class ScreenObject(object):
    
    img_path = "../images/"
    
    def __init__(self,screen,img_name,start_pos = (0,0)):
        super(ScreenObject,self)
        self.gameScreen = screen
        self.img = pygame.image.load(self.img_path + img_name)
        self.rect = self.img.get_rect()
        
        self.width= screen.get_width()
        self.height= screen.get_height()
        
        self.rect.left = start_pos[0]
        self.rect.top = start_pos[1]
        
        self.last_moved_time = 0
        self.move_speed = [0,0]
        
    def draw(self):
        self.update_position()
        self.screenedge()
        self.gameScreen.blit(self.img, self.rect)
        
    def screenedge(self):
        if self.rect.left>self.width:
            self.rect.right=0
        if self.rect.top>self.height:
            self.rect.bottom=0
        if self.rect.right<0:
            self.rect.left=self.width
        if self.rect.bottom<0:
            self.rect.top=self.height
            
    def update_position(self):
        time_now = pygame.time.get_ticks()
        if time_now - self.last_moved_time > 50:
            self.last_moved_time = time_now
            self.rect= self.rect.move(self.move_speed)