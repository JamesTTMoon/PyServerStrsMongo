__author__ = 'James Moon'

import sys
import threading
import datetime
import socket
import time

class ThreadClass (threading.Thread):

    def openSocket(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        svrAddr = ('14.63.222.197', 5001)
        print ('starting up on ')

        #sock.bind(svrAddr)
        sock.connect(svrAddr)

        #sock.listen(1)



        print  ("Start : %s" % time.ctime() )
        time.sleep( 1 )
        print  ("Start : %s" % time.ctime() )
        print ('I woke up !!')

        rcvData = sock.recv(1024)

        print (rcvData)




    def run(self):
        now = datetime.datetime.now()
        print ("%s says Hello .. now  %s " %(self.getName(), now))


