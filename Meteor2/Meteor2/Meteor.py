'''
Created on Apr 14, 2014

@author: Steven
'''
import sys, pygame 
pygame.init()

size = width, height = 600, 500
speed = [0,0]
speedMax = 50

screen = pygame.display.set_mode(size)
black =255,255,255

ship = pygame.image.load("ship.png")
shiprect = ship.get_rect()
shiprect.left = width/2
shiprect.top = height/2

mspeed= [1,1]
meteor = pygame.image.load("Asteroid.png")
meteorrect = meteor.get_rect()
meteorrect.left = width/4
meteorrect.top =  height/4

lastTime = pygame.time.get_ticks()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        if event.type== pygame.KEYDOWN and event.key == pygame.K_UP and abs(speed[1]) < speedMax:
            speed[1] = speed[1] - 1;
        if event.type== pygame.KEYDOWN and event.key == pygame.K_DOWN and abs(speed[1]) < speedMax:
            speed[1] = speed[1] + 1;
        if event.type== pygame.KEYDOWN and event.key == pygame.K_LEFT and abs(speed[0]) < speedMax:
            speed[0] = speed[0] - 1;
        if event.type== pygame.KEYDOWN and event.key == pygame.K_RIGHT and abs(speed[0]) < speedMax:
            speed[0] = speed[0] + 1;
    
    #test for edge of screen
    if shiprect.left>width:
        shiprect.right=0
    if shiprect.top>height:
        shiprect.bottom=0
    if shiprect.right<0:
        shiprect.left=width
    if shiprect.bottom<0:
        shiprect.top=height
    
    #update position every second
    if pygame.time.get_ticks() - lastTime > 50:
        lastTime = pygame.time.get_ticks() 
        shiprect= shiprect.move(speed)
    ##meteorrect = meteorrect.move(mspeed)
    screen.fill(black)
    screen.blit(ship,shiprect)
    screen.blit(meteor, meteorrect)
    pygame.display.flip()