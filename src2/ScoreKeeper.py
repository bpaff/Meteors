from threading import Timer


class ScoreKeeper(object):
    def __init__(self, time_interval):
        self._timer = None
        self.score = 0
        self.time_elapsed = 0
        self.time_interval = time_interval
        self.is_active = False
    
        #start timing
        self.start()
    
    def _run(self):
        self.is_active = False
        self.start()
        #calculating score
        self.increment_score()
    
    def increment_score(self):
        #1   pt/sec
        self.score += 1
        #10  pt/asteroid
        #100 pt/ship
    
    def update_score(self, obj_type):
        if obj_type == 'AsteroidObject':
            self.score += 10
        elif obj_type == 'ShipObject':
            self.score += 100
    
    def start(self):
        if not self.is_active:
            self._timer = Timer(self.time_interval, self._run)
            self._timer.start()
            self.is_active = True
    
    def stop(self):
        self._timer.cancel()
        self.is_active = False
    
    def get_score(self):
        return self.score