

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
        super(AsteroidObject, self).__init__(game, "Asteroid.png")        
        asteroids.append(self)
        speed_factor = 1.0/1000
        self.speed_x = random.randint(-100,100) * speed_factor
        self.speed_y = random.randint(-100,100) * speed_factor
        
        
