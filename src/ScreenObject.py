
import pygame 

class ScreenObject(pygame.sprite.Sprite):
    
    img_path = "../images/"
        
    def __init__(self,game,img_name):
        
        super(ScreenObject,self).__init__(game.sprites)
        
        self.image = pygame.image.load(self.img_path + img_name)
        self.rect = self.image.get_rect()
        
        self.screen_width= game.screen.get_width()
        self.screen_height= game.screen.get_height()
        
        self.move_speed = [0,0]
        
    def update(self,time,events):
        self.update_position(time)
        self.screenwrap()
        super(ScreenObject,self).update()
         
    def screenwrap(self):
        if self.rect.left>self.screen_width:
            self.rect.right=0
        if self.rect.top>self.screen_height:
            self.rect.bottom=0
        if self.rect.right<0:
            self.rect.left=self.screen_width
        if self.rect.bottom<0:
            self.rect.top=self.screen_height
            
    def update_position(self,time):
        self.rect= self.rect.move(self.move_speed)
        
            