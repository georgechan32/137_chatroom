from network import Listener, Handler, poll

#------CONTROLLER------
class MyHandler(Handler):
     
    def on_open(self):
        print "Calling Server Open"
        
         
    def on_close(self):
        print "Calling Server Close"
     
    def on_msg(self, msg):
        tempParse = " "
        print "SERVER ON_MSG"
        if len(handlers) < 2:
            tempParse = parseUser(str(msg))
            if tempParse != "%$$--#":
                print "HANDLER INSERT: [" + tempParse + "]"
                handlers[tempParse] = self
            else:
                tempParse = " "
        if tempParse == " ":
            strArr = str(msg).split("|", 2)
            print "["+strArr[0]+"]"
            if strArr[0] == "Me":
                handlers["Admin"].do_send("Customer: "+strArr[1])
            else:
                handlers["Me"].do_send("Admin: "+strArr[1])

    def on_accept(self, msg):
        print "SERVER ON_ACCEPT"
        print msg
        print self

class MyListener(Listener):
    def on_accept(self, h):
        print "MYLISTENER CLASS ON_ACCEPT"
        print h
        print self

def parseUser(msg):
    #print "MSG: " + msg
    if msg.find('join') != -1:
        strArr = msg.split("'")
        return strArr[3]
    else:
        return "%$$--#"
#------MODEL------
handlers = {}  # map client handler to user name
port = 8888
server = MyListener(port, MyHandler)    


#------CONTROLLER------

while 1:
    poll(timeout=0.1) # in seconds