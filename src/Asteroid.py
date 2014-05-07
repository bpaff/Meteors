

import ScreenObject, random
asteroids = []

def collision_detect(screenObject):
    for a in asteroids:
        if a.rect.colliderect(screenObject.rect):
            return True
    return False

class AsteroidObject(ScreenObject.ScreenObject):
        
    def __init__(self, game):
        #todo get random inital cords along edge of screen
        super(AsteroidObject, self).__init__(game, "cloud.png")        
        asteroids.append(self)
        self.game = game
        
        self.speed_x = random.randint(-100,100) * 0.0001
        self.speed_y = random.randint(-100,100) * 0.0001
        
    def kill(self):
        asteroids.remove(self)
        super(AsteroidObject,self).kill()
        if len(asteroids) == 0:
            self.game.game_over(win=True) 
        
        
