'''
Created on Apr 13, 2014

@author: Steven
'''
import random
import Meteors
import pygame

class Game(object):
    def __init__(self):
        self.level = 1
        self.sprites=pygame.sprite.Group()
        self.meteors = Meteors.Meteors((0,0),3,random.randrange(360)+1,self.sprites,self.meteors)
        
    def spawn(self):
        for i in range(self.level+1):
            while True:
                x=random.randrange(self.width)
                y=random.randrange(self.height)
                if x==0 or y==0 or x==self.width or y==self.height:
                    Meteors((x,y),3,random.randrange(360)+1,self.sprites,self.meteors)
                    print("got here")
                    break  