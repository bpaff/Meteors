import ScreenObject, random
import threading

lock = threading.Lock()


class AsteroidObject(ScreenObject.ScreenObject):
        
    def __init__(self, game, id=None):
        #todo get random inital cords along edge of screen
        super(AsteroidObject, self).__init__(game, "Asteroid.png", id)        
        
        self.game = game
        
        self.speed_x = random.randint(-100,100) * 0.0001
        self.speed_y = random.randint(-100,100) * 0.0001
        
    def destroy(self):
        
        lock.acquire()
        try:
            super(AsteroidObject,self).destroy()
        finally:
            lock.release()
         
        
        
