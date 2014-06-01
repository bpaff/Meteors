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
        self.gameServer.spawnclient(self)
        self.gameServer.send_state(0,self)
        
    def on_close(self):
        print 'client left'
        self.gameServer.killclient(self)
        clients.remove(self)
        
    def on_msg(self, msg):
        # send msg to all other clients
        self.gameServer.clientmsg(self, msg)

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
        self.client_inputs = []
        
    def create_meteors(self, time):
        if len(self.ships.keys()) == 0:
            return
        if time/5000 > self.asteroid_spawn_counter:
            self.asteroid_spawn_counter += 1
            spawn = time/10000
            x=0
            while x!=spawn:
                Asteroid.AsteroidObject(self)
                x+=1
    
    def process_client_inputs(self):
        if len(self.client_inputs) == 0:
            return
        for client_input in self.client_inputs:
            for client in client_input:
                commands = client_input[client]
                for cmd_name in commands:
                    time = commands[cmd_name]
                    self.ships[client].process_command(cmd_name,time)
        self.client_inputs = []
        
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
        
    def send_state(self, time_passed, client=None):
        self.send_state_counter -= time_passed
        if not client:
            if self.send_state_counter > 0:
                return        
            self.send_state_counter = 50
        state = {}
        
        #send all the ship positions and new asteroids
        for oID in ScreenObject.screenObjs:
            obj = ScreenObject.screenObjs[oID]
            
            if client or obj.__class__.__name__ == "ShipObject" or obj in self.update_objs:
                    
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
                    state[oID]["lives"] = obj.lives
                    state[oID]["invis_time"] = obj.invis_time
                if state[oID]["type"]== "BulletObject":
                    state[oID]["time_life"]= obj.time_life
        
        if client:
            client.do_send(state)
        else:
            # send state to every client
            for client in self.ships.keys():
                client.do_send(state)
            # clear updated objects
            self.update_objs = []
            
    def clientmsg(self, client, msg):
        self.client_inputs.append({client: msg})
    
    def run(self):
        port = 8888
        s = Listener(port, MyHandler, self)
        
        print"running"
        
        Asteroid.AsteroidObject(self)
        Asteroid.AsteroidObject(self)
        Asteroid.AsteroidObject(self)
        Asteroid.AsteroidObject(self)
        #Ship.ShipObject(self)
        
        while 1:
            poll(timeout=0.001) # in seconds
            self.process_client_inputs()
            time_passed = self.gametick()            
            self.send_state(time_passed)
            self.drawgame()
            
if __name__=="__main__":
    server = MeteorGameServer()
    server.run()       












