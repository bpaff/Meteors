from Network import Handler, poll
import sys, json, ScreenObject
from threading import Thread
from time import sleep


host, port = 'localhost', 8888
class Client(Handler):
    
    def on_close(self):
        print "Client has Left Game"
        
    
    def on_msg(self, msg):
        ##keys from dictionary, correspond to objects that have changed
        for x in msg:
            ##get the object from key 'x'
            obj = ScreenObject.screenObjs.get(x)
            ##Dictionary of property names and values
            vals = msg[x]
            for v in vals:
                ##loading new values from msg dictionary
                obj[v]= vals[v]  
                
                
    def send(self, msg):
        print msg
        ##send stuff back to the server
            
        

##client = Client(host, port)
##client.do_send({'join': myname})

    def periodic_poll(self):
        while 1:
            poll()
            sleep(0.05)  # seconds
            
    def run(self):                         
        thread = Thread(target=self.periodic_poll)
        thread.daemon = True  # die when the main thread dies 
        thread.start()
        
        while 1:
            mytxt = sys.stdin.readline().rstrip()
            #client.do_send({'speak': myname, 'txt': mytxt})
            if mytxt =="quit":
            ##client.do_send({'speak': myname, 'txt': "client has left"})
                self.on_close()
                break
            else:
            ##client.do_send({'speak': myname, 'txt': mytxt})
    