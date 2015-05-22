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
 
port = 8888
server = Listener(port, MyHandler)

while 1:
    poll(timeout=0.05) # in seconds
    server.on_accept("yes")
