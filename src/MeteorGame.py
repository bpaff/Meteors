'''
Created on Apr 14, 2014

@author: Steven
'''
import sys, pygame, Asteroid, Ship

class MeteorGame(object):
    
    def main(self, screen):
        self.screen = screen
        self.sprites=pygame.sprite.Group()
        self.clock=pygame.time.Clock()
        
        white = 255,255,255
        
        # instantiate ship        
        Ship.ShipObject(self)
        
        # multiple meteors
        for x in range(0,6):
            Asteroid.AsteroidObject(self)
                
        while 1:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT: 
                    sys.exit()                

            screen.fill(white)
            time_passed = self.clock.tick(60)
            self.sprites.update(time_passed,events)
            self.sprites.draw(screen)
            pygame.display.flip()
                
    
if __name__=="__main__":
    pygame.init()
    pygame.display.set_caption("Inf123 - 2to1's Game")
    size = width, height = 600, 500
    screen = pygame.display.set_mode(size)        
    gameinit=MeteorGame()    
    gameinit.main(screen)
    