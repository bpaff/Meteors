'''
Created on Apr 18, 2014

@author: Steven
'''
import ScreenObject, math, random
bullets=[]

class BulletObject(ScreenObject.ScreenObject):
    
    def __init__(self, ship):
        self.ready = False
        super(BulletObject, self).__init__(ship.game, "bullet.png")
        self.ship = ship
        self.time_life = 250.0
        
        angle = ship.direction                
        if angle+90>360:
            angle-=360.0
        self.realangle=(angle+90)*math.pi/180
        self.rect.center = ship.rect.center
        
        self.speed_x=1.0*math.cos(self.realangle)
        self.speed_y=-1.0*math.sin(self.realangle)
        
        self.position_x = self.rect.x + self.speed_x * 5
        self.position_y = self.rect.y + self.speed_y * 5
        
        self.ready = True
        
    def update(self, time, events):
        self.time_life -= time
        if self.time_life > 0:
            super(BulletObject,self).update(time,events)
        else:
            super(BulletObject,self).kill()
    
            
            
            
            