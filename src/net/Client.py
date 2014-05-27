from Network import Handler, poll
import sys, json, ScreenObject
from threading import Thread
from time import sleep
from Factory import MakeScreenObject
import threading

getting_screenState = False
lock = threading.Lock()
## get current screen state    
def get_screenState():
    
    global getting_screenState
    getting_screenState = True
    
    screenstate ={}
    # report killed objects
    
    ## get state for existing screen objects
    for x in ScreenObject.screenObjs:
        ##for every object        
        obj = ScreenObject.screenObjs[x]
        
        #if it's a remote object don't worry about sending it's state 
        ##map object with its position and speed values
        screenstate[x] = {
            "position_x": obj.position_x,
            "position_y": obj.position_y, 
            "speed_x":obj.speed_x,
            "speed_y":obj.speed_y,
            "type": obj.__class__.__name__,
            "is_alive": obj.is_alive
            
        }
        if screenstate[x]["type"]== "ShipObject":
            screenstate[x]["direction"]= obj.direction
    
    getting_screenState = False
    return screenstate

##set new screen state values
def set_screenState(screenstate):
    global getting_screenState
    while getting_screenState:
        sleep(0.001)  # seconds
        
    ##get all objects and set new position and speed
    for id in screenstate:
        val = screenstate[id]
        if id not in ScreenObject.screenObjs.keys():
            MakeScreenObject(val["type"],id)
            pass
        
        else:
            obj = ScreenObject.screenObjs[id]
            if obj.is_alive != val["is_alive"]:
                obj.destroy()
            obj.position_x = val["position_x"]
            obj.position_y= val["position_y"]
            obj.speed_x = val["speed_x"]
            obj.speed_y = val["speed_y"]
            if val["type"]== "ShipObject":
                obj.direction = val["direction"]


host, port = 'localhost', 8888
class Client(Handler):
    
    def on_close(self):
        print "Client has Left Game"
        
    def on_msg(self, msg):
        lock.acquire()
        try:
            set_screenState(msg)
        finally:
            lock.release()

##client = Client(host, port)
##client.do_send({'join': myname})

    def periodic_poll(self):
        while 1:
            self.do_send(get_screenState())
            for i in range(1,20):
                poll()
                sleep(0.005)  # seconds
            
    def run(self):                         
        thread = Thread(target=self.periodic_poll)
        thread.daemon = True  # die when the main thread dies 
        thread.start()




'''        
while 1:
mytxt = sys.stdin.readline().rstrip()
#client.do_send({'speak': myname, 'txt': mytxt})
if mytxt =="quit":
##client.do_send({'speak': myname, 'txt': "client has left"})
    self.on_close()
    break
else:
##client.do_send({'speak': myname, 'txt': mytxt})
'''