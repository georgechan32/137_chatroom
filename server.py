from network import Listener, Handler, poll

#Controller
 
handlers = {}  # map client handler to user name
 
class MyHandler(Handler):
     
    def on_open(self):
        pass
         
    def on_close(self):
        pass
     
    def on_msg(self, msg):
        print msg
    def on_accept(self, msg):
        print msg

class MyListener(Listener):
    def on_accept(self, h):
        print h

port = 8888
server = MyListener(port, MyHandler)

while 1:
    poll(timeout=0.1) # in seconds
    
