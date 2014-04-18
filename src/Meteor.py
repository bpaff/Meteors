'''
Created on Apr 14, 2014

@author: Steven
'''
import sys, pygame, ScreenObject, Asteroid, Bullet, Ship
pygame.init()

size = width, height = 600, 500
speed = [0,0]
speedMax = 50

screen = pygame.display.set_mode(size)
white = 255,255,255

##ship = ScreenObject.ScreenObject(screen, "ship.png", (width/2,height/2))
ship = Ship.ShipObject(screen)
ship.rotate=(0,0)

##multiple meteors
mspeed= [1,1]
for x in range(0,6):
    Asteroid.AsteroidObject(screen)

lastTime = pygame.time.get_ticks()

#mapping = {K_UP: (0,-1), K_RIGHT: (1,0)}

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        if event.type ==pygame.KEYDOWN and event.key == pygame.K_SPACE:
            Bullet.BulletObject(screen)
        if event.type== pygame.KEYDOWN and event.key == pygame.K_UP and abs(speed[1]) < speedMax:
            speed[1] = speed[1] - 1;
        if event.type== pygame.KEYDOWN and event.key == pygame.K_DOWN and abs(speed[1]) < speedMax:
            speed[1] = speed[1] + 1;  
        if event.type== pygame.KEYDOWN and event.key == pygame.K_LEFT and abs(speed[0]) < speedMax:
            speed[0] = speed[0] - 1;
            """ship.rotate+=0.5
            if ship.rotate>360:
                ship.rotate-=360.0
            ship.img = pygame.transform.rotate(ship.img,ship.rotate)"""
        if event.type== pygame.KEYDOWN and event.key == pygame.K_RIGHT and abs(speed[0]) < speedMax:
            speed[0] = speed[0] + 1;
            """if ship.rotate<0.0:
                ship.rotate+=360.0
            ship.img = pygame.transform.rotate(ship.img,ship.rotate) """
        if event.type==pygame.MOUSEBUTTONDOWN:
            ##shoot
            ship.rotate = pygame.mouse.get_pos()[0]
            ship.img = pygame.transform.rotate(ship.img,ship.rotate)
          
        
            
    #meteor collision
    if Asteroid.collision_detect(ship):
        ship.rect.left = width/2
        ship.rect.top = height/2
        speed= [0,0]
        
    #update ships move speed
    ship.move_speed = speed
        
    #draw screen
    screen.fill(white)
    ship.draw()
    for b in Bullet.bullets:
        b.draw
   
    for a in Asteroid.asteroids:
        a.draw()            
    pygame.display.flip()