
import pygame 
import uuid

screenObjs ={}

def collision_detect_all(screenObjects):
    for s in screenObjects:
        s.collision_detect()

class ScreenObject(pygame.sprite.Sprite):
    
    img_path = "../images/"
        
    def __init__(self,game,img_name):
        
        super(ScreenObject,self).__init__(game.sprites)
        
        self.ID = uuid.uuid4()
        screenObjs[self.ID] = self
        
        self.image = pygame.image.load(self.img_path + img_name)
        self.rect = self.image.get_rect()
        
        self.screen_width= game.screen.get_width()
        self.screen_height= game.screen.get_height()
        
        self.position_x = 0
        self.position_y = 0
        self.speed_x = 0
        self.speed_y = 0
                
    def update(self,time,events):
        self.update_position(time)
        self.screenwrap()        
         
    def screenwrap(self):
        # wrap horizontal 
        if self.position_x > self.screen_width:
            self.position_x = 0
        if self.position_x < 0:
            self.position_x = self.screen_width        
        # wrap vertical             
        if self.position_y > self.screen_height:
            self.position_y = 0
        if self.position_y < 0:
            self.position_y = self.screen_height        
                        
    def update_position(self,time):
        self.position_x += time * self.speed_x
        self.position_y += time * self.speed_y
        self.rect.center = (self.position_x, self.position_y)
        
    def collision_detect(self):
        pass
            