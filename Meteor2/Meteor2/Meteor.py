'''
Created on Apr 14, 2014

@author: Steven
'''
import sys, pygame 
pygame.init()

size = width, height = 600, 500
speed = [0,0]


screen = pygame.display.set_mode(size)
black =255,255,255

ship = pygame.image.load("ship.png")
shiprect = ship.get_rect()
shiprect.left = width/2
shiprect.top = height/2

while 1:
    
    shiprect= shiprect.move(speed)
    screen.fill(black)
    for event in pygame.event.get():
        if event.type== pygame.KEYDOWN and event.key == pygame.K_UP:
            speed=[0,-1]
        if event.type== pygame.KEYDOWN and event.key == pygame.K_DOWN:
            speed=[0,1]
        if event.type== pygame.KEYDOWN and event.key == pygame.K_LEFT:
            speed=[-1,0]
        if event.type== pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            speed=[1,0]
    screen.blit(ship,shiprect)
    pygame.display.flip()