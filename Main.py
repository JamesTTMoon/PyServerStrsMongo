__author__ = 'James Moon'

import sys
import threading
import datetime



from MyThread  import ThreadClass


"""   class ThreadClass (threading.Thread):
    def run(self):
        now = datetime.datetime.now()
        print ("%s says Hello .. now  %s " %(self.getName(), now))
"""

someObj = ThreadClass()
someObj.openSocket()


for i in range(2):
    t = ThreadClass()
    t.start()

