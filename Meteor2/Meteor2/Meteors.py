'''
Created on Apr 15, 2014

@author: Steven
'''
import Object
import pygame

class Meteors(Object):
    def __init__(self, w, h, speed):
        super(Meteors).__init__(w, h)
        meteor = pygame.image.load("Asteroid.png")
        meteorrect = meteor.get_rect()
        meteorrect.left = w/4
        meteorrect.top =  h/4
        self.speed = speed