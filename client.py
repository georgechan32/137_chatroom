from network import Handler, poll
import sys
from threading import Thread
from time import sleep

myname = raw_input("What is your name? ")

#Model
class Client(Handler):
    
    #def on_open(self):


    def on_close(self):
        #pass
        client.do_send("ClientClosed")  #ehh...
        print "Client Closing..."

    def on_msg(self, msg):
        print msg

        
host, port = 'localhost', 8888
client = Client(host, port)
client.do_send({'join': "Me"})
#client.on_msg('yes')
#View

def periodic_poll():
    while 1:
        poll()
        sleep(0.05)  # seconds
                            
thread = Thread(target=periodic_poll)
thread.daemon = True  # die when the main thread dies 
thread.start()

v_continue = True

#Controller
while v_continue:
    mytxt = raw_input(myname + ' >> ')
    if mytxt == ":q":
        client.do_close()
        v_continue = False
    else:
        client.do_send("Me" + '|' + mytxt)