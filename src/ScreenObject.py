
import pygame 
import uuid

screenObjs ={}
screenObjs_killed = []

def collision_detect_all(screenObjects):
    for s in screenObjects:
        s.collision_detect()
    
## get current screen state    
def get_screenState():
    screenstate ={}
    
    # report killed objects
    
    ## get state for existing screen objects
    for x in screenObjs:
        ##for every object        
        obj = screenObjs[x]
        
        #if it's a remote object don't worry about sending it's state 
        if obj.remote:
            continue
        
        ##map object with its position and speed values
        
        screenstate[x] = {
            "position_x": obj.position_x,
            "position_y": obj.position_y, 
            "speed_x":obj.speed_x,
            "speed_y":obj.speed_y,
            "type": obj.__class__.__name__,
            "is_alive": True
        }
        screenstate[x] = "test"
         
    return screenstate

##set new screen state values
def set_screenState(screenstate):
    
    #print screenstate
    ##get all objects and set new position and speed
    for x in screenstate:
        val = screenstate[x]
        if x not in screenObjs.keys():
            pass
            #have game make new object
        
        obj = screenObjs[x]
               
        obj.position_x = val["position_x"]
        obj.position_y= val["position_y"]
        obj.speed_x = val["speed_x"]
        obj.speed_y = val["speed_y"]
        
class ScreenObject(pygame.sprite.Sprite):
    
    img_path = "../images/"
        
    def __init__(self,game,img_name,id=None):
        
        super(ScreenObject,self).__init__(game.sprites)
        
        ##gives each object a unique ID and stores it in a dictionary mapped to its object
        if id==None:
            self.ID = uuid.uuid4().__str__()
            self.remote = False
        else:
            self.ID = id
            self.remote = True;
            
        global screenObjs
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
            