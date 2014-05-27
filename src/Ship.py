'''
Created on Apr 18, 2014

@author: Steven
'''
import ScreenObject, Bullet, pygame, math
from random import randrange

ships =[] ##for when we have more ships

class ShipObject(ScreenObject.ScreenObject):
    
    def __init__(self, game, id=None):
        # Call the parent class constructor
        super(ShipObject, self).__init__(game, "ship2.jpg", id)
        self.game = game
        self.invis = False
        #number of lives per player
        self.lives = 3 + 1 # 1 life is used during first spawn
        
        # for tracking and drawing the direction the ship is facing
        self.image_original = self.image        
        
        self.respawn()
                
        ships.append(self)
        
        self.invince =0
    
    
    def update(self, time, events):
        if self.invis_time==200:
            self.invis = False
            self.invis_time=0
        if self.time_reload > 0:
            self.time_reload -= time
            
                    
        self.process_inputs(time, events)
        super(ShipObject,self).update(time,events)
        
        
    def process_inputs2(self, time, button):
        if button == "Left":
            self.direction+=0.5*time
            if(self.direction > 360): 
                self.direction -= 360  
        if button == "Right":
            self.direction-=0.5*time
            if(self.direction < -360): 
                self.direction += 360
        if button =="Up":
            self.move()
        if button == "Space":
            self.shoot()
            
            
    def move(self):
        x = self.position_x
        y = self.position_y
        realangle=self.direction+90
        if realangle>360:
            realangle-=360.0
        realangle*=math.pi/180
        rady=-math.sin(realangle)
        radx=math.cos(realangle)
        y+=rady 
        x+=radx
        self.position_x = x
        self.position_y = y
        
    def respawn(self):
        print "spawn"
        
        self.position_x = randrange(self.screen_width)/2
        self.position_y = randrange(self.screen_height)/2
        self.speed_x = 0
        self.speed_y = 0
        self.direction = 0  
        self.time_reload = 0  
        self.lives-=1   
        self.invis = True
        
        self.invis_time=0
        if self.lives <= 0:
            self.game.game_over(win=False)
        
    def process_inputs(self, time, events):
        # process key presses
        #    iterate through events                    
        # process key holds
        if not self.remote:
            key=pygame.key.get_pressed()
            if key[pygame.K_LEFT]:
                self.direction+=0.5*time
                if(self.direction > 360): self.direction -= 360            
            if key[pygame.K_RIGHT]:
                self.direction-=0.5*time
                if(self.direction < -360): self.direction += 360                        
            if key[pygame.K_UP]:
                self.move()
            if key[pygame.K_SPACE]:
                self.shoot()
                
        # transform the image with to the direction it should be facing and get the new rectangle
        if self.invis:
            self.image_original = pygame.image.load(ScreenObject.img_path+"ship3.jpg")
        else:
            self.image_original = pygame.image.load(ScreenObject.img_path+"ship2.jpg")
        self.image = pygame.transform.rotate(self.image_original, self.direction)
        self.rect = self.image.get_rect(center=self.rect.center)
        

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
        if self.invis:
            self.invis_time+=1
            pass
        else:
            collisions = pygame.sprite.spritecollide(self, self.game.sprites, 0)
            if len(collisions) > 1:
                self.respawn()
        return 0
        