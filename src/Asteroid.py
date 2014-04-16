

import ScreenObject, random

class AsteroidObject(ScreenObject.ScreenObject):
    
    asteroids = []
    
    def __init__(self, screen):
        #todo get random inital cords along edge of screen
        super(AsteroidObject, self).__init__(screen, "Asteroid.png")
        self.asteroids.append(self)
        self.move_speed = [random.randint(-5,5),random.randint(-5,5)]
        
    @staticmethod
    def collision_detect(screenObject):
        for a in AsteroidObject.asteroids:
            if a.rect.colliderect(screenObject.rect):
                return True
        return False