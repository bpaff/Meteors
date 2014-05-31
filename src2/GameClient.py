from Network import Handler, poll
import sys, json, ScreenObject, Factory
import pygame
from threading import Thread
from time import sleep
import threading

lock = threading.Lock()

host, port = 'localhost', 8888
    
class GameClient(Handler):
    
    def __init__(self):
        Handler.__init__(self, host, port)
        #super(GameClient, self).__init__(host, port)
        
        pygame.init()
        pygame.display.set_caption("Inf123 - 2to1's Game")
        size = width, height = 800, 600
        self.screen = pygame.display.set_mode(size)        
        
        self.asteroid_spawn_counter = 0
        self.sprites=pygame.sprite.Group()
        self.clock=pygame.time.Clock()
        self.laststate = None
        self.state = None
        self.update_objs = []
        
    def on_close(self):
        print "Client has Left Game"
        
    def on_msg(self, msg):
        self.state = msg

    def periodic_poll(self):
        while 1:
            poll()
            sleep(0.005)  # seconds
        
    def updatestate(self):
        if not self.state:
            return
        
        state = self.state
        
        ##get all objects and set new position and speed
        for id in state:
            val = state[id]
            if id not in ScreenObject.screenObjs.keys():
                Factory.MakeScreenObject(self, val,id)                
            else:
                obj = ScreenObject.screenObjs[id]
                Factory.LoadScreenObject(obj, val)
                if obj.is_alive != val["is_alive"]:
                    obj.destroy()
        self.state = None
        
    
        
    def gametick(self):
        events = pygame.event.get()
        print events
        if len(events) > 0:
            raise Exception()
        time_passed = self.clock.tick(60)
        self.sprites.update(time_passed,events)
        ScreenObject.collision_detect_all(self.sprites)
        
        return time_passed
        
    def drawgame(self):
        white = 255,255,255
        self.screen.fill(white)
        self.sprites.draw(self.screen)
        pygame.display.flip()
        
    def run(self):                         
        thread = Thread(target=self.periodic_poll)
        thread.daemon = True  # die when the main thread dies 
        thread.start()
        
        # wait for first state to come in from server
        while not self.state:
            sleep(0.05)
        
        while 1:
            self.updatestate();
            time_passed = self.gametick()   
            self.drawgame()      

if __name__=="__main__":
    client = GameClient()
    client.run()
