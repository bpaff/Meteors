'''
Created on Apr 14, 2014

@author: Steven
'''
import sys, pygame, Asteroid, Ship, ScreenObject

class MeteorGame(object):
    over = False
    def game_over(self, win):
        msg = "You Win"
        if(not win):
            msg = "You Lose"
            
        MeteorGame.over = True
        font = pygame.font.SysFont(None, 30)
        gameover = font.render(msg, 1,(255,0,0))
        screen.blit(gameover,(100,100))
        
        
    
    def display_lives(self):
        self.lives = Ship.ships[0].lives
        font = pygame.font.SysFont(None,20)
        lifes = font.render("Lives: " + str(self.lives), 1, (0,0,0))
        screen.blit(lifes,(10,10))
        
    
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
            
            time_passed = self.clock.tick(60)
            
            self.display_lives()
            if not MeteorGame.over:
                screen.fill(white)
                self.sprites.update(time_passed,events)
                self.display_lives()
                ScreenObject.collision_detect_all(self.sprites)
                self.sprites.draw(screen)
                
            pygame.display.flip()
        
if __name__=="__main__":
    pygame.init()
    pygame.display.set_caption("Inf123 - 2to1's Game")
    size = width, height = 600, 500
    screen = pygame.display.set_mode(size)        
    gameinit=MeteorGame()    
    gameinit.main(screen)
    