'''
Created on Apr 18, 2014

@author: Steven
'''
import ScreenObject, Bullet, pygame, math
from random import randrange

#ships =[] ##for when we have more ships

class ShipObject(ScreenObject.ScreenObject):
#     count = 0
    
    def __init__(self, game, id=None):
        # Call the parent class constructor
        super(ShipObject, self).__init__(game, "ship2.jpg", id)
        
        #number of lives per player
        self.lives = 3 # 1 life is used during first spawn
        self.respawn(False)
        
        # for tracking and drawing the direction the ship is facing
        self.image_original = self.image        
        
    
    def update(self, time, events):
        if self.invis_time > 0:
            self.invis_time -= time
        if self.time_reload > 0:
            self.time_reload -= time
                    
        self.process_inputs(time, events)
        
        # transform the image with to the direction it should be facing and get the new rectangle
        if self.invis_time > 0:
            self.image_original = pygame.image.load(ScreenObject.img_path+"ship3.jpg")
        else:
            self.image_original = pygame.image.load(ScreenObject.img_path+"ship2.jpg")
        self.image = pygame.transform.rotate(self.image_original, self.direction)
        self.rect = self.image.get_rect(center=self.rect.center)
        
        super(ShipObject,self).update(time,events)
        
    def process_inputs(self, time, events):
        # process key presses
        #    iterate through events                    
        # process key holds
        if not self.remote:
            key=pygame.key.get_pressed()
            if key[pygame.K_LEFT]:
                self.process_command('LEFT', time)            
            if key[pygame.K_RIGHT]:
                self.process_command('RIGHT', time)                        
            if key[pygame.K_UP]:
                self.process_command('UP', time)
            if key[pygame.K_SPACE]:
                self.process_command('SPACE', time)
    
    def process_command(self, command, time):
        if command == "LEFT":
            self.direction+=0.5*time
            if(self.direction > 360): 
                self.direction -= 360  
        if command == "RIGHT":
            self.direction-=0.5*time
            if(self.direction < -360): 
                self.direction += 360
        if command =="UP":
            self.move(time)
        if command == "SPACE":
            self.shoot()
            
            
    def move(self, time):
        x = self.position_x
        y = self.position_y
        realangle=self.direction+90
        if realangle>360:
            realangle-=360.0
        realangle*=math.pi/180
        rady=-math.sin(realangle)
        radx=math.cos(realangle)
        y+=rady * time / 17
        x+=radx * time / 17
        self.position_x = x
        self.position_y = y
        

    def respawn(self, condition):
        self.position_x = randrange(self.screen_width)/2
        self.position_y = randrange(self.screen_height)/2
        self.speed_x = 0
        self.speed_y = 0
        self.direction = 0  
        self.time_reload = 0  
        if condition == True:
            self.lives-=1   
        
        self.invis_time=5000
        if self.lives <= 0:
            self.destroy()
    
    def accelerate(self):
        x = self.speed_x
        y = self.speed_y
        realangle=self.direction+90
        if realangle>360:
            realangle-=360.0
        realangle*=math.pi/180
        rady=-math.sin(realangle)
        radx=math.cos(realangle)
        if (rady<0 and not y<-0.5) or (rady>0 and not y>0.5):
            y+=rady*0.014
        if (radx<0 and not x<-0.5) or (radx>0 and not x>0.5):    
            x+=radx*0.014            
        self.speed_x = x
        self.speed_y = y 
        
    def shoot(self):
        if self.time_reload <= 0:
            self.time_reload = 200 # TODO move this value out to a global constant
            Bullet.BulletObject(self)
            
    def collision_detect(self):
        if self.invis_time <= 0:
            collisions = pygame.sprite.spritecollide(self, self.game.sprites, 0)
            indices = range(0,len(collisions))
            indices.reverse()
            for i in indices:
                obj = collisions[i]
                if obj == self or (obj.__class__.__name__ == "BulletObject" and obj.ship and obj.ship == self):
                    collisions.remove(obj)                
            if len(collisions) > 0:
                self.respawn(True)
        return 0
        