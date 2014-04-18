'''
Created on Apr 18, 2014

@author: Steven
'''
import ScreenObject, Asteroid, Bullet

ships =[] ##for when we have more ships

def collision_detect(screenObject):
    for a in Asteroid.asteroids:
        if a.rect.colliderect(screenObject.rect):
            ##Destroy ship
            return True
    return False

class ShipObject(ScreenObject.ScreenObject):
    def __init__(self, screen):
        super(ShipObject, self).__init__(screen, "ship.png")
        ships.append(self)
        
    """def shoot(self, Bullet, screen):
        bullet = Bullet.BulletObject(screen)
        bullet.move_speed = self.move_speed"""
        
        

