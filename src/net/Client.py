from Network import Handler, poll
import sys, json, ScreenObject
from threading import Thread
from time import sleep


host, port = 'localhost', 8888
class Client(Handler):
    
    def on_close(self):
        print "Client has Left Game"
        
    
    def on_msg(self, msg):
        ScreenObject.set_screenState(msg)

            
        

##client = Client(host, port)
##client.do_send({'join': myname})

    def periodic_poll(self):
        while 1:
            self.do_send(ScreenObject.get_screenState())
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