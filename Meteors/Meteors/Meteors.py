'''
Created on Apr 8, 2014

@author: Steven
'''
import sys, pygame
import random
import math


        
class Meteors():
    def __init__(self, location, s, bulletangle):
        self.location = location
        self.size=s
        
        #IMAGES
        self.originalimage=pygame.image.load("ship.png").convert_alpha()
        width,height= self.originalimage.get_width()*s,self.originalimage.get_height()*s
        self.image=pygame.transform.scale(self.originalimage,(width,height))
        self.rect=pygame.rect.Rect(location,self.image.get_size())
        
        
        self.direction = random.randrange(21)*2*(random.randrange(7)+1)
        angle=random.randrange(21)*2*(random.randrange(7)+1)
        realangle = angle*math.pi/180
        
#         if location[0]<= 1:
#             self.rect.right=location[0]
#         elif location[0]>= gameinit.width:
#             self.rect.left=location[0]
#         else:
#             self.rect.centerx=location[0]
#         if location[1]<= 1:
#             self.rect.bottom=location[1]
#         elif location[1]>= gameinit.height:
#             self.rect.top=location[1]
#         else:
#             self.rect.centery==location[1]
        
        
        self.speedx = (random.randrange(1)*2-1)*((random.randrange(70)+5))/(80+30*s)*math.cos(realangle)
        self.speedy = (random.randrange(1)*2-1)*((random.randrange(70)+5))/(80+30*s)*math.sin(realangle)
        if self.speedx<-0.6:
            self.speedx=-0.6
        if self.speedx>0.6:
            self.speedx=0.6
        if self.speedy<-0.6:
            self.speedy=-0.6
        if self.speedy>0.6:
            self.speedy=0.6
            
        (self.x,self.y)= self.rect.center
        
    def destroy (self):
        self.kill()
        
    def update(self,time):
#         if gameinit.running:
#             if pygame.sprite.collide_circle(self,gameinit.player) and gameinit.player.invincibility<=0.0:
#                 gameinit.player.explode(time)
        self.x+=0.5*time*self.speedx/(self.size+1)
        self.y+=0.5*time*self.speedy/(self.size+1)
        self.rect.center=(self.x,self.y)
        self.screenedge(time)
  

# class Ship(object, pygame.sprite.Sprite):
#     
#     def __init__(self,location,*groups):
#         super(Ship,self).__init__(*groups)
#         self.originalimage=pygame.image.load("img/ship.png").convert_alpha()
#         self.rect=pygame.rect.Rect(location,self.originalimage.get_size())
#         (self.rect.centerx,self.rect.centery)=location
#         self.rotation=0.0
#         self.speedx=0
#         self.speedy=0
#         self.shot=0
#         self.load=200.0
#         self.invincibility=0.0
#         self.alive=1
#         (self.x,self.y)=self.rect.center





    
    