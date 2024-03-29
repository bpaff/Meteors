'''
Created on Apr 18, 2014

@author: Steven
'''
import ScreenObject, math, pygame, Asteroid, Ship

class BulletObject(ScreenObject.ScreenObject):
    
    def __init__(self, ship, game=None):
        
        self.ship = ship
        self.time_life = 1000
        score = 0
        
        if ship:
            self.game = ship.game
        else:
            self.game = game
            
        super(BulletObject, self).__init__(self.game, "fireball.png")
        
        if ship:
            angle = ship.direction                
            if angle+90>360:
                angle-=360.0
            self.realangle=(angle+90)*math.pi/180
            
            self.speed_x=.25*math.cos(self.realangle)
            self.speed_y=-.25*math.sin(self.realangle)
            self.position_x = self.ship.position_x #+ (self.speed_x * 30)
            self.position_y = self.ship.position_y #+ (self.speed_y * 30)            
                
    def update(self, time, events):
        self.time_life -= time
        
        if self.time_life > 0:
            super(BulletObject,self).update(time,events)
        else:
            super(BulletObject,self).destroy()
    
    def collision_detect(self):
        collisions = pygame.sprite.spritecollide(self, self.game.sprites, 0)
        score = 0
        if len(collisions) > 1:
            for obj in collisions:
                #TODO: ability to kill other objects
                if isinstance(obj,Asteroid.AsteroidObject):
                    score += 10
                    obj.destroy()
                    self.destroy()
                elif isinstance(obj, Ship.ShipObject) and obj != self.ship and obj.invis_time <= 0:
                    score += 100
                    obj.respawn(True)
                    self.destroy()
        if self.ship is not None:
            self.ship.score += score        
        
            
            
            