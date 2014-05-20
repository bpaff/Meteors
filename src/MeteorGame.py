'''
Created on Apr 14, 2014

@author: Steven
'''
import sys, pygame, Asteroid, Ship, ScreenObject, Client, Factory
import ScoreKeeper

class MeteorGame(object):
    over = False
    
    def __init__(self):
        #instantiate ScoreKeeper
        self.score = ScoreKeeper.ScoreKeeper(1)
        #self.player_score = self.score.get_score()
        #NOTE: not using yet, use this when lives = 0 and players chase each other
        self.continue_play = False
    
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
        lifes = font.render("Lives:  " + str(self.lives), 1, (0,0,0))
        screen.blit(lifes,(10,10))
        
        
    def create_meteors(self, time):
        
        if time/5000 > self.asteroid_spawn_counter:
            self.asteroid_spawn_counter += 1
            spawn = time/10000
            x=0
            while x!=spawn:
                Asteroid.AsteroidObject(self)
                x+=1
    
    def display_score(self):
        font = pygame.font.SysFont(None, 20)
        player_score = font.render("Score:" + str(self.score.get_score()), 1, (0,0,0))
        screen.blit(player_score, (10, 20))   
        
    
    def main(self, screen):
        Factory.game = self
        self.asteroid_spawn_counter = 0
        self.screen = screen
        self.sprites=pygame.sprite.Group()
        self.clock=pygame.time.Clock()
        
        white = 255,255,255
        
        ##connect to game server
        client = Client.Client("localhost", 8888)
        client.run()
        
        # instantiate ship        
        Ship.ShipObject(self)
        
        
        # multiple meteors
        for x in range(0,1):
            Asteroid.AsteroidObject(self)
            

                
        while 1:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT: 
                    sys.exit()                
            
            time_passed = self.clock.tick(60)
            
            if not MeteorGame.over:
                screen.fill(white)
                self.create_meteors(pygame.time.get_ticks())
                self.sprites.update(time_passed,events)
                self.display_lives()
                points = ScreenObject.collision_detect_all(self.sprites)
                if (points > 0):
                    self.score.update_score(points)
                self.display_score()
                self.sprites.draw(screen)
            else:
                self.score.stop()    
            pygame.display.flip()
        
if __name__=="__main__":
    pygame.init()
    pygame.display.set_caption("Inf123 - 2to1's Game")
    size = width, height = 600, 500
    screen = pygame.display.set_mode(size)        
    gameinit=MeteorGame()    
    gameinit.main(screen)
    