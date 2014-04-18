'''
Created on Apr 18, 2014

@author: Steven
'''
import ScreenObject
bullets=[]

class BulletObject(ScreenObject.ScreenObject):
    def __init__(self, screen):
        super(BulletObject, self).__init__(screen, "bullet.png")
        bullets.append(self)
        
