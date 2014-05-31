'''
Created on Apr 14, 2014

@author: Steven
'''
from Network import Listener, Handler, poll
import sys, pygame, Asteroid, Ship, ScreenObject
import Network

clients = []
class MyHandler(Handler):
        
    def on_open(self):
        print 'client connected'
        clients.append(self)
        clientid = self.gameServer.spawnclient(self)
        # TODO: msg client with their id
        
    def on_close(self):
        print 'client left'
        self.gameServer.killclient(self)
        clients.remove(self)
        
    def on_msg(self, msg):
        # send msg to all other clients
        self.gameServer.clientmsg(msg)

class MeteorGameServer(object):
    
    def __init__(self):
        
        pygame.init()
        pygame.display.set_caption("Inf123 - 2to1's Game")
        size = width, height = 800, 600
        self.screen = pygame.display.set_mode(size)        
        
        self.asteroid_spawn_counter = 0
        self.sprites=pygame.sprite.Group()
        self.clock=pygame.time.Clock()
        self.ships = {}
        self.send_state_counter = 0
        self.update_objs = []
        
    def create_meteors(self, time):
        if time/5000 > self.asteroid_spawn_counter:
            self.asteroid_spawn_counter += 1
            spawn = time/10000
            x=0
            while x!=spawn:
                Asteroid.AsteroidObject(self)
                x+=1
    
    def gametick(self):
        events = pygame.event.get()
        time_passed = self.clock.tick(60)
        self.create_meteors(pygame.time.get_ticks())
        self.sprites.update(time_passed,events)
        ScreenObject.collision_detect_all(self.sprites)
        return time_passed
        
    def drawgame(self):
        white = 255,255,255
        self.screen.fill(white)
        self.sprites.draw(self.screen)
        pygame.display.flip()
        
    def spawnclient(self, client):
        ship = Ship.ShipObject(self)
        self.ships[client] = ship;
        return ship.ID
    
    def killclient(self, client):
        if self.ships.has_key(client):
            self.ships[client].destroy()
        
    def send_state(self, time_passed):
        self.send_state_counter -= time_passed
        if self.send_state_counter > 0:
            return        
        self.send_state_counter = 100        
    
        state = {}
        
        #send all the ship positions and new asteroids
        for oID in ScreenObject.screenObjs:
            obj = ScreenObject.screenObjs[oID]
            
            if obj.__class__.__name__ == "ShipObject" or obj in self.update_objs:
                    
                # map object with its position and speed values
                state[oID] = {
                    "position_x": obj.position_x,
                    "position_y": obj.position_y, 
                    "speed_x":obj.speed_x,
                    "speed_y":obj.speed_y,
                    "type": obj.__class__.__name__,
                    "is_alive": obj.is_alive
                    
                }
                
                if state[oID]["type"]== "ShipObject":
                    state[oID]["direction"]= obj.direction
        
        self.update_objs = []
        
        # send state to every client
        for client in self.ships.keys():
            client.do_send(state)
            
    def clientmsg(self, msg):
        print "clientsmg: " + msg    
    
    def run(self):
        port = 8888
        s = Listener(port, MyHandler, self)
        
        print"running"
        
        while 1:
            poll(timeout=0.001) # in seconds
            time_passed = self.gametick()
            self.send_state(time_passed)
            self.drawgame()
            
if __name__=="__main__":
    server = MeteorGameServer()
    server.run()       












