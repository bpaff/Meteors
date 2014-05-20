'''
Created on Apr 18, 2014

@author: Steven
'''
import ScreenObject, math, pygame, Asteroid, Ship
bullets=[]

class BulletObject(ScreenObject.ScreenObject):
    
    def __init__(self, ship):
        super(BulletObject, self).__init__(ship.game, "fireball.png")
        self.ship = ship
        self.time_life = 250.0
        
        angle = ship.direction                
        if angle+90>360:
            angle-=360.0
        self.realangle=(angle+90)*math.pi/180
        
        self.speed_x=1.0*math.cos(self.realangle)
        self.speed_y=-1.0*math.sin(self.realangle)
        
        self.position_x = self.ship.position_x + (self.speed_x * 30)
        self.position_y = self.ship.position_y + (self.speed_y * 30)
                
    def update(self, time, events):
        self.time_life -= time
        
        if self.time_life > 0:
            super(BulletObject,self).update(time,events)
        else:
            super(BulletObject,self).destroy()
    
    def collision_detect(self):
    
        collisions = pygame.sprite.spritecollide(self, self.ship.game.sprites, 0)
        score = 0
        if len(collisions) > 1:
            for o in collisions:
                #TODO: ability to kill other objects
                if isinstance(o,Asteroid.AsteroidObject):
                    score += 10
                elif isinstance(o, Ship.ShipObject):
                    score += 100
                o.destroy()
                self.destroy()

        return score 
        
            
            
            