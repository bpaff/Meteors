from Network import Listener, Handler, poll
import sys
import Network

clients = []
 
class MyHandler(Handler):
        
    def on_open(self):
        print 'client connected'
        # capture reference to the connected client
        clients.append(self)
        
    def on_close(self):
        print 'client left'
        clients.remove(self)
        # destroy all objects which belong to that client
        # msg all other clients about new object state 
    
    def on_msg(self, msg):
        # send msg to all other clients
        for c in clients:
            if c != self:
                print 'sending msg'
                c.do_send(msg)

class Server:
    def run(self):
        port = 8888
        s = Listener(port, MyHandler)
        print"running"
        while 1:
            poll(timeout=0.01) # in seconds

# Uncomment to run the server            
server = Server()
server.run()       
