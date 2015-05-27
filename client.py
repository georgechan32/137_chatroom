from network import Handler, poll
import sys
from threading import Thread
from time import sleep

#View
def beep():
    print("\a")
def getInput():
    mytemptxt = raw_input("Me " + ' >> ')
    return mytemptxt
def print_msg(msg):
    print(msg)
    global stringSoFar
    stringSoFar = stringSoFar + str(msg) + "\n"

#Controller
class Client(Handler):
    def on_close(self):
        pass
    def on_msg(self, msg):
        print_msg(msg)


def periodic_poll():
    while 1:
        poll()
        sleep(0.05)  # seconds
def parseSubject():
    if len(topic2)>20:
        topic2[:20]
    topic2.replace(" ", "_")

def main_funct():
    v_continue = True 
    while v_continue:
        mytxt = getInput()
        if mytxt == ":q":
            client.do_close()
            v_continue = False
        elif mytxt == ":e":
            beep()
        elif mytxt == ":s":
            file_wr = open(topic2+".txt", 'w+')
            file_wr.write(stringSoFar)
            file_wr.close()
        else:
            client.do_send("Me" + '|' + mytxt)
            global stringSoFar
            stringSoFar = "Me: " + stringSoFar + mytxt+ "\n"


#Model
                           
thread = Thread(target=periodic_poll)
thread.daemon = True  # die when the main thread dies 
thread.start()
topic1 = input("Please select your topic\n 1: Feedback\t2: Complaint\t3: Misc")
topic2 = input("What is the name of the topic? (20 character limit): ")
host, port = 'localhost', 8888
client = Client(host, port)
client.do_send({'join': "Me"})
client.do_send("Me|TOPIC: ("+topic1 +") "+topic2 )
stringSoFar = ""
#client.on_msg('yes')
parseSubject()
main_funct()






