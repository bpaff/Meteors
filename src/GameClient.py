from Network import Handler, poll
import sys, json, ScreenObject, Factory
import pygame
from threading import Thread
from time import sleep
import threading

lock = threading.Lock()

host, port = 'localhost', 8888 
#host, port = '169.234.49.64', 8888

class GameClient(Handler):
    
    def __init__(self):
        Handler.__init__(self, host, port)
        #super(GameClient, self).__init__(host, port)
        
        pygame.init()
        pygame.display.set_caption("Inf123 - 2to1's Game")
        size = width, height = 1024, 768
        self.screen = pygame.display.set_mode(size) 
               
        
        self.asteroid_spawn_counter = 0
        self.sprites=pygame.sprite.Group()
        self.clock=pygame.time.Clock()
        self.laststate = None
        self.state = None
        self.update_objs = []
        self.first_state = None
        self.first_state_loaded = False
        
        self.commands = {}
        self.commands_send_timer = 0
        
        self.score = None
        self.ship_id = None
        self.winner_id = None
        self.top_score = 0
        
    def on_close(self):
        print "Client has Left Game"
        
    def on_msg(self, msg):
        if msg.has_key('SHIP_ID'):
            self.ship_id = msg['SHIP_ID']
            print 'my ship id: ' + self.ship_id
            return 
        if msg.has_key('winner'):
            self.winner_id = msg['winner']
            msg.pop('winner',None)
        else:
            self.winner_id = None
        if msg.has_key('top_score'):
            self.top_score = msg['top_score']
            msg.pop('top_score',None)
            
        if not self.first_state:
            self.first_state = msg
        self.state = msg

    def periodic_poll(self):
        while 1:
            poll()
            sleep(0.005)  # seconds
    
    def updatestate(self):
        if not self.state:
            return
        
        state = self.state
        if not self.first_state_loaded:
            state = self.first_state
            self.first_state_loaded = True
        
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
        time_passed = self.clock.tick(60)
        self.sprites.update(time_passed,events)
        self.process_inputs(time_passed)
        #ScreenObject.collision_detect_all(self.sprites)
        
        return time_passed
    
    def process_inputs(self, time_passed):
        def set_inc(k):
            if self.commands.has_key(k):
                self.commands[k] += time_passed
            else:
                self.commands[k] = time_passed
        
        key=pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            set_inc('LEFT')                                    
        if key[pygame.K_RIGHT]:
            set_inc('RIGHT')                        
        if key[pygame.K_UP]:
            set_inc('UP')
        if key[pygame.K_SPACE]:
            set_inc('SPACE')
                    
        self.commands_send_timer -= time_passed
        if self.commands_send_timer < 0 and len(self.commands.keys()) > 0:
            sendcmds = self.commands.copy()
            self.commands = {}
            self.do_send(sendcmds)
            self.commands_send_timer = 50
            
            
    def drawgame(self):
        white = 255,255,255
        self.screen.fill(white)
        self.sprites.draw(self.screen)
        self.display_lives()
        self.display_score()
        # TODO: Display winner if it exists
        pygame.display.flip()
    
    def display_lives(self):
        my_ship = self.get_my_ship()
        if my_ship:
            font = pygame.font.SysFont(None,20)
            lifes = font.render("Lives:  " + str(my_ship.lives), 1, (0,0,0))
            self.screen.blit(lifes,(10,10))
        
    def display_score(self):
        my_ship =  self.get_my_ship()
        if my_ship:
            font = pygame.font.SysFont(None, 20)
            player_score = font.render("Score:" + str(my_ship.score), 1, (0,0,0))
            self.screen.blit(player_score, (10, 25))
        # display top score
        font = pygame.font.SysFont(None, 20)
        player_score = font.render("Top Score:" + str(self.top_score), 1, (0,0,0))
        self.screen.blit(player_score, (10, 40))
        
        if self.winner_id:
            msg = "You the top dawg"
            if not my_ship or (my_ship.ID != self.winner_id):
                msg = "Try harder next time"
            font = pygame.font.SysFont(None, 30)
            gameover = font.render(msg, 1,(255,0,0))
            self.screen.blit(gameover,(100,100))

        
    def get_my_ship(self):
        for id in ScreenObject.screenObjs:
            if self.ship_id and self.ship_id == id:
                return ScreenObject.screenObjs[id]
        return None
        
    def run(self):                         
        thread = Thread(target=self.periodic_poll)
        thread.daemon = True  # die when the main thread dies 
        thread.start()
        # wait for first state to come in from server
        while not self.state:
            sleep(0.05)
        while 1:            
            self.updatestate()
            time_passed = self.gametick()   
            self.drawgame()      

if __name__=="__main__":
    client = GameClient()
    client.run()
