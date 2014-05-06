import asynchat
import asyncore
import json
import socket
from time import sleep

class Handler(asynchat.async_chat):
    
    def __init__(self, host, port, sock=None):
        if sock:  # passive side: Handler automatically created by a Listener
            asynchat.async_chat.__init__(self, sock)
        else:  # active side: Handler created manually
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP
            asynchat.async_chat.__init__(self, sock)
            self.connect((host, port))  # asynchronous and non-blocking
        self.set_terminator('\0')
        self._buffer = []
        
    def collect_incoming_data(self, data):
        self._buffer.append(data)

    def found_terminator(self):
        msg = json.loads(''.join(self._buffer))
        self._buffer = []
        self.on_msg(msg)
    
    def handle_close(self):
        self.close()
        self.on_close()

    def handle_connect(self):  # called on the active side
        self.on_open()
        
    # API you can use
    def do_send(self, msg):
        self.push(json.dumps(msg) + '\0')
        
    def do_close(self):
        self.handle_close()  # will call self.on_close
    
    # callbacks you should override
    def on_open(self):
        pass
        
    def on_close(self):
        pass
        
    def on_msg(self, data):
        pass
    
    
class Listener(asyncore.dispatcher):
    
    def __init__(self, port, handler_class):
        asyncore.dispatcher.__init__(self)
        self.handler_class = handler_class
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP
        self.bind(('', port))
        self.listen(5)  # max 5 incoming connections at once (Windows' limit)

    def handle_accept(self):  # called on the passive side
        accept_result = self.accept()
        if accept_result: # None if connection blocked or aborted
            sock, (host, port) = accept_result
            h = self.handler_class(host, port, sock)
            self.on_accept(h)
            h.on_open()
    
    # API you can use
    def stop(self):
        self.close()

    # callbacks you override
    def on_accept(self, h):
        pass
    
    
def poll(timeout=0):
    asyncore.loop(timeout=timeout, count=1) # return right away